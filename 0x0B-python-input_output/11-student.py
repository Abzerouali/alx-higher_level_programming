#!/usr/bin/python3
"""Student class definition with attributes and methods for JSON serialization"""

class Student:
    """A class that defines a student by their first name, last name, and age."""
    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with the provided attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the student, optionally filtering attributes."""
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    my_dict[i] = getattr(self, i)
            return my_dict
def reload_from_json(self, json):
    """that replaces all attributes of the student instance"""
    for key, value in json.items():
        setattr(self, key, value)
