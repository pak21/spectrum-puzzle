#!/usr/bin/env python3

import program
import robot

def main():
    foo0 = program.Foo(program.Action.PICK_UP, program.TrueCondition(), 1)
    foo1 = program.Foo(program.Action.MOVE_RIGHT, program.FalseCondition(), 2)
    p = program.Program([foo0, foo1])
    r = robot.Robot(p)

    r.step()
    r.step()
    r.step()

if __name__ == '__main__':
    main()
