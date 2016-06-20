from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This Default!'

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/login',methods=['GET','POST'])
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

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

#test,with link and route
# with app.test_request_context():
#     print url_for('index')
#     print url_for('login')
#     print url_for('login',next='/')
#     print url_for('profile',username='John Doe')

#url_for('static',filename='style.css')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')