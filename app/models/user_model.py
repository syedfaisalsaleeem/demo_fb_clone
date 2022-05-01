from . import db
from .user_likes import userliketable

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    info = db.relationship(
        "User_Info",
        backref=db.backref("user", lazy="joined"),
        foreign_keys="User_Info.user_id",
        uselist=False,
    )
    # friend = db.relationship("Friends",backref=db.backref('user', lazy='joined'), foreign_keys="Friends.user_id", uselist=True)
    user_liking = db.relationship(
        "LikeTable",
        secondary=userliketable,
        lazy='subquery',
        backref=db.backref("user", lazy="joined")
    )
    def __repr__(self):
        return "<User %r>" % self.username
