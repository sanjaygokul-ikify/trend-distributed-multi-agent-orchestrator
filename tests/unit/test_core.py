import unittest
from packages.core.types import Agent, Action, Result
from packages.core.engine import Engine

class TestCore(unittest.TestCase):
    def test_agent(self):
        agent = Agent('test', lambda: [])
        self.assertEqual(agent.name, 'test')

    def test_action(self):
        action = Action('test', lambda: None)
        self.assertEqual(action.name, 'test')

    def test_result(self):
        result = Result('test', {})
        self.assertEqual(result.agent_name, 'test')

    def test_engine(self):
        engine = Engine([])
        self.assertEqual(engine.agents, [])

if __name__ == '__main__':
    unittest.main()
