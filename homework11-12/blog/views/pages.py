# -*- coding: utf-8 -*-

from flask import Blueprint, request, flash, render_template
from db import db

views = Blueprint('views', __name__, url_prefix='/')


@views.route('users', methods=['GET', 'POST'])
def users():
    from models.user import User
    from forms.userform import UserForm

    if request.method == 'POST':
        form = UserForm(request.form)
        if form.validate():
            user = User(**form.data)
            db.session.add(user)
            db.session.commit()
            flash('valid')
        else:
            flash('invalid')
    data = User.query.all()
    return render_template('users.html', users=data)


@views.route('posts', methods=['GET', 'POST'])
def posts():
    from models.post import Post
    from forms.postform import PostForm

    if request.method == 'POST':
        form = PostForm(request.form)
        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()
            flash('valid')
        else:
            flash('invalid')
    data = Post.query.all()
    return render_template('posts.html', posts=data)
