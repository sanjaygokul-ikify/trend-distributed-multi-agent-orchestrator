class OrchestratorError(Exception):
    pass

class AgentError(OrchestratorError):
    pass

class ActionResultError(OrchestratorError):
    pass
