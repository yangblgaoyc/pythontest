from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from . import bp
from application import db
from models.model import User
from flask import jsonify

@bp.route('/hello/', methods=['GET', 'POST'])
@bp.route('/hello/<name>', methods=['GET', 'POST'])
def hello(name=None):
    if request.method == 'GET':
        users = get_all()
        return render_template('hello.html', name=name, users=users)

    username = request.form.get('username')
    email = request.form.get('email')

    add(username, email)
    return redirect(url_for('.hello'))

@bp.route('/hello/<int:user_id>/delete')
def delete_user(user_id):
    delete(user_id)
    return jsonify_with_data((200, 'OK'))

def delete(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

@bp.route('/hello/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    username = request.form.get('username')
    email = request.form.get('email')
    edit(user_id, username, email)

    return jsonify_with_data((200, 'OK'))

def edit(user_id, username, email):
    user_page = User.query.get(user_id)
    user_page.username = username
    user_page.email = email
    db.session.add(user_page)
    db.session.commit()

def get_all(type=None):
    stmt = User.query.filter_by()

    if type:
        stmt = stmt.filter_by(type=type)

    users = stmt.order_by(User.id.asc()).all()
    return [user.to_dict() for user in users]

def add(username, email):
    user = User(username=username, email=email)

    db.session.add(user)
    db.session.commit()

def jsonify_with_data(err, **kwargs):
    resp = {
        'data': kwargs,
        'message': err[1],
        'errno': err[0]
        }
    return jsonify(resp), 200
