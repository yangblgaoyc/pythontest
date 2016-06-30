from flask import render_template
from . import bp

@bp.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return 'User %s' % username