import os
from flask import Flask

from .model_service import ModelService

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    model_service = ModelService.init()

    @app.route('/')
    def root():
        return "Hello World!"

    @app.route('/shutdown')
    def shutdown():
        model_service.shutdown()
        return "shutdown"

    return app