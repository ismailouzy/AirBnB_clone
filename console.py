#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
""" the interpreter of AirBnb console tha inherratce from cmd
and handle commands"""


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""
    prompt = "(hbnb) "

    command_class = {
        "BaseModel",
        "User",
        "Place",
        "Amenity",
        "City",
        "Review",
        "State",
    }

    def do_quit(self, command):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """ This method represents quit Commande"""
        return True

    def do_EOF(self, command):
        """Handle the End Of File by clicking on ctr + d"""
        print()
        return True

    def emptyline(self):
        """This module represents empty line """
        pass

    def do_create(self, command):
        """Create a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        args = command.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.command_class:
            print("** class doesn't exist **")
        else:
            instance = (eval(args[0])().id)
            storage.save()
            print(instance)

    def do_show(self, command):
        """Prints the string representation of an instance"""
        args = command.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.command_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            models_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in models_dict:
                obj_str = models_dict[key]
                print(obj_str)
            else:
                print("** no instance found **")

    def do_destroy(self, command):
        """Deletes an instance based on the class name and id"""
        args = command.split()
        models_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.command_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models_dict:
                del models_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            try:
                models_dict = storage.all()
                instances = [str(value) for value in models_dict.values()]
                print(instances)
            except FileNotFoundError:
                print("[]")
        else:
            try:
                cls_name = eval(arg).__name__
                models_dict = storage.all()
                instances = [str(value) for key, value in models_dict.items()
                             if key.startswith(cls_name)]
                print(instances)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            models_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in models_dict:
                print("** no instance found **")
                return
            obj = models_dict[key]
            setattr(obj, args[2], args[3])
            obj.save()
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
