# anything with a dunder file in it (__init__.py) is a package.
# filepatsh are tricky. make the parent folder a package to avoid importing issues
import os
from packages.my_classes.game_class import Game

work_dir = os.getcwd()


def return_pid():
    return os.getpid()


def return_cpu_info():
    return os.cpu_count()


def return_new_vegas():
    return Game("Fallout New Vegas", "PC", "3.4")

