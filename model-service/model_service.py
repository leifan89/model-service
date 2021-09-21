from typing import Dict

from sklearn.tree import DecisionTreeClassifier

from .model.classifier import Classifier
from .model_manager import ModelManager

class ModelService:
    @classmethod
    def init_from_disk(cls):
        # init from disk
        models = {}
        return cls(models)

    @classmethod
    def init(cls):
        return cls({})

    def __init__(self, models: Dict[str, Classifier]):
        self.model_manager = ModelManager(models)

    def shutdown(self):
        print("shutting down model service")

