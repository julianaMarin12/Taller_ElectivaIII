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

class PhoneModel(Model):
     id_phone = AutoField(primary_key=True)
     name = CharField(max_length = 50)
     brand = CharField(max_length = 50)
     price = CharField(max_length = 50)
     
     class meta:
        database = database
        tabla_name = "phone"

class HouseModel(Model):
     id_house = AutoField(primary_key=True)
     name = CharField(max_length = 50)
     price = CharField(max_length = 50)
     classification = CharField(max_length = 50)
     room = CharField(max_length = 50)
     
     class meta:
        database = database
        tabla_name = "house"

class FoodModel(Model):
     id_food = AutoField(primary_key=True)
     name = CharField(max_length = 50)
     price = CharField(max_length = 50)
     detail = CharField(max_length = 50)
     
     class meta:
        database = database
        tabla_name = "food"

class AutomobileModel(Model):
     id_automobile = AutoField(primary_key=True)
     name = CharField(max_length = 50)
     price = CharField(max_length = 50)
     classification = CharField(max_length = 50)
     weight = CharField(max_length = 50)
     
     class meta:
        database = database
        tabla_name = "food"

class AnimalModel(Model):
     id_animal = AutoField(primary_key=True)
     name = CharField(max_length = 50)
     gender = CharField(max_length = 50)
     classification = CharField(max_length = 50)
     age = CharField(max_length = 50)
     owner = CharField(max_length = 50)
     
     class meta:
        database = database
        tabla_name = "food"
