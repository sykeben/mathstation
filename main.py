# MathStation Main Script
# (C)2018 - Benjamin Sykes

import cmd

class MathShell (cmd.Cmd):
    intro = 'Welcome to MathShell on MathStation.   Type help or ? to list commands.\n'
    prompt = '[Math]$ '
    file = None

    # ----- Basic Math Commands -----
    def do_add(self, num):
        print("Not there yet!")

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if (__name__ == '__main__'):
    MathShell().cmdloop()