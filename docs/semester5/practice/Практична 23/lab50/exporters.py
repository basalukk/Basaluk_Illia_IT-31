from abc import ABC, abstractmethod
from pathlib import Path


class Exporter(ABC):
    @abstractmethod
    def export(self, expenses, path):
        pass

    def target(self, name):
        return Path(f"{name}.{self.extension()}")

    @abstractmethod
    def extension(self):
        pass
