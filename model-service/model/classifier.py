from ..data_source.data_source import DataSource

class Classifier:
    def __init__(self, name: str, model, data_source: DataSource):
        self._name = name
        self._model = model
        self._data_source = data_source

    def name(self) -> str:
        return self._name

    def model(self):
        return self._model

    def train(self, train, test):
        raise RuntimeError("Not implemented")

    def classify(self, data):
        raise RuntimeError("Not implemented")

    def checkpoint(self):
        raise RuntimeError("Not implemented")

    def refresh(self):
        raise RuntimeError("Not implemented")
