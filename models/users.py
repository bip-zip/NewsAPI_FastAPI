from tortoise import Model, fields
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator

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

user_pydantic = pydantic_model_creator(User, name='User', exclude=('is_verified'))
user_pydanticIn = pydantic_model_creator(User, name='UserIn',exclude_readonly=True)
user_pydanticOut = pydantic_model_creator(User, name='UserOut',exclude=('password',))
