from typing import Any
from typing import Tuple

class DataSource:
    def __init__(self, name: str):
        self._name = name

    def name(self) -> str:
        return self._name

    def fetch(self) -> Tuple[Any, Any]:
        return [self.fetch_features(), self.fetch_target()]

    def fetch_features(self) -> Any:
        raise RuntimeError("Not implemented")

    def fetch_target(self) -> Any:
        raise RuntimeError("Not implemented")

    def shutdown(self) -> None:
        raise RuntimeError("Not implemented")