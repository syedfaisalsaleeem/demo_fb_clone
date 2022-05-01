import os
from dotenv import load_dotenv


load_dotenv()

app_settings = os.environ.get("APP_SETTINGS")
host = os.environ.get("FLASK_HOST")
port = os.environ.get("FLASK_PORT")


from flask_migrate import Migrate
from app.app import create_app
from app.models import db
from app.admin import admin_view

migrate = Migrate(create_app, db)
admin_view(create_app,db)


if __name__ == "__main__":
    create_app.run(host=host, port=port, debug=True)
