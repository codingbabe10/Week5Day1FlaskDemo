from datetime import datetime

from app import db

class PostModel(db.Model):

    __tablename__='posts'

    id = db.Column(db.Integer,primary_key =True)
    body=db.Column(db.string,nullibe=False)
    timestamp= db.Column(db.Strin, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.Foreignkey('users.id'),nullable=False)

    def __repr__(self):
        return f'<Post:{self.body}>'
    def commit(self):
        db.session.add(self)
        db.session.commit()