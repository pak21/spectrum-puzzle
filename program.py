import abc
import dataclasses
import enum

class Action(enum.Enum):
    NOOP = enum.auto(),
    PICK_UP = enum.auto(),
    DROP = enum.auto(),
    MOVE_RIGHT = enum.auto(),
    MOVE_UP = enum.auto(),
    MOVE_LEFT = enum.auto(),
    MOVE_DOWN = enum.auto(),

class Condition(abc.ABC):
    @abc.abstractmethod
    def evaluate(self, robot, board):
        pass

class TrueCondition(Condition):
    def evaluate(self, robot, board): return True

class FalseCondition(Condition):
    def evaluate(self, robot, board): return False

class IsSourceCondition(Condition):
    def evaluate(self, robot, board):
        return robot.position in board.sources

class IsSinkCondition(Condition):
    def evaluate(self, robot, board):
        return robot.position in board.sinks

@dataclasses.dataclass
class StateDefinition():
    action: Action
    condition: Condition
    next_state: int

@dataclasses.dataclass
class Program():
    state_definitions: list[StateDefinition]
