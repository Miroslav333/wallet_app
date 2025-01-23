from pony.orm import *
import uuid

db = Database()


random_uuid_generate = [str(uuid.uuid4()) for _ in range(2)]


class User(db.Entity):
    name = Required(str)
    surname = Required(str)
    wallets = Set('Wallet')


class Wallet(db.Entity):
    amount = Required(int)
    WALLET_UUID = Required(str)
    owner = Required(User)


def get_user(user_id):
    with db_session:
        return User.get(id=user_id)


def get_wallet(ident):
    with db_session:
        return Wallet.get(WALLET_UUID=ident)


try:
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
    db.generate_mapping()
except Exception as Ex:
    print(Ex)


