"""
THEORY:
* Everything in python are objects.
* Everything in python derives from a class.
* Python has duck typing.
* For python, it is redundant to use getters and setters.
* For legibility and maintenability purposes, always apply typing to your methods.
* All classes inherit from object class.
* Minimal functionality of the object class:
    * __init__()
    * __str__()
    * __repr__()
    * __eq__()
    * __hash__()
"""
import weakref


class Shop: 
    def __init__(self, name: str):
        self.name = name
        

    def hire(self, employee: "Employee"):
        self.experience: int | None = employee.experience # Optional typing :)



class Cafe(Shop)
