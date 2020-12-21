import pathlib
import re

import asyncio
from aiohttp import web
from aiohttp_apispec import validation_middleware, setup_aiohttp_apispec
from aiohttp_cache import setup_cache
from aiohttp_middlewares import cors_middleware

from middlewares import log_middleware
from routes import routes

PROJ_ROOT = pathlib.Path(__file__).parent.parent


async def init_app(build='development') -> web.Application:
    """
    """
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    app = web.Application()
    setup_cache(app)

    middlewares = [
        validation_middleware,
        log_middleware,
        cors_middleware(
            allow_all=True,
            urls=[re.compile(r"^\/api")],
            allow_credentials=True
        )
    ]

    app.middlewares.extend(middlewares)
    for route in routes:
        if len(route) > 2:
            app.router.add_route(*route)
        else:
            app.router.add_view(*route)


    # --- Swagger setup
    setup_aiohttp_apispec(
        app=app,
        title="Game Choicer Doc",
        version='v1',
        url="/api/v1/docs/swagger.json",
        swagger_path="/api/",
    )
    return app
