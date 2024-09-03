from dataclasses import dataclass

import pytest


@dataclass
class LabelData:
    name: str
    description: str

    def get_mark(self):
        return pytest.mark(self.name)

    def register_mark(self, config: pytest.Config):
        config.addinivalue_line("markers", f"{self.name}: {self.description}")