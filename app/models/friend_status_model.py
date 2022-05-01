from . import db


class FriendStatus(db.Model):
    __tablename__ = "friendstatus"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    status_id = db.Column(
        db.Integer, db.ForeignKey("friends.id"), nullable=False, unique=False
    )
    status = db.Column(db.String(120), unique=False, nullable=False)
