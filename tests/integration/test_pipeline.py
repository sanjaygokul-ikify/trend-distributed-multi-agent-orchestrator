import unittest
from packages.core.types import Agent, Action, Result
from packages.services.orchestrator import OrchestratorService
from packages.core.engine import Engine

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        agent = Agent('test', lambda: [Action('test', lambda: Result('test', {}))])
        engine = Engine([agent])
        engine.run()
        results = engine.get_results()
        self.assertIn('test', results)

if __name__ == '__main__':
    unittest.main()
