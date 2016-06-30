from flask import render_template
from . import bp

@bp.route('/')
def hello_world():
    return 'This Default!'