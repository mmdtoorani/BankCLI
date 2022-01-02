from mongoengine import (
    connect,
    DynamicDocument,
    StringField,
    ReferenceField,
    FloatField,
    IntField,
    DateField,

    CASCADE,
)

connect('BankCLIDB')


class User(DynamicDocument):
    first_name = StringField(max_length=255, null=True)
    last_name = StringField(max_length=255, null=True)
    age = IntField(min_length=18, null=True)
    username = StringField(unique=True, required=True, max_length=255)
    password = StringField(required=True, min_length=6)

    meta = {
        'allow_inheritance': True
    }

    def __repr__(self):
        return self.username


class Account(DynamicDocument):
    user = ReferenceField('User', reverse_delete_rule=CASCADE)
    finance = FloatField(min_value=0.0, default=10.0)
    number_of_transactions = IntField(default=0)
    date_of_last_transaction = DateField()
