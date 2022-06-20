from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        """ user = request.form['user']
        password = request.form['password'] """
        print(request.form['user'])
        print(request.form['password'])

        return 'Ok'
    else:
        return render_template('auth/login.html')


def page_not_found(error):
    return render_template('errors/404.html'), 404


def initialize_app(config):
    app.config.from_object(config)
    app.register_error_handler(404, page_not_found)
    return app
