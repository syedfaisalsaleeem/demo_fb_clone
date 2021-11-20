try:
    from .models import db
    from .models.user_model import User
    from .models.user_info_model import User_Info
except:
    from models import db
    from models.user_model import User
    from models.user_info_model import User_Info


def add_user():
    py = User(
        username="Python",
        email="python@gmail.com",
    )
    # Post(title="Hello Python!", body="Python is pretty cool", category=py)
    # p = Post(title="Snakes", body="Ssssssss")
    # py.posts.append(p)
    db.session.add(py)
    db.session.commit()
    print("record added")


def add_user_info():
    user_data = User(
        username="Python1",
        email="python1@gmail.com",
    )
    u_i = User_Info(address="karachi", postalcode="75100", user_id=user_data)
    # user_data.info.append(u_i)
    db.session.add(u_i)
    # db.session.add(u_i)
    # db.session.commit()
    print("record added")
