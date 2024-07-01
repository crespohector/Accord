from flask_socketio import SocketIO, emit, join_room, leave_room, send
import os
from .models import User, Chat, Channel, db

if os.environ.get('FLASK_ENV') == 'production':
    REACT_APP_BASE_URL = os.getenv('REACT_APP_BASE_URL')
    origins = [REACT_APP_BASE_URL]
else:
    origins = "*"

# initialize your socket instance
socketio = SocketIO(cors_allowed_origins=origins)

# handle chat messages
@socketio.on("chat")
def handle_chat(data):
    chat = Chat(
        content = data["chat"],
        channel_id = data['channel_id'],
        owner_id = data["user"]["id"]
    )
    db.session.add(chat)
    db.session.commit()
    payload = {
        "chat": chat.to_dict(),
        "payload": data
    }
    emit("chat", payload, broadcast=True)

# delete chat messages
@socketio.on("delete-chat")
def delete_chat(data):
    # query for the chat instance in the db
    chat = Chat.query.get(data["id"])
    # apply deletion of the chat instance onto the SQL Alchemy session object
    # return the id of the deleted chat instance
    db.session.delete(chat)
    db.session.commit()
    payload = {
        "chat_id": chat.id,
        "channel_id": chat.channel_id
    }
    emit("delete-chat", payload, broadcast=True)

# @socketio.on('connect')
# def test_connect():
#     print('CONNECTED-----')

#handle chat messages to specific rooms
# @socketio.on('chat_to_channel')
# def chat_to_channel(data):
#     message = Chat(content=data['content'], channel_id=data['channel_id'], created_at=datetime.datetime.utcnow())

#     db.session.add(message)
#     db.session.commit()

#     send(message.to_dict(), to=f'channel_{data["channel_id"]}')
