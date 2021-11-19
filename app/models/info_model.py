from . import db


class Info(db.Model):
    __tablename__ = "info"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    address = db.Column(db.String(80), unique=False, nullable=False)
    postalcode = db.Column(db.String(120), unique=False, nullable=False)
    about = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return "<Info %r>" % self.info
