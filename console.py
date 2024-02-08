#!/usr/bin/python3
import cmd
import Filestorage
import sys
import json
import os

class class HBNBCommand(cmd.Cmd):
    def user_prompt = (hbnb)

    def quit_cmd(self, arg):
        """ Exit when user clicks on quit"""
        exit()

    def EOF_cmd(self, arg):
        """Exit when user input End_Of_File"""
        print ('')
        exit()

    def empty_input(self):
        """ Method to pass when user inputs an emptyline"""
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
