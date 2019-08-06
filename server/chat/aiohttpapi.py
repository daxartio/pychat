import asyncio
import logging
from typing import Dict, Optional

from aiohttp import web

MAX_HTTP_HEADER_SIZE = 65536
MAX_HTTP_BODY_SIZE = 500 * 1024 ** 2


class AIOHttpApi(object):
    def __init__(self, loop: asyncio.AbstractEventLoop,
                 host: str,
                 port: int,
                 routes=None,
                 data_to_store_in_app: Optional[Dict] = None,
                 logger: Optional[logging.Logger] = None,
                 middlewares=None):
        if logger is not None:
            self._logger = logger.getChild(__name__)
        else:
            self._logger = logging.getLogger(__name__)
        self._access_log_format = '%a "%r" -> %s [%bb in %Tfs]'

        self._host = host
        self._port = port

        self._loop = loop
        self._server: Optional[asyncio.AbstractServer] = None

        self._middlewares = list(middlewares) if middlewares else []

        self._app = web.Application(
            middlewares=self._middlewares, client_max_size=MAX_HTTP_BODY_SIZE)

        self._app['logger'] = self._logger
        self._app['loop'] = self._loop

        if data_to_store_in_app:
            for key, value in data_to_store_in_app.items():
                self._app[key] = value

        if routes:
            for route in routes:
                self._app.router.add_route(*route)

        self._runner = web.AppRunner(
            self._app,
            access_log=self._logger,
            access_log_format=self._access_log_format,
            max_line_size=MAX_HTTP_HEADER_SIZE
        )

    async def start(self):
        await self._runner.setup()
        site = web.TCPSite(self._runner, self._host, self._port)
        await site.start()

        self._logger.info(
            "Запуск API сервера на http://{}:{}/".format(self._host, self._port))

    async def stop(self):
        await self._runner.cleanup()
