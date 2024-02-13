#!/usr/bin/python3
""" Console """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNB CONSOLE """

    def do_quit(self):
        """ Quit """
        return True

    def do_EOF(self, line):
        """EOF"""
        return True

    def emptyline(self):
        """Empty"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
