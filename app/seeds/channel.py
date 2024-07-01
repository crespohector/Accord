from app.models import db, Channel
import os

# Adds a demo user, you can add other users here if you want
def seed_channel():

    for num in range(1,9):
        channel = Channel(title="#intros", category_id=1, server_id=num)
        channel_2 = Channel(title="#chat", category_id=1, server_id=num)
        channel_3 = Channel(title="#announcements", category_id=1, server_id=num)
        channel_4 = Channel(title="#random", category_id=1, server_id=num)
        db.session.add(channel)
        db.session.add(channel_2)
        db.session.add(channel_3)
        db.session.add(channel_4)


    food_channel = Channel(title="#recipes!", category_id=1, server_id=1)
    league_channel = Channel(title="#tournaments", category_id=1, server_id=8)
    sports_channel = Channel(title="#events", category_id=1, server_id=3)
    anime_channel = Channel(title="#memes", category_id=1, server_id=4)
    game_channel = Channel(title="#gaming", category_id=1, server_id=5)

    db.session.add(food_channel)
    db.session.add(league_channel)
    db.session.add(sports_channel)
    db.session.add(anime_channel)
    db.session.add(game_channel)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_channel():
    db.session.execute('TRUNCATE channels RESTART IDENTITY CASCADE;')
    db.session.commit()
