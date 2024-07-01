from .db import db, SCHEMA, environment

class Category(db.Model):
    __tablename__ = 'categories'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    channels = db.relationship("Channel", back_populates="category")

    def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
       }
