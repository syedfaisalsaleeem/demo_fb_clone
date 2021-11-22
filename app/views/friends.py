from sqlalchemy.sql.expression import and_
from ..models.friend_model import Friends
from ..models import db
from .users import Users

class Friends_View():
    def __init__(self) -> None:
        pass
    
    def unfriend(self,user_id,friend_id):
        if self.check_already_friends(user_id,friend_id):
            Friends.query.filter(and_(Friends.user_id == user_id, Friends.friend_id == friend_id)).delete()
            Friends.query.filter(and_(Friends.user_id == friend_id, Friends.friend_id == user_id)).delete()
            db.session.commit()
            print("Unfriended")
        else:
            print("They are not friends with each other")

    def get_friends(self,user_id):
        import pprint
        friends = Friends.query.filter(Friends.user_id == user_id).all()
        print(friends)
        pprint.pprint(vars(friends[0]))

    def check_already_friends(self,user_id,friend_id):
        friends_list = Friends.query.filter(and_(Friends.user_id == user_id, Friends.friend_id == friend_id)).all()
        if len(friends_list) > 1:
            return False
        else:
            return True

    def insert_friends(self, user_id,friend_id):
        if self.check_already_friends(user_id,friend_id):
            main_user = Users().get_specific_user(user_id)
            main_user = main_user[0]
            friend_object = Friends(user_id=main_user,friend_id=friend_id)
            main_user.friend.append(friend_object)
            db.session.add(main_user)
            main_user = Users.get_specific_user(friend_id)
            main_user = main_user[0]
            friend_object = Friends(user_id=main_user,friend_id=user_id)
            main_user.friend.append(friend_object)
            db.session.add(main_user)
            db.session.commit()
            print("friend added")
        else:
            print("already friends")

    def update_friends():
        pass