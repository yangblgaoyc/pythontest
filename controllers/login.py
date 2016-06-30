from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from . import bp

@bp.route('/login',methods=['GET','POST'])
def login():
    # if request.method =='POST':
    #     do_the_login()
    # else:
    #     show_the_login_form()
    return 'Login Page'

# def do_the_login():
#     return 'get request'
#
# def show_the_login_form():
#     return 'post request'
