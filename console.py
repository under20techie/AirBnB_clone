#!/usr/bin/python3
""" Console """
import cmd
from inspect import isclass
import models as md
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNB CONSOLE """

    prompt = '(hbnb) '
    all_models = ["BaseModel", "User", "City", "Place",
"State", "Amenity", "Review"]

    def do_quit(self, line):
        """ Quit """
        return True

    def do_EOF(self, line):
        """EOF"""
        return True

    def emptyline(self):
        """Empty"""
        return

    def do_create(self, cls_name):
        """Creates a new instance of BaseModel and subclasses"""

        if cls_name:
            if cls_name not in self.all_models:
                print("** class doesn't exist **")
                return

            new_instance = eval(cls_name)()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]

        if cls_name not in self.all_models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        id_no = args[1]

        try:
            obj = md.storage.all()[f"{cls_name}.{id_no}"]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance"""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if not cls_name not in self.all_models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id_no = args[1]
        try:
            obj = md.storage.all()
            del obj[f"{cls_name}.{id_no}"]
            md.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances """

        if arg:
            if arg not in self.all_models:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in md.storage.all().values()])

    def do_update(self, arg):
        """Updates an instance"""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]

        if cls_name not in self.all_models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id_no = args[1]

        try:
            obj = md.storage.all()[f"{cls_name}.{id_no}"]
        except KeyError:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        setattr(obj, args[2], args[3])
        md.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
