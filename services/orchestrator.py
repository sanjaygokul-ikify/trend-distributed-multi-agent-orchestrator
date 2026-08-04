from typing import List
from packages.core.types import Agent
from packages.core.engine import Engine

class OrchestratorService:
    def __init__(self, agents: List[Agent]):
        self.engine = Engine(agents)

    def run(self) -> None:
        self.engine.run()
