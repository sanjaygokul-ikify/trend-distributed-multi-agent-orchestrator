from typing import Dict
from dataclasses import dataclass

@dataclass
class Metrics:
    name: str
    value: int

    def to_dict(self) -> Dict[str, int]:
        return {self.name: self.value}
