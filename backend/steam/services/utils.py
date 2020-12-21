import asyncio
from dataclasses import dataclass

from lxml import html
from lxml.html import HtmlElement


def get_request_kwargs(request_query: dict):
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
        'X-Prototype-Version': '1.7',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    cookies = {
        'Steam_Language': 'russian'
    }

    params = dict(
        query='',
        start='0',
        count='50',
        dynamic_data='',
        sort_by='_ASC',
        tags='4026',
        infinite='1',
    )
    params.update(request_query)

    url = 'https://store.steampowered.com/search/results/'
    return {
        'url': url,
        'headers': headers,
        'params': params,
        'cookies': cookies,
    }


@dataclass
class Game:
    id: HtmlElement
    tags: HtmlElement
    name: HtmlElement
    img_url: HtmlElement
    release_date: HtmlElement
    user_review: HtmlElement

    def clear_tags(self):
        """
            '[1663,1774]' => [1663,1774]
        """
        splitted_tags = self.tags.replace(']', "").replace('[', "").split(',')
        result = [int(x) for x in splitted_tags]
        return result

    def clear_img_url(self):
        def _crop_img_str(img_str):
            stop_index = img_str.index('?')
            return img_str[:stop_index]

        if not self.img_url:
            return f'https://steamcdn-a.akamaihd.net/steam/apps/{self.id}/capsule_231x87.jpg'

        img_urls = self.img_url[0].attrib['srcset'].split(',')
        # micro_small_img = _crop_img_str(img_urls[0])
        small_img = _crop_img_str(img_urls[1])
        return small_img

    def clear_release_date(self):
        return self.release_date[0].text

    def clear_id(self):
        return int(self.id)

    def clear_user_review(self):
        if not self.user_review:
            return ''
        user_review_raw = self.user_review[0].attrib['data-tooltip-html']
        result = user_review_raw.split('<')[0]
        return result

    @staticmethod
    async def get_game(game):
        game_name_xpath = 'div[@class="responsive_search_name_combined"]/div[@class="col search_name ellipsis"]/span'
        img_url_xpath = 'div[@class="col search_capsule"]/img'
        release_date_xpath = 'div[@class="responsive_search_name_combined"]/div[@class="col search_released responsive_secondrow"]'
        user_review_xpath = 'div[@class="responsive_search_name_combined"]/div[@class="col search_reviewscore responsive_secondrow"]/span'

        raw_data = dict(
            id=game.attrib['data-ds-appid'],
            name=game.xpath(game_name_xpath)[0].text,
            tags=game.attrib['data-ds-tagids'],
            img_url=game.xpath(img_url_xpath),
            release_date=game.xpath(release_date_xpath),
            user_review=game.xpath(user_review_xpath),
        )

        return Game(**raw_data).__dict__

    @classmethod
    async def make_game_list(cls, text_response):
        tree = html.fromstring(text_response)
        game_item_xpath = 'a'
        game_list = tree.xpath(game_item_xpath)

        task_list = list()
        for game in game_list:
            task = asyncio.create_task(cls.get_game(game))
            task_list.append(task)

        tasks = await asyncio.gather(*task_list)
        return tasks

    def __post_init__(self):
        self.id = self.clear_id()
        self.tags = self.clear_tags()
        self.img_url = self.clear_img_url()
        self.release_date = self.clear_release_date()
        self.user_review = self.clear_user_review()
