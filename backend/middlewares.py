# -*- coding: utf-8 -*-
import asyncio
import json

from aiohttp import web
from loguru import logger


async def logger_info(msg, ):
    logger.info(msg)


@web.middleware
async def log_middleware(request, handler):
    '''
    '''
    response = await handler(request)

    msg = f'{request._rel_url.path} : status {getattr(response, "status", "ERROR")} '
    other_msg = [
        lambda: msg,
        # lambda: json.dumps(
        #     response.body.decode("unicode-escape"),
        #     ensure_ascii=False,
        #     sort_keys=False,
        # ),
    ]
    for x in other_msg:
        asyncio.ensure_future(logger_info(x()))
    return response
