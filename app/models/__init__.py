from flask_sqlalchemy import SQLAlchemy

from ..app import create_app
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

# from sql_alchemy.main import *

# # if __package__ is None or __package__ == "":
# #     # uses current directory visibility
# #     from main import create_app
# # else:
# #     # uses current package visibility
# #     from ..main import create_app

db = SQLAlchemy(create_app)
# db = "faisal"
