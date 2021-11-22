from . import db


class User_Info(db.Model):
    __tablename__ = "user_info"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    address = db.Column(db.String(80), unique=False, nullable=False)
    postalcode = db.Column(db.String(120), unique=False, nullable=False)
    about = db.Column(db.String(120), unique=False, nullable=False)

    # def __repr__(self):
    #     return "<User Info %r>" % self.user_info
