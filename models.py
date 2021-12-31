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
    address = StringField(max_length=255)
    finance = FloatField(default=0, min_value=0)
    number_of_transactions = IntField(default=0)
    date_of_last_transaction = DateField()

# user = User(username='mohamad', password='1234567').save()
# account_mmd = Account(user=user, address='adres', finance=0).save()
