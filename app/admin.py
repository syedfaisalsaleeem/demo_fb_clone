from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from . import *

def admin_view(create_app,db):
    admin = Admin(create_app, name='facebook_clone', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))