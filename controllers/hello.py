from flask import render_template
from . import bp

@bp.route('/hello/')
@bp.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)