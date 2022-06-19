from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Testing server'


def initialize_app(config):
    app.config.from_object(config)
    return app
