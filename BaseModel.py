# coding=utf-8

from peewee import *
from Config import Config

class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    #id = UUIDField(primary_key=True)

    class Meta:
        database = Config.PSQL_DB