from flask import render_template
from . import bp

@bp.route('/index')
def index():
    return 'Index Page'