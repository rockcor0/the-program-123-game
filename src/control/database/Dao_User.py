from firebase import firebase

from src.control import DbConection

firebase = DbConection.firebase
user_uri = DbConection.uri_player

# Create the player in the database
def create_player(name, email, age):
    data = {
        'name': name,
        'email': email,
        'age': age
    }

    return firebase.post(user_uri, data)

# Read de player from database
def read_player(player_id):
    # Update for read only a user
    result = firebase.get(user_uri, '')
    print(result)
    return result

def get_a_player():
    pass

# Update de player
def update_player(player_id, name, email, age):
    data = {
        'name': name,
        'email': email,
        'age': age
    }

    result = firebase.put(user_uri, player_id, data)
    print(result)
    return result

# Delete the player
def delete_player(player_id):
    result = firebase.delete(user_uri, player_id)
    print(result)
    return result


# create_player('Ricardo Delgado', 'ridel007@gmail.com', 37)
read_player(' ')
update_player('-MOJ_fJScoQsBBHFdYnW', 'Lilly', 'lipadugi', 32)
delete_player('-MOJeAneLr9EZsu-9awB')