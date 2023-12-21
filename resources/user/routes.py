

from app import app
from db import users
from flask import request
from uuid import uuid4


from . import bp
from db import posts, users

from schemas import UserSchema

@bp.route('/user/<user_id>')
class User (methodView):
   
   @bp response(200,Userschema)
   def get(self, user_id):
      try:
         print (users:, users[user_id])
      try:
         return users [user_id]
      except:
         return {'message' 'invalid user'}, 400
   
   def put(self, user_id):
      try:
      user=users[user_id]
      user_data = request.get_json()
      user |=user_data
      return {"message": f'{user["username"]} updated'}, 202
   except KeyError:
      return {'message': "Invalid User"}
   
   def delete(self):
      try:
       del users[user_id]
       return {'message': f'user deleted'}, 202
    except:
       return{'message': "Invalid username"}, 400

@bp.route('/user')
class UserList(MethodView)


@bp.route('/user', methods=['GET'])
def user():
    return {'users' : list(users.values())}

# @app.post('/user', methods=["GET", "POST"])
# def user2():
#     return



# @app.get('/user')
# def user():
#    return { 'users' : list(users.values())}, 200

@app.get('/user')
def user():
   return user




@bp.route ('/user', methods=["POST"])
@bp.arguments (userSchema)
def create_user(user_data):
    user_data= request.get_json()
    return { 'message' : f' {user_data["username"]} created'}, 201


@bp.put('/user/<user_id>')
def update_user(user_id):
  try:
     user=users[user_id]
     user_data = request.get_json()
     user |=user_data
     return {"message": f'{user["username"]} updated'}, 202
  except KeyError:
     return {'message': "Invalid User"}

  @bp.delete('/user')
  def delete_user ():
    user = users[user_id]
    user_data = request.get_json()
    username= user_data['username']
    for id, user in users.items():
        if user['username'] == username:
         return

@bp.delete('/user/<user_id>')
def delete_user (user_id):
    # user_data = request.get_json()
    # username= user_data['username']
    try:
       del users[user_id]
       return {'message': f'user deleted'}, 202
    except:
       return{'message': "Invalid username"}, 400
