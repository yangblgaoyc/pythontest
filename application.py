from flask import Flask
from controllers import bp
app = Flask(__name__)

app.register_blueprint(bp)

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