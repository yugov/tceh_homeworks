# Реализовать на Flask
# 1. По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']
# 2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму
# 3. По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'
# 4. По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля.
# Необходимо валидировать email, что обязательно присутствует, валидировать пароли,
# что они минимум 6 символов в длину и совпадают. Возрващать пользователю json вида:
# "status" - 0 или 1 (если ошибка валидации), "errors" - список ошибок, если они есть, или пустой список.
# 5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files.
# Файлы можно туда положить любые текстовые. А если такого нет - 404.

import os
from flask import Flask, jsonify, request, abort
from flask_wtf import FlaskForm
from wtforms import validators, PasswordField, StringField
import locale

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='my_secret_key',
    WTF_CSRF_ENABLED=False,
)


class UserForm(FlaskForm):
    email = StringField('email', validators=[validators.Email(message='invalid e-mail'), ])
    password = PasswordField('password', validators=[validators.Length(min=6),
                                                     validators.EqualTo('password_confirm',
                                                                        message='Password not match'), ])
    password_confirm = PasswordField('Confirm password')


@app.route('/locales')
def get_locales():
    locales = ['ru', 'en', 'it']
    locales_alias = [{loc: locale.locale_alias[loc] for loc in locales}]
    return jsonify(locales_alias)


@app.route('/sum/<int:first>/<int:second>')
def my_sum(first, second):
    return str(first + second)


@app.route('/greet/<username>')
def greet_user(username):
    return 'Hello, {}'.format(username)


@app.route('/from/user', methods=['POST'])
def from_user():
    form = UserForm(request.form)
    if form.validate():
        return jsonify({'status': 0})
    else:
        return jsonify({'status': 1, 'errors': [''.join(err) for err in form.errors.values()]})


@app.route('/serve/<path:filename>')
def path_file(filename):
    if os.path.exists(os.path.join('./files', filename)):
        with open(os.path.join('./files', filename), 'r') as f:
            return f.read()
    else:
        return abort(404)


if __name__ == '__main__':
    app.run()
