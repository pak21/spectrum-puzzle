import dataclasses
import typing

import environment
import program

@dataclasses.dataclass
class Robot():
    program: program.Program
    position: (int, int)
    state: int = 0
    carrying: typing.Optional[environment.ObjectType] = None

    _ACTION_FNS = {
            program.Action.NOOP: lambda s, b: None,
            program.Action.PICK_UP: lambda s, b: s._pickup(b),
            program.Action.DROP: lambda s, b: s._drop(b),
            program.Action.MOVE_RIGHT: lambda s, b: s._move((1, 0)),
            program.Action.MOVE_UP: lambda s, b: s._move((0, 1)),
            program.Action.MOVE_LEFT: lambda s, b: s._move((-1, 0)),
            program.Action.MOVE_DOWN: lambda s, b: s._move((0, -1)),
    }

    def step(self, board):
        state_definition = self.program.state_definitions[self.state]
        self._ACTION_FNS[state_definition.action](self, board)
        if state_definition.condition.evaluate(self, board):
            self.state = state_definition.next_state

    def _move(self, move):
        self.position = (self.position[0] + move[0], self.position[1] + move[1])

    def _pickup(self, board):
        if self.carrying is None:
            self.carrying = board.pickup_from(self.position)

    def _drop(self, board):
        if self.carrying is not None and board.drop_at(self.position, self.carrying):
            self.carrying = None
