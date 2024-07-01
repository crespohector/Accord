from flask import Blueprint, jsonify, session, request
from flask_login import current_user
from app.models import User, Chat, Channel, db
from app.forms import ChatForm

chat_routes = Blueprint("chat", __name__)

#Grabs all the chat messages from specific channel
@chat_routes.route("/<int:id>", methods=["GET"])
def chat_channel(id):
    chats = Chat.query.filter(Chat.channel_id == id).all()
    return {"chats": [chat.to_dict() for chat in chats]}

@chat_routes.route("/<int:id>", methods=['POST'])
def chat_post(id):
    form = ChatForm()
    user_id = current_user.id
    form['csrf_token'].data = request.cookies['csrf_token']
    form.data['channel_id'] = id

    if form.validate_on_submit():
        chat = Chat(
            content = form.data['content'],
            channel_id = id,
            owner_id = user_id
        )
        db.session.add(chat)
        db.session.commit()
        return chat.to_dict()

    return {"error": "unable to fulfill request"}, 400

@chat_routes.route("/<int:id>", methods=['DELETE'])
def delete_chat(id):
    """
    DELETE - delete the user's chat message
    """
    chat = Chat.query.get(id)
    db.session.delete(chat)
    db.session.commit()
    #query for a list of chat within a channel
    return {"id": chat.id}
