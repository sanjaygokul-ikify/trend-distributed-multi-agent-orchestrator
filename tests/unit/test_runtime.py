import unittest
from packages.services.orchestrator import OrchestratorService
from packages.core.types import Agent

class TestRuntime(unittest.TestCase):
    def test_orchestrator_service(self):
        agents = [Agent('test', lambda: [])]
        service = OrchestratorService(agents)
        service.run()

if __name__ == '__main__':
    unittest.main()
