import json

from aiohttp import web

from steam.services.utils import Game, get_request_kwargs
from steamdb_info.services.utils import get_tag_request


class SearchByTag(web.View):

    @staticmethod
    async def get(request):
        request_kwargs = get_request_kwargs(request.query)
        resp = await get_tag_request(**request_kwargs)
        data = json.loads(resp)

        result = await Game.make_game_list(data['results_html'])

        response = {
            "objects": result
        }

        return web.json_response(status=200, data=response)
