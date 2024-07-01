from app.models import db, User, Server

# Adds a demo user, you can add other users here if you want
def seed_useserv():

    demo_user = User.query.get(1)
    server1 = Server.query.get(1)

    demo_user.servers.append(server1)

    db.session.add(demo_user)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_useserv():
    db.session.execute('TRUNCATE servers RESTART IDENTITY CASCADE;')
    db.session.commit()
