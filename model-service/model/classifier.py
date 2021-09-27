from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

from typing import Any
from typing import Dict

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

    def train(self, X, y) -> None:
        # self.refresh()

        params = self.training_params()
        scaled_X = self._scaler.fit_transform(X)

        clf = GridSearchCV(self._model, params, cv=3, n_jobs=-1)
        clf.fit(scaled_X, y)

        self._model = clf.best_estimator_
        print(f"""
            Fitted model of type {type(self._model)}
            Best score: {clf.best_score_}
            Best params: {clf.best_params_}
        """)

    def classify(self, data):
        scaled = self._scaler.transform(data)
        return self._model.predict(scaled)

    def checkpoint(self) -> None:
        raise RuntimeError("Not implemented")

    def refresh(self) -> None:
        X, y = self._data_source.fetch()
        print(X)
        print(y)
        # self.train(X, y)

    def training_params(self) -> Dict[str, Any]:
        raise RuntimeError("Not implemented")

    def shutdown(self) -> None:
        raise RuntimeError("Not implemented")