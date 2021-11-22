try:
    from .models import db
    from .models.user_model import User
    from .models.user_info_model import User_Info
except:
    from models import db
    from models.user_model import User
    from models.user_info_model import User_Info

from sqlalchemy import or_
from sqlalchemy.sql.expression import and_
def add_user():
    py = User(
        username="Python3",
        email="python3@gmail.com",
    )
    # Post(title="Hello Python!", body="Python is pretty cool", category=py)
    # p = Post(title="Snakes", body="Ssssssss")
    # py.posts.append(p)
    db.session.add(py)
    db.session.commit()
    print("record added")


def add_user_info():
    user_data = User(
        username="Python3",
        email="python3@gmail.com",
        
    )
    u_i = User_Info(address="karachi2", postalcode="751002",about="here is me2", user_id=user_data)
    user_data.info = u_i
    db.session.add(user_data)
    db.session.commit()
    print("record added")

def add_user_info_without_relationship():
    u_i = User_Info(address="karachi", postalcode="75100",about="here is me")
    db.session.add(u_i)
    db.session.commit()
    print("record added")

def get_user():
    v = User.query.filter(User.info != None).all() # query for removing empty relationship
    v = User.query.filter(and_(User.info != None, User.id == 2)).all() # query for removing empty relationship and using and operation get_user_and_userinfo_by_join()
    # v = db.session.query(User).filter(User.id == 2).all()
    for i in v:
        print(i.username)
        print(i.email)
        print(i.info.address)
    print(v)

def get_userinfo():
    import pprint
    v = User_Info.query.all()
    pprint.pprint(vars(v[2]))
    # v = db.session.query(User_Info).all()
    for i in v:
        print(i.user_id)
        print(i.address)
        print(i.postalcode)
        print(i.about)
    print(v)

def get_userinfo_whichrelation_user():
    '''
    In this function we are getting the data of parent table from child table using backref
    '''
    import pprint
    v = User_Info.query.filter(User_Info.user != None).all()
    # pprint.pprint(vars(v[2]))
    # v = db.session.query(User_Info).all()
    for i in v:
        print(i.user)
        print(i.user_id)
        print(i.address)
        print(i.postalcode)
        print(i.about)
    print(v)