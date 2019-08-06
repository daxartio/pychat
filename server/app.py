import asyncio
from collections import defaultdict
import sys
from . import logger
from .chat import chat
from .chat import aiohttpapi


def main(host: str, port: int):
    logger.info('Start server')
    loop = asyncio.get_event_loop()

    services = [
        aiohttpapi.AIOHttpApi(
            loop,
            host,
            port,
            routes=[('GET', '/ws/{room_id}', chat.web_socket_handler)],
            data_to_store_in_app={'wslist': defaultdict(dict)}
        )
    ]

    for service in services:
        loop.run_until_complete(service.start())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        try:
            loop.run_until_complete(loop.shutdown_asyncgens())
            for service in services:
                loop.run_until_complete(service.stop())
        finally:
            loop.close()

    logger.info('server завершил работу')
    return 0


if __name__ == '__main__':
    sys.exit(main('0.0.0.0', 8080))
