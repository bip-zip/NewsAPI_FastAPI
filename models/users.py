from tortoise import Model, fields
from datetime import datetime


class User(Model):
    id = fields.IntField(pk=True,index=True)
    username = fields.CharField(max_length=55, null=False, unique=True)
    email = fields.CharField(max_length=200, null=False, unique = True)
    password = fields.CharField(max_length=200, null=False)
    is_verified = fields.BooleanField(default=False)
    joined_date = fields.DatetimeField(default = datetime.now())
    

class Reporter(Model):
    user = fields.ForeignKeyField('models.User',related_name='reporter')
    education = fields.CharField(max_length=100, null=False, default = 'Unspecified')
    certificate = fields.CharField(max_length=200, null=False, unique = 'certificate.jpg')


