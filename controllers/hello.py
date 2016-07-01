from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from . import bp
from application import db
from models.model import User

@bp.route('/hello/', methods=['GET', 'POST'])
@bp.route('/hello/<name>', methods=['GET', 'POST'])
def hello(name=None):
    if request.method == 'GET':
        users = User.get_all()
        return render_template('hello.html', name=name, users=users)

    username = request.form.get('username')
    email = request.form.get('email')

    add(username, email)
    return redirect(url_for('.hello'))

def add(username, email):
    user = User(username=username, email=email)

    db.session.add(user)
    db.session.commit()


