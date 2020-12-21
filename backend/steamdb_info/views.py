from aiohttp import web
from aiohttp_cache import cache

from steamdb_info.services.utils import get_tag_request, get_tag_request_kwargs, make_tag_info


class AllTags_View(web.View):

    @staticmethod
    @cache(expires=60 * 60 * 24)  # 24 часа в секундах
    async def get(request):
        text_response = await get_tag_request(**get_tag_request_kwargs())
        result = await make_tag_info(text_response)

        response = {
            "objects": result
        }

        return web.json_response(data=response, status=200)
