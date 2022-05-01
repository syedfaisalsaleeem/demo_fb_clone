from ..models.likes import LikeTable
from sqlalchemy.sql.expression import and_
from ..models import db

def adduserlikes():
    py = LikeTable(
        like_books="the prisoner of zenda",
        like_movies="",
    )
    db.session.add(py)
    db.session.commit()
    print("record added")