from datetime import datetime

# from sqlalchemy.orm import relationship
from . import db

# association_table = db.Table(
#     "association",
#     db.Model.metadata,
#     db.Column("id", db.Integer, db.ForeignKey('user.id')),
#     db.Column("right_id", db.Integer, db.ForeignKey("right.id")),
# )


# class UserLikeTable:
#     __tablename__ = "userliketable"
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     like_id = db.Column(db.Integer, db.ForeignKey("liketable.id"))

#     # ... any other fields

#     user = db.relationship(
#         "User",
#         foreign_keys="User.user_id",
#         uselist=True,
#     )
#     like = db.relationship(
#         "liketable",
#         foreign_keys="liketable.id",
#         uselist=True,
#     )


userliketable = db.Table(
    "userliketable",
    db.Column("User", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("LikeTable", db.Integer, db.ForeignKey("liketable.id"), primary_key=True),
)
