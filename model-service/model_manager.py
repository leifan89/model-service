from typing import Any
from typing import Dict

from .model.classifier import Classifier

class ModelManager:
    def __init__(self, models: Dict[str, Classifier]):
        self.models = models

    def add_model(self, name: str, model: Classifier) -> None:
        if name in self.models:
            raise RuntimeError(f"Failed to add model with name {name}, already exists")

        self.models[name] = model

    def train_model(self, name: str, X, y) -> None:
        if name in self.models:
            self.models[name].train(X, y)
        else:
            raise RuntimeError(f"Model {name} is not found")

    def classify_with_model(self, name: str, X) -> Any:
        if name in self.models:
            return self.models[name].classify(X)
        else:
            raise RuntimeError(f"Model {name} is not found")
        