import uuid
from datetime import datetime
from models.post import Post
from Flask.API.common.database import Database

__author__="trunglv"

class Blog(object):
    def __init__(self, author, title, description, author_id, id=None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id
    
    def new_post(self, title, content, date = datetime.utcnow()):
        post = Post(blog_id = self.id,
                    title = title,
                    content = content,
                    author = self.author,
                    date = datetime.strptime(date, "%d%m%Y"))
        post.save_to_mongo()                    
    
    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            'author': self.author,
            'author_id': self.author_id,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'id': id})
        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls, author_id):
        blogs = Database.find(collection = 'blogs', query = {'author_id': author_id})
        return [cls(**blog) for blog in blogs]