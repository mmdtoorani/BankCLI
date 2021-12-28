from mongoengine import *

connect('BankCLIDB')


class User(DynamicDocument):
    username = StringField(required=True, max_length=255)
    password = StringField(required=True, min_length=6)

    meta = {
        'allow_inheritance': True
    }


class Account(DynamicDocument):
    user = ReferenceField('User', reverse_delete_rule=CASCADE)
    address = StringField(max_length=255)
    finance = FloatField(min_value=0)


class AllUsers(DynamicDocument):
    users = ListField(StringField(max_length=255))

