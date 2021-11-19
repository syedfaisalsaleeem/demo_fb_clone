from .models import db
from models.user_model import User

py = User(
    username="Python",
    email="python@gmail.com",
)
# Post(title="Hello Python!", body="Python is pretty cool", category=py)
# p = Post(title="Snakes", body="Ssssssss")
# py.posts.append(p)
db.session.add(py)
db.session.commit()
