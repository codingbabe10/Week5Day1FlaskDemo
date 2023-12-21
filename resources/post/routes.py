from flask import request
from uuid import uuid4 

from db import posts, users
from db import posts, users



@bp.get('/post')
def get_posts():
    return {'posts': list(posts.values())}


@app.get('/post/<post_id>')
def get_post(post_id):
   try:
      return{'post': posts[post_id]}, 200
   except KeyError:
    return {'message': "Invalid Post"}, 400

@app.get('/post')
def create_post():
   post_data = request.get_json()
   user_id = post_data['user_id']
   if user_id in users:
      posts[uuid4()] = post_data
      return { 'message': "post created"}, 201
   return {'message': "Invalid User"}, 401

@app.put('/pos/ <post_id>')
def update_post(post_id):
   try:
      post=posts[post_id]
      post_data = request.get_json()
      if post_data['user_id'] == post['user_id']:
         post['body'] = post_data['body']
         return {'message': 'Post Updated'}, 202
      return {'message': "unauthorized"}, 401
   except:
      return {'message': "Invalid Post ID "}, 400

@app.delete('/post/<post_id>')
def delete_post(post_id):
   try:
      del posts[post_id]
      return {"message": "Invalid Post"}, 202
   except:
    return {'message' : "invlaid post"}, 400

