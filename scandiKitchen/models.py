from scandiKitchen import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

#check if user is authenticated
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#allow user login functions
class User(db.Model,UserMixin):
    #setting up user model
    __tablename__ = 'users'
    #creating unique identification for users
    id = db.Column(db.Integer,primary_key=True)
    #link to a file that user uploads / setting up a default profile image if nothing is submitted
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    #setup email and making sure it is not repeated
    email = db.Column(db.String(64),unique=True,index=True)
    #setup username to be unique
    username = db.Column(db.String(64),unique=True,index=True)
    #setup password for the user using password hashing#
    password_hash = db.Column(db.String(128))

    #connecting recipe with the person who uploaded
    posts = db.relationship('BlogPost',backref='author',lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}"



    

class Recipe(dn.model):
    pass