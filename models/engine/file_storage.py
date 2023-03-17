#!/usr/bin/python3

'''
    File Storage Module by Michael Mensah && Frimpong Rijkaard
'''
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
        '''
            sets in objects with key classname.id
            Args:
                obj
        '''

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        '''
            serializes __objects to JSON file
        '''
        newdict = {}
        with open(self.__file_path, mode='w+', encoding='utf-8') as f:
            for k, v in self.__objects.items():
                newdict[k] = v.to_dict()
                json.dump(newdict, f)

    def reload(self):
        '''
            deserializes the JSON file
        '''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                newobjects = json.load(f)
                for k, v in newobjects.items():
                    reloadedobj = eval('{}(**v)'.format(v['__class__']))
                    self.__objects[k] = reloadedobj
        except IOError:
            pass
