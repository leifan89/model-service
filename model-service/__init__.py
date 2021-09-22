import os
from flask import Flask

from .model_service import ModelService

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    model_service = ModelService.init()

    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    iris = load_iris()

    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)

    @app.route('/')
    def root():
        return "Hello World!"

    @app.route('/train')
    def train():
        print("training")
        model_service.train_model("category", X_train, y_train)
        return "trained"

    @app.route('/classify')
    def classify():
        y_pred = model_service.classify_with_model("category", X_test)
        return f"Score is {accuracy_score(y_test, y_pred)}"

    @app.route('/shutdown')
    def shutdown():
        model_service.shutdown()
        return "shutdown"

    return app