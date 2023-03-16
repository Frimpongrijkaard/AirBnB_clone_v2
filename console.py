#!/usr/bin/python3

''' Console for AirBnB '''
import cmd


class HBNBCommand(cmd.Cmd):
    ''' class to control console commands '''

    prompt = '(hbnb) '

    def do_quit(self, line):
        ''' exits the program '''

        return True

    def do_EOF(self, line):
        ''' implements EOF
            exits console on command
        '''

        return True

    def emptyline(self):
        ''' Do nothing when an empty line is received. '''

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
