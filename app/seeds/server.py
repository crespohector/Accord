from app.models import db, Server, User
import os
import random

def seed_serv():

    # make a query to get the first 6 users
    users = User.query.limit(6).all()

    seeds_dir = os.path.dirname(__file__)

    assets_dir = os.path.join(seeds_dir, "..", "..", "assets")

    images = os.listdir(assets_dir)

    # iterate through the images in the assets folder
    for image in images:
        file_path_to_image = os.path.join(assets_dir, image)
        file_name = os.path.splitext(image)[0]

        with open(file_path_to_image, 'rb') as f:
            img_data = f.read()
            rand_int = random.randint(0,4)
            server = Server(server_name=file_name,
                            img_url=img_data,
                            owner_id=rand_int + 1)
            # append server instance to the user's servers attribute
            users[rand_int].servers.append(server)
            db.session.add(server)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_serv():
    db.session.execute('TRUNCATE servers RESTART IDENTITY CASCADE;')
    db.session.commit()
