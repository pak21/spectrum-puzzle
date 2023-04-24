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
    def evaluate(self):
        pass

class TrueCondition(Condition):
    def evaluate(self): return True

class FalseCondition(Condition):
    def evaluate(self): return False

@dataclasses.dataclass
class Foo():
    action: Action
    condition: Condition
    next_state: int

@dataclasses.dataclass
class Program():
    foos: list[Foo]
