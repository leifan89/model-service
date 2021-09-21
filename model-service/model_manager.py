from typing import Dict

from .model.classifier import Classifier

class ModelManager:
    def __init__(self, models):
        self.models : Dict[str, Classifier] = []

    def add_model(self, name: str, model: Classifier):
        if name in self.models:
            raise RuntimeError(f"Failed to add model with name {name}, already exists")

        self.models[name] = model
