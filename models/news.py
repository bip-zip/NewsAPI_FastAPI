from tortoise import Model, fields
from pydantic import BaseModel
from datetime import datetime

class Category(Model):
    category = fields.CharField(max_length=20, pk=True)

class News(Model):
    id = fields.IntField(pk=True, index=True)
    title = fields.CharField(max_length=200, null=False, index=True)
    thumbnail = fields.CharField(max_length=500, null=False)
    category = fields.ForeignKeyField('models.Category', related_name='category')
    is_verified = fields.BooleanField(default=False)
    is_updated = fields.BooleanField(default=False)
    created_date = fields.DatetimeField(default = datetime.now())
    updated_date = fields.DatetimeField(default = datetime.now())
    views = fields.IntField(default=0)
    reporter = fields.ForeignKeyField('models.User', related_name='reporter')

