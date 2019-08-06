import uuid
import json
from datetime import datetime

from aiohttp import web, WSMsgType


async def _broadcast(request, room_id, message):
    """ Send messages to all in this room """
    for peer in request.app['wslist'][room_id].values():
        await peer.send_str(_prepare(message.data))


def _prepare(message_data):
    try:
        data = json.loads(message_data)
        data['created_at'] = datetime.now().isoformat()
        message_data = json.dumps(data)
    finally:
        return message_data


async def web_socket_handler(request):
    app = request.app
    room_id = request.match_info.get('room_id', 'unknown_room')

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    user_id = uuid.uuid4()

    app['wslist'][room_id][user_id] = ws
    app.logger.info('New connectection {} {}'.format(room_id, user_id))

    async for message in ws:
        if message.type == WSMsgType.TEXT:
            await _broadcast(request, room_id, message)
        elif message.type == web.MsgType.close:
            break

    app['wslist'][room_id].pop(user_id, None)
    app.logger.info('Close connectection {} {}'.format(room_id, user_id))

    return ws
