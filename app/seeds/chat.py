from app.models import db, Chat, SCHEMA, environment
from faker import Faker
import random

faker = Faker()
# Adds a demo user, you can add other users here if you want
def seed_chat():

    for i in range(0, 100):
        another = Chat(content=faker.text(),
                    channel_id=random.randint(1, 37),
                    owner_id=random.randint(1, 16)
                    )
        db.session.add(another)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_chat():

    if environment == "production":
         db.session.execute(f"TRUNCATE table {SCHEMA}.chats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute('TRUNCATE table chats RESTART IDENTITY CASCADE;')
    db.session.commit()
