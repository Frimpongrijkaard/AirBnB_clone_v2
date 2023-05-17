#!/usr/bin/python3
from models import storage 
from uuid import uuid4
from datetime import datetime


"""
Basemodel of which other classes of  model 
will inherit from 

"""
class BaseModel:
    """
        this module create an id with uniqne string 
        for different, current time and instance where created
        when it need to update,. thos module also contain
        instance method that save and add to dict
        
        instance Attribute:
                id : id string format
                created_at: current datetime
                updated_at: update datetime
        
    """
    def __init__(self, *args, **kwargs):
        """public intance of the basemodel 
           that handle id, created_at and update_at
           
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs is not None:
            for key, value in kwargs.items():
                if 'created_at' == key or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f' )
                    
                else:
                    self.__dict__[key] = value
        else:
            storage.new(self)
        
        
    def __str__(self):
        Base = self.__class__.__name__
        return ("[{}] ({}) {}".format(Base, self.id, self.__dict__))
    
    def save(self):
        self.updated_at =  datetime.now()
        storage.save(self)
        
        
    def to_dic(self):
        obj = self.__dict__.copy()
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updateed_at.isoformat()
        obj['__class__'] = self.__class__.__name__
        return obj
    
    
    
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))