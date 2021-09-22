from typing import Dict

from .model.classifier import Classifier
from .model.TreeClassifier import TreeClassifier
from .model_manager import ModelManager

class ModelService:
    @classmethod
    def init_from_disk(cls):
        # init from disk
        models = {}
        return cls(models)

    @classmethod
    def init(cls):
        name = "category"
        model = TreeClassifier(name, data_source=None)
        return cls({name: model})

    def __init__(self, models: Dict[str, Classifier]):
        self.model_manager = ModelManager(models)

    def train_model(self, name: str, X, y):
        self.model_manager.train_model(name, X, y)

    def classify_with_model(self, name: str, X):
        return self.model_manager.classify_with_model(name, X)

    def shutdown(self):
        print("shutting down model service")

