# in order to create two users as friends we add

from . import db


class Friends(db.Model):
    __tablename__ = "friends"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),unique=False)
    friend_id = db.Column(db.Integer, unique=False, nullable=False)