import logging
import threading
from typing import List, Dict
from ..core.engine import Engine
from ..core.types import Agent, Action, Result
from ..core.exceptions import OrchestratorError

logger = logging.getLogger(__name__)


class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.running = False
        self.lock = threading.Lock()

    def start(self) -> None:
        with self.lock:
            if not self.running:
                self.running = True
                self._start_execution()

    def stop(self) -> None:
        with self.lock:
            if self.running:
                self.running = False

    def _start_execution(self) -> None:
        threading.Thread(target=self.engine.run).start()
