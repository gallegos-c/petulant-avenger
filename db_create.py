from project import db
#from models import BlogPost

# Create the database and the db tables
db.create_all()


# # Insert
# db.session.add(BlogPost("Good", "I\'m good."))
# db.session.add(BlogPost("Well", "I\'m well."))
# db.session.add(BlogPost("Flask", "learning Flask"))
# db.session.add(BlogPost("postgres", "We setup a local postgres instance."))

# Commit the changes
db.session.commit()