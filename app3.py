from models.post import Post
from database import Database

__author__ = "trunglv"

Database.initialize()

# post = Post(blog_id="blog_id_123", title="Another great post",
#             content="This is some sample content", author="trunglv")
# post.save_to_mongo()

# postById = Post.from_mongo('024952762eb348359b2bb8938cf3f069')
# print(postById)

# postsByBlogId = Post.from_blog('blog_id_123')
# for blog in postsByBlogId:
#     print(blog)

blog = Blog(author="trunglv", title="Sample title", description="Sample description")

blog.new_post()

blog.save_to_mongo()

Blog.from_mongo()