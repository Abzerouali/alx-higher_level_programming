#!/usr/bin/python3

"""Base Class Definition and Utilities"""
import json


class Base:
    """Base model class.

    Represents the foundation for all other classes in project 0x0C*.

    Private Class Attributes:
    __nb_objects (int): Number of instantiated Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base object.

        Args:
        id (int): The identifier for the new Base object.
        """
        if id is not None:
            type(self).id = id
        else:
            type(self).__nb_objects += 1
            type(self).id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
         Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create and return a class instance from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Load and return a list of class instances from a JSON file.

        Reads from '<cls.__name__>.json'.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated class instances.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
