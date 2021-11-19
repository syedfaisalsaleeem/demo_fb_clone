from flask import Flask


create_app = Flask(__name__)
create_app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:faisal@localhost:5432/test"
