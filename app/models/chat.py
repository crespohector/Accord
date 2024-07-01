from .db import db

class Chat(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey("channels.id"), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    channel = db.relationship("Channel", back_populates="chats")
    user = db.relationship("User", back_populates="user_chats")

    def to_dict(self):
        return {
        "id": self.id,
        "content": self.content,
        "channel_id": self.channel_id,
        "owner_id": self.owner_id,
        "created_on": self.created_on.strftime("%Y-%m-%d %H:%M:%S"),
        "user": self.user.to_dict()
        }
