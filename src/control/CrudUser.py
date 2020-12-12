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
    # Update for read only a user
    result = firebase.get(user_uri, '')
    print(result)
    return result


def update_player(player_id, name, email, age):
    data = {
        'name': name,
        'email': email,
        'age': age
    }
    result = firebase.put(user_uri+'/'+player_id, 'name', name)
    print(result)
    return result


def delete_player(player_id):
    pass


# create_player('Ricardo Delgado', 'ridel007@gmail.com', 37)
read_player(' ')
update_player('-MOJ_fJScoQsBBHFdYnW', 'Lilly', 'lipadugi', 32)
