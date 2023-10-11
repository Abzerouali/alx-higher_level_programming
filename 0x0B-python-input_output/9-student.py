#!/usr/bin/python3
""" Contains the clas "Student" """


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with the provided attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation"""
        return self.__dict__