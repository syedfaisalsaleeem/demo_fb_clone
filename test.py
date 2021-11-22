from app.demo_query import *
from app.views.friends import *
if __name__ == "__main__":
    # add_user()
    # add_user_info()
    # add_user_info_without_relationship()
    # get_user()
    # get_userinfo()
    # get_userinfo_whichrelation_user()
    x = Friends_View()
    x.get_friends(1)