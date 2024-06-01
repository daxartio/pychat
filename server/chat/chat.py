import json
import logging
import uuid
from collections import defaultdict
from datetime import datetime

from aiohttp import WSMsgType, web

logger = logging.getLogger(__name__)


async def _broadcast(request, room_id, message):
    """Send messages to all in this room"""
    for peer in request.app["wslist"][room_id].values():
        await peer.send_str(_prepare(message.data))


def _prepare(message_data):
    try:
        data = json.loads(message_data)
        data["created_at"] = datetime.now().isoformat()
        message_data = json.dumps(data)
    finally:
        return message_data


async def web_socket_handler(request):
    app = request.app
    room_id = request.match_info.get("room_id", "unknown_room")

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    user_id = uuid.uuid4()

    if "wslist" not in app:
        app["wslist"] = defaultdict(dict)

    app["wslist"][room_id][user_id] = ws
    logger.info("New connectection %s %s", room_id, user_id)

    async for message in ws:
        if message.type == WSMsgType.TEXT:
            await _broadcast(request, room_id, message)
        elif message.type == WSMsgType.CLOSE:
            break

    app["wslist"][room_id].pop(user_id, None)
    logger.info("Close connectection %s %s", room_id, user_id)

    return ws
