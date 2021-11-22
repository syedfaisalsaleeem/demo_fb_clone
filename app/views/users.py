# from ..models import db
from ..models.user_model import User
from sqlalchemy.sql.expression import and_
# from ..models.user_info_model import User_Info

class Users():
    def __init__(self):
        pass

    def get_all_user():

        all_users = User.query.all() # query for getting all users
        return all_users

    @staticmethod
    def get_specific_user(user_id):
        print(user_id)
        user = User.query.filter(and_(User.id == user_id)).all() # query for removing empty relationship and using and operation get_user_and_userinfo_by_join()
        return user