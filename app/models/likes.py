from . import db


class LikeTable(db.Model):
    __tablename__ = "liketable"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    like_books = db.Column(db.String(120), unique=False, nullable=True)
    like_movies = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return "<id %r>" % self.id
