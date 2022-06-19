from app import initialize_app
from config import config

configuration = config['development']
app = initialize_app(config=configuration)

if __name__ == '__main__':
    app.run()
