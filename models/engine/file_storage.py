#!/usr/bin/python3
import json
from pickletools import pydict
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
"""
module store file of any instance created write and read them

"""
class FileStorage:
    """
    json file serialize and deserialize instances
    
    Private class attribute:
        __file_path: json file name
        __object: dictionary in python
    
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        class_n = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_n, obj.id)] = obj
        
    def save(self):
        """
        serialize __object to the json file 
        
        """
        mydict = {}
        obj_dict = FileStorage.__objects
        for key1 in obj_dict.key():
            for key2, value2 in obj_dict.to_dict[key1].items():
                mydict[key2] = value2
                
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(mydict, f)
            
    def reload(self):
        """deserialize the json file """
        
        try:
            with open(FileStorage.__file_path, 'r') as f:
                    OM = json.load(f)
                    return OM
                    
        except FileNotFoundError:
            return 