from flask import Blueprint, session, request
from flask_login import current_user
from app.models import db, User, Server

user_server_routes = Blueprint("userserver", __name__)

@user_server_routes.route("/", methods=["GET"])
def getServersByUser():
    '''
    GET all servers from a specific user that the user owns and is a member of
    '''
    id = current_user.get_id()
    if id:
        user = User.query.get(id)
        user_servers = user.servers
        servers = [userserver.to_dict() for userserver in user_servers]
        return {"user_server": servers}
    else:
        return {"error": "user does not exist"}, 400


@user_server_routes.route("/server/<id>", methods=["GET"])
def getUsersByServer(id):
    '''
    GET all users in a specific server
    '''
    server = Server.query.get(id)
    servers_users = server.users
    return {"user_server": [serveruser.to_dict() for serveruser in servers_users]}

@user_server_routes.route("/server/<id>", methods=["POST"])
def addMemberToServer(id):
    '''
    POST add user member into the server
    '''
    user_id = current_user.get_id()
    if user_id:
        user = User.query.get(user_id)
        server = Server.query.get(id)
        user.servers.append(server)
        db.session.commit()
        return server.to_dict()
    else:
        return {"error": "user does not exist"}, 400

@user_server_routes.route("/server/<id>", methods=["DELETE"])
def removeMemberFromServer(id):
    '''
    DELETE remove user member from the server
    '''
    user_id = current_user.get_id()
    if user_id:
        user = User.query.get(user_id)
        server = Server.query.get(id)
        user.servers.remove(server)
        db.session.commit()
        return server.to_dict()
    else:
        return {"error": "user does not exist"}, 400
