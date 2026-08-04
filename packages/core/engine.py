import logging
import threading
from typing import List, Dict
from .types import Agent, Action, Result
from .exceptions import OrchestratorError

logger = logging.getLogger(__name__)


class Engine:
    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.actions = {}
        self.results = {}
        self.lock = threading.Lock()

    def run(self) -> None:
        for agent in self.agents:
            self._run_agent(agent)

    def _run_agent(self, agent: Agent) -> None:
        try:
            actions = agent.get_actions()
            for action in actions:
                self._execute_action(action)
        except Exception as e:
            logger.error(f"Failed to run agent {agent.name}", exc_info=e)
            raise OrchestratorError(f"Failed to run agent {agent.name}")

    def _execute_action(self, action: Action) -> None:
        try:
            result = action.execute()
            self._handle_result(result)
        except Exception as e:
            logger.error(f"Failed to execute action {action.name}", exc_info=e)
            raise OrchestratorError(f"Failed to execute action {action.name}")

    def _handle_result(self, result: Result) -> None:
        with self.lock:
            self.results[result.agent_name] = result

    def get_results(self) -> Dict[str, Result]:
        with self.lock:
            return self.results.copy()
