#!/usr/bin/python3
""" Console """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNB CONSOLE """

    prompt = '(hbnb) '

    def do_quit(self, line):
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
