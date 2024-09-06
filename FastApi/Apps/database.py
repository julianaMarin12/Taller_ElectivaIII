from dotenv import load_dotenv
from peewee import *
import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user= os.getenv("MYSQL_USER"),
    passwd = os.getenv("MYSQL_PASSWORD"),
    host = os.getenv("MYSQL_HOST")
)

class UserModel(Model):
    id_user = AutoField(primary_key=True)
    username = CharField(max_length = 50)
    email = CharField(max_length = 50)
    pasword = CharField(max_length = 50)

    class meta:
        database = database
        tabla_name = "users"

