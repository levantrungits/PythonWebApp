__author="trunglv"

import uuid
from datetime import datetime
from Flask.API.models.blog import Blog
from Flask.API.common.database import Database

class User(object):
    def __init__(self, email, password, id=None):
        self.email = email
        self.password = password
        self.id = uuid.uuid4().hex if id is None else id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one('users', {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(self, id):
        data = Database.find_one("users", {"id": id})
        if data is not None:
            return cls(**data)

    def login_valid(self, email, password):
        # Check whether a user's email matches the password they sent us
        user = User.get_by_email(email)
        if user is not None:
            # Check the password
            return user.password == password
        return False

    @classmethod
    def register(self, email, password):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(email, password)
            new_user.save_to_mongo()
            return True

    @staticmethod
    def login(user_email):
        # Login_valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def get_blogs(self):
        return Blog.find_by_author_id(self.id)

    def new_blog(self, title, description):
        # author, title, description, author_id
        blog = Blog(author = self.email,
                    title = title,
                    description = description,
                    author_id = self.id)
        blog.save_to_mongo()

    @staticmethod
    def new_post(self, blog_id, title, content, date = datetime.utcnow()):
        # title, content, date=datetime.utcnow()
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title = title,
                        content = content,
                        date = date)

    def json(self):
        return {
            "email": self.email,
            "id": self.id,
            "password": self.password
        }

    def save_to_mongo(self):
        Database.insert("users", self.json())