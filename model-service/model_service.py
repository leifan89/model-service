from __future__ import annotations
import traceback
from typing import Any
from typing import Dict

from .model.classifier import Classifier
from .model.TreeClassifier import TreeClassifier
from .model_manager import ModelManager

from .data_source.db_source import DBSource

class ModelService:
    @classmethod
    def init_from_disk(cls) -> ModelService:
        # init from disk
        models = {}
        return cls(models)

    @classmethod
    def init(cls, models_spec: Dict[str, Any]) -> ModelService:
        try:
            for model in models_spec['models']:
                name = model['name']
                ds_config = model['data_source']
                type = ds_config['type']
                if type == 'db':
                    source = DBSource(ds_config['name'], ds_config)
                else:
                    raise RuntimeError(f"Provided unknown data source type: {type}")

                if model['type'] == 'TreeClassifier':
                    model = TreeClassifier(name, data_source=source)
                else:
                    raise RuntimeError(f"Provided unknown model type: {model['type']}")
                return cls({
                    name: model
                })
        
        except:
            traceback.print_exc()

    def __init__(self, models: Dict[str, Classifier]):
        self.model_manager = ModelManager(models)

    def train_model(self, name: str, X, y) -> None:
        self.model_manager.train_model(name, X, y)

    def classify_with_model(self, name: str, X) -> Any:
        return self.model_manager.classify_with_model(name, X)

    def shutdown(self) -> None:
        print("shutting down model service")
        if self.model_manager is not None:
            self.model_manager.shutdown()
