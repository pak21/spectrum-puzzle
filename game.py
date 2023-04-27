#!/usr/bin/env python3

import environment
import program
import robot

def main():
    state_definitions = [
        program.StateDefinition(program.Action.PICK_UP, program.TrueCondition(), 1),
        program.StateDefinition(program.Action.MOVE_RIGHT, program.IsSinkCondition(), 2),
        program.StateDefinition(program.Action.DROP, program.TrueCondition(), 3),
        program.StateDefinition(program.Action.MOVE_LEFT, program.IsSourceCondition(), 0),
    ]
    p = program.Program(state_definitions)
    r = robot.Robot(p, (0, 0))

    initial_objects = {
            (0, 0): environment.ObjectType.BLOCK_BLUE
    }
    sources = {
            (0, 0): environment.ObjectType.BLOCK_RED
    }
    sinks = {
            (2, 0): []
    }
    b = environment.Board(initial_objects, sources, sinks)

    for _ in range(20):
        r.step(b)
        b.step()

    print(b)

if __name__ == '__main__':
    main()
