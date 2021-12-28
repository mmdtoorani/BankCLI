from mongoengine import (
    connect,
    DynamicDocument,
    StringField,
    ReferenceField,
    FloatField,
    IntField,

    CASCADE,
)

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
    finance = FloatField(default=0, min_value=0)

# user = User(username='mohamad', password='1234567').save()
# account_mmd = Account(user=user, address='adres', finance=0).save()
