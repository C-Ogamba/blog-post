from turtle import title
from app import db


class Post(db.Model):
    __table_name__= 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(65))
    content = db.Column(db.String(140))


    def __repr__(self):
        return f'Post {self.title}'