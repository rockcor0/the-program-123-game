from firebase import firebase

firebase = firebase.FirebaseApplication('https://the-program-123-game.firebaseio.com/', None)
data = {
  'username':'rockcor',
  'name':'Ricardo Delgado',
  'email':'ridel007@gmail.com'
}
result = firebase.post('/users-test', data)
print(result)