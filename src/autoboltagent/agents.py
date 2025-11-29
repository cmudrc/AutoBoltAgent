import smolagents
from .low_fidelity_tool import LowFidelityCalculator
from .high_fidelity_tool import HighFidelityCalculator
class GuessingAgent(smolagents.ToolCallingAgent):
    def __init__(self):
        super().__init__(
            name="GuessingAgent",
            model="",
            tools=[],
        )
class LowFidelityAgent(smolagents.Agent):
    def __init__(self):
        super().__init__(
            model="LowFidelityAgent",
            tools=[LowFidelityCalculator()],
        )
class HighFidelityAgent(smolagents.Agent):
    def __init__(self):
        super().__init__(
            model="HighFidelityAgent",
            tools=[HighFidelityCalculator()],
        )
class DualFidelityAgent(smolagents.Agent):
    def __init__(self):
        super().__init__(
            model="DualFidelityAgent",
            tools=[LowFidelityCalculator(), HighFidelityCalculator()],
        )