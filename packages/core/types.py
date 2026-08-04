from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    get_actions: callable

@dataclass
class Action:
    name: str
    execute: callable

@dataclass
class Result:
    agent_name: str
    data: Dict[str, str]
