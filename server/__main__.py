import logging
import sys

from aiohttp import web

from .chat import chat

logger = logging.getLogger(__name__)


async def root_handler(_request):
    return web.FileResponse("./web/build/index.html")


def main(host: str, port: int):
    logging.basicConfig(level=logging.INFO)

    logger.info("Start server")

    app = web.Application()
    app.add_routes([web.get("/ws/{room_id}", chat.web_socket_handler)])
    app.router.add_route("*", "/", root_handler)
    app.add_routes([web.static("/", "./web/build")])

    web.run_app(app, host=host, port=port)

    logger.info("server finish")
    return 0


if __name__ == "__main__":
    sys.exit(main("0.0.0.0", 8080))
