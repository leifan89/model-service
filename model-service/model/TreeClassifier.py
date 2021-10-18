from typing import Any
from typing import Dict

from sklearn.tree import DecisionTreeClassifier

from .classifier import Classifier
from ..data_source.data_source import DataSource


class TreeClassifier(Classifier):
    def __init__(self, name: str, data_source: DataSource):
        super().__init__(name, DecisionTreeClassifier, data_source)

    def training_params(self) -> Dict[str, Any]:
        return {
            "max_leaf_nodes": [2, 5, 10, 20, 50, 100],
            "min_samples_split": [2, 3, 4]
        }

    def shutdown(self):
        if self._data_source is not None:
            self._data_source.shutdown()
