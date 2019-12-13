import asyncio
from collections import defaultdict
import sys

from aiohttp import web

from . import logger
from .chat import chat


def main(host: str, port: int):
    logger.info("Start server")
    loop = asyncio.get_event_loop()

    app = web.Application()
    app.add_routes([web.get("/ws/{room_id}", chat.web_socket_handler)])

    web.run_app(app, host=host, port=port)

    logger.info("server finish")
    return 0


if __name__ == "__main__":
    sys.exit(main("localhost", 8080))
