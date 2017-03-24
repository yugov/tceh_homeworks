from db import db
from datetime import date
from models.user import User


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date, default=date.today)
    content = db.Column(db.String(400), unique=True, nullable=False)
    user = db.relationship(User, foreign_keys=[user_id])
    visible = db.Column(db.Boolean, nullable=False, default=True)

    def __str__(self):
        return '<Post %r>' % self.author
