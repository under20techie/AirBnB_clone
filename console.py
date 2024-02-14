#!/usr/bin/python3
""" Console """
import cmd
import re
from inspect import isclass
import models as md
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review


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
        if cls_name not in self.all_models:
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
            return

    def do_all(self, arg):
        """Prints all string representation of all instances """

        if arg:
            if arg not in self.all_models:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in md.storage.all().values( ) if type(obj) == eval(arg)])
        else:
            print([str(obj) for obj in md.storage.all().values( )])
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
        obj.save()

    def default(self, line):
        """Default"""

        pattern = re.compile(r'^(.*?)\.(.*?)\((.*?),?\)$')
        match = pattern.match(line)

        if match:
            groups = match.groups()
             print(f'Matched: {s}')
             print(f'Groups: {groups}')
        else:
            return

        cls_name = groups[0]
        func = groups[1]
        par_1 = groups[2]

        if len(groups) == 3:
            if func == "all":
               self.do_all(cls_name)
               return
            elif func == "count":
                self.do_count(cls_name)
                return
            elif func in ["show", "destroy"]:
                par = f"{cls_name} {par_1}"
                par = "{} {}".format(cls_name, par_1)
                eval(f"self.do_{func}")(par)
                return

        par_2 = groups[2]

        if len(groups) == 4:
            if func == "update":
                par_2, par_3 = eval(par_2).values()
                par = "{} {} {} {}".format(cls_name, par_1, par_2, par_3)
                eval(f"self.do_{func}")(par)
                return

        par_3 = groups[4]

        if len(groups) == 5 and func == "update":
            par = "{} {} {} {}".format(cls_name, par_1, par_2, par_3)
            eval(f"self.do_{func}")(par)
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
