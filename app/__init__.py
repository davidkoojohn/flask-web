
from flask import Flask

from config import DevConfig

app = Flask(__name__)


def create_app():
    app.config.from_object(DevConfig)

    return app


@app.route('/')
def index():
    return 'index'


