from flask import Blueprint, jsonify, session, request
from flask_login import current_user
from app.models import db, User, Server, Category, Channel
from app.forms import ServerForm

server_routes = Blueprint("server", __name__)

@server_routes.route("/", methods=["GET"])
def getServers():
    '''
    get all servers
    '''
    servers = Server.query.all()
    return {"servers": [server.to_dict() for server in servers]}


@server_routes.route('/', methods=["POST"])
def post_server():
    '''
    CREATE a server
    '''
    image = request.files['image'].read()
    name = request.form.get('name')

    user = User.query.get(current_user.id)

    server = Server(
        server_name = name,
        img_url = image,
        owner_id = current_user.id
    )

    # add user to the new server
    user.servers.append(server)
    db.session.add(user)
    db.session.add(server)
    db.session.commit()

    new_category = Category(title="General")
    db.session.add(new_category)
    db.session.commit()

    new_channel = Channel(title="room 1", category_id=new_category.id, server_id=server.id)
    db.session.add(new_channel)
    db.session.commit()

    return server.to_dict()

@server_routes.route('/<id>/', methods=["PUT"])
def update_server(id):
    '''
    UPDATE a server
    '''
    server = Server.query.get(id)
    # grab form data from request object
    if request.files.get("image"):
        # check if file exist
        image = request.files['image'].read()
        server.img_url = image

    name = request.form.get('name')
    server.server_name = name
    server.owner_id = current_user.id

    db.session.commit()
    return server.to_dict()

@server_routes.route('/<id>', methods=["DELETE"])
def delete_server(id):
    '''
    Delete a server
    '''
    server = Server.query.get(id)
    db.session.delete(server)
    db.session.commit()
    return server.to_dict()


@server_routes.route('/<id>', methods=["GET"])
def get_server(id):
    '''
    Getting current server
    '''
    server = Server.query.get(id)
    test = server.to_dict
    return {"server": server.to_dict()}
