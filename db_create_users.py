from app import db
from models import User

# Insert data
db.session.add(User("chris", "example@example.com", "I'll-never-tell"))
db.session.add(User("admin", "ad@min.com", "admin"))

# Commit changes
db.session.commit()