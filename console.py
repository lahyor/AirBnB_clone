#!/usr/bin/python3
import cmd
import Filestorage
import sys
import json
import os

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def quit_cmd(self, arg):
        """ Exit when user clicks on quit"""
        exit()

    def do_EOF(self, arg):
        """Exit when user input End_Of_File"""
        print('')
        exit()

    def emptyline(self):
        """ Method to pass when user inputs an emptyline"""
        pass

    def do_create(self, arg):
        """ Create a new instance """
        if len(arg) == 0:
            print('** class name missing **')
            return

        arg_list = arg.split()
        if len(arg_list) == 1:
            if arg_list[0] in self.classes:
                new_instance = self.classes[arg_list[0]]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print('** instance id missing **')

    def do_show(self, arg):
        """ Method to print instance """
        if len(arg) == 0:
            print('** class name missing **')
            return

        arg_list = arg.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                instance_dict = storage.all()
                print(instance_dict[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

	def do_destroy(self,arg):
		 if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                instance_dict = storage.all()
                print(instance_dict[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')gfv


if __name__ == '__main__':
    HBNBCommand().cmdloop()
