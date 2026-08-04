import argparse
from packages.core.types import Agent
from packages.services.orchestrator import OrchestratorService

import logging

def main():
    parser = argparse.ArgumentParser(description='Distributed Multi-Agent Orchestrator')
    parser.add_argument('--agents', nargs='+', help='Agent names')
    args = parser.parse_args()
    agents = [Agent(name, lambda: []) for name in args.agents]
    service = OrchestratorService(agents)
    service.run()

if __name__ == '__main__':
    main()
