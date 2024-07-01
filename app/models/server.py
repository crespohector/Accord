from .db import db, SCHEMA, environment, add_prefix_for_prod
from .user_server import user_server

import base64

class Server(db.Model):
    __tablename__ = 'servers'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    server_name = db.Column(db.String(15), nullable=False)
    img_url = db.Column(db.LargeBinary, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    channels = db.relationship("Channel", cascade="all, delete", back_populates="server")

    users = db.relationship(
        "User",
        secondary=user_server,
        back_populates="servers"
    )

    def to_dict(self):

        return {
        "id": self.id,
        "name": self.server_name,
        "created_on": self.created_on,
        "owner_id": self.owner_id,
        "img_url": base64.b64encode(self.img_url).decode('utf-8')
        }
