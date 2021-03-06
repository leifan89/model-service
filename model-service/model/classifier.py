from typing import Any
from typing import Dict

from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder

from ..data_source.data_source import DataSource


class Classifier:
    def __init__(self, name: str, model_class: type, data_source: DataSource):
        self._name = name
        self._data_source = data_source

        self._feature_encoder = OrdinalEncoder()
        self._target_encoder = LabelEncoder()
        self._model = model_class()

        self._trained = False

    def name(self) -> str:
        return self._name

    def model(self):
        return self._model

    def train(self, X, y) -> None:
        params = self.training_params()
        encoded_X = self._feature_encoder.fit_transform(X)
        encoded_y = self._target_encoder.fit_transform(y)

        clf = GridSearchCV(self._model, params, cv=3, n_jobs=-1)
        clf.fit(encoded_X, encoded_y)

        self._model = clf.best_estimator_
        print(f"""
            Fitted model of type {type(self._model)}
            Best score: {clf.best_score_}
            Best params: {clf.best_params_}
        """)

        self._trained = True

    def classify(self, data):
        if self._model is None or not self._trained:
            raise RuntimeError(f"Trying to classify {self.name()} without training")

        encoded = self._feature_encoder.transform(data)
        prediction = self._model.predict(encoded)
        return self._target_encoder.inverse_transform(prediction)

    def checkpoint(self) -> None:
        raise RuntimeError("Not implemented")

    def refresh(self) -> None:
        X, y = self._data_source.fetch()
        self.train(X, y)

    def training_params(self) -> Dict[str, Any]:
        raise RuntimeError("Not implemented")

    def shutdown(self) -> None:
        raise RuntimeError("Not implemented")
