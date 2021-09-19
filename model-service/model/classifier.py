class Classifier:
    def __init__(self, name, model, data_source):
        self._name = name
        self._model = model
        self._data_source = data_source

    def name(self):
        return self._name

    def model(self):
        return self._model

    def train(self, train, test):
        raise RuntimeError("Not implemented")

    def classify(self, data):
        raise RuntimeError("Not implemented")

    def checkpoint(self):
        raise RuntimeError("Not implemented")
