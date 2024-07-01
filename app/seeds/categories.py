from app.models import db, Category, SCHEMA, environment

# Adds a demo user, you can add other users here if you want
def seed_categories():

    cat = Category(title="General")
    db.session.add(cat)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_categories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute('TRUNCATE table categories RESTART IDENTITY CASCADE;')
    db.session.commit()
