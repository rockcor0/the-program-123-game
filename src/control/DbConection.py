from firebase import firebase

firebase = firebase.FirebaseApplication('https://the-program-123-game.firebaseio.com/', None)
uri_player = '/users-test'

data = {'123': {
  'username':'rockcor',
  'name':'Ricardo Delgado',
  'email':'ridel007@gmail.com'
}}
result = firebase.post('/users-test', data)
print(result)