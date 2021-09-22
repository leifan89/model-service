from re import S
from sklearn.base import ClassifierMixin
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from typing import Any
from typing import Dict
from typing import Type

from ..data_source.data_source import DataSource

class Classifier:
    def __init__(self, name: str, model_class: type, data_source: DataSource):
        self._name = name
        self._data_source = data_source
        
        self._scaler = StandardScaler()
        self._model = model_class()

    def name(self) -> str:
        return self._name

    def model(self):
        return self._model

    def train(self, X, y):
        params = self.training_params()
        scaled_X = self._scaler.fit_transform(X)

        clf = GridSearchCV(self._model, params, cv=3, n_jobs=-1)
        clf.fit(X, y)

        self._model = clf.best_estimator_
        print(f"""
            Fitted model of type {type(self._model)}
            Best score: {clf.best_score_}
            Best params: {clf.best_params_}
        """)

    def classify(self, data):
        scaled = self._scaler.transform(data)
        return self._model.predict(scaled)

    def checkpoint(self):
        raise RuntimeError("Not implemented")

    def refresh(self):
        raise RuntimeError("Not implemented")

    def training_params(self) -> Dict[str, Any]:
        raise RuntimeError("Not implemented")
