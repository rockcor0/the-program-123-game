from firebase import firebase

from src.control import DbConection

firebase = DbConection.firebase
user_uri = '/users-test'


def create_player(name, email, age):
    data = {
        'name': name,
        'email': email,
        'age': age
    }

    return firebase.post(user_uri, data)

def read_player(player_id):
    pass

create_player('Test', 'Test', 20)