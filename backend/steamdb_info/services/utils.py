import asyncio
from dataclasses import dataclass

import aiohttp
from lxml import html
from lxml.html import HtmlElement

from utils import get_only_int_from_str


def get_tag_request_kwargs():
    url = 'https://steamdb.info/tags/'
    headers = {
        'authority': 'steamdb.info',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
    }

    return {
        'url': url,
        'headers': headers,
    }


@dataclass
class GameTag:
    tag_products_count: HtmlElement
    tag_name: HtmlElement
    tag_steam_id: HtmlElement

    def get_tag_products_count(self):
        product_count_raw_str = self.tag_products_count[0].text  # '48984 products'
        return get_only_int_from_str(product_count_raw_str)

    def get_tag_name(self):
        return self.tag_name[0].text

    def get_tag_id(self):
        product_count_raw_str = self.tag_steam_id[0].attrib['href']  # '/tag/492/'
        return get_only_int_from_str(product_count_raw_str)

    def __post_init__(self):
        self.tag_products_count = self.get_tag_products_count()
        self.tag_name = self.get_tag_name()
        self.tag_steam_id = self.get_tag_id()


async def get_tag_info(tag_element: HtmlElement):
    tag_products_count = tag_element.xpath('span')
    tag_name = tag_element.xpath('a')
    tag_id = tag_element.xpath('a')
    result = dict(
        tag_products_count=tag_products_count,
        tag_name=tag_name,
        tag_steam_id=tag_id,
    )
    return GameTag(**result).__dict__


async def get_tag_request(url, headers, **kwargs):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.get(url, headers=headers, **kwargs) as resp:
            text_response = await resp.text()
            return text_response


async def make_tag_info(text_response):
    tree = html.fromstring(text_response)
    tags_list_xpath = '//*[@id="list"]/div[@class="row list"]/div[@class="span4"]'
    tags_list = tree.xpath(tags_list_xpath)

    task_list = list()

    for tag in tags_list:
        task = asyncio.create_task(get_tag_info(tag))
        task_list.append(task)

    tasks = await asyncio.gather(*task_list)
    return tasks
