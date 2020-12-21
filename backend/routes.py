from aiohttp import web

from steam.routes import routes as steam_routes
from steamdb_info.routes import routes as steamdb_info_routes


class AvailableServerView(web.View):

    async def get(self) -> web:
        data = {
            'ok': 200
        }
        return web.json_response(data=data, status=200)


available_server_url = '/api/backend_status'

routes = [
    ('GET', available_server_url, AvailableServerView.get),
    *steamdb_info_routes,
    *steam_routes,
]
