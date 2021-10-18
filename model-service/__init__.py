import atexit
import json

import pandas as pd
import yaml
from flask import Flask

from .model_service import ModelService


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    with open('model-service/config.yml', 'r') as f:
        config = yaml.load(f, Loader=yaml.Loader)

    print("Running Flask server with config")
    print(json.dumps(config, indent=4))

    model_service_app = ModelService.init(config)

    # from sklearn.datasets import load_iris
    # from sklearn.model_selection import train_test_split
    # from sklearn.metrics import accuracy_score
    # iris = load_iris()
    #
    # X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)

    @ app.route('/')
    def root():
        return "Hello World!"

    @app.route('/train')
    def train():
        # model_service_app.train_model("category", X_train, y_train)
        model_service_app.refresh_model("category")
        return "trained"

    @app.route('/classify')
    def classify():
        # y_pred = model_service_app.classify_with_model("category", X_test)
        test_df = pd.DataFrame.from_dict({
            'name': ['name1'],
            'location': ['loc1']
        })
        output = model_service_app.classify_with_model("category", test_df)
        return f"Output is {output}"

    @app.route('/refresh')
    def refresh():
        model_service_app.refresh_model("category")
        return "refresh"

    @app.route('/shutdown')
    def shutdown():
        model_service_app.shutdown()
        return "shutdown"

    atexit.register(shutdown)

    return app
