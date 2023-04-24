import dataclasses

import program

@dataclasses.dataclass
class Robot():
    program: program.Program
    state: int = 0

    def step(self):
        print(f'Robot is in state {self.state}')
        foo = self.program.foos[self.state]
        print(f'Robot executes action {foo.action}')
        switch = foo.condition.evaluate()
        print(f'Condition evalues to {switch}')
        if switch:
            self.state = foo.next_state
            print(f'Robot switches to state {self.state}')
        else:
            print(f'Robot stays in state {self.state}')
        print()
