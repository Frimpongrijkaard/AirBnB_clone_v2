#!/usr/bin/python3

'''
    File Storage Module by Michael Mensah && Frimpong Rijkaard
'''
import json
import models
from models.base_model import BaseModel


class FileStorage():
    '''
        Class FileStorage serializes instances to a JSON file and
        deserializes JSON file to instances

        class attributes:
                            file_path - private class attribute path to JSON
                            file
                            objects - private class attribute dictionary
                            to store all objects by <class name>.id
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' returns the dict __objects '''

        return self.__objects

    def new(self, obj):
        ''' sets in objects with key classname.id
            Args:
                obj
        '''

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        ''' serializes __objects to JSON file '''

        new_dict = {}
        with open(self.__file_path, mode='w+', encoding='utf-8') as f:
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
                json.dump(new_dict, f)

    def reload(self):
        ''' deserializes the JSON file '''

        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                new_obj = json.load(f)
                for key, value in new_obj.items():
                    re_obj = eval('{}(**value)'.format(value['__class__']))
                    self.__objects[key] = re_obj
        except IOError:
            pass
