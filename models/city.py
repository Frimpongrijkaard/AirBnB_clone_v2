#!/usr/bin/python3
"""define the city class"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    this class attribute describes a cities
    
        Attributes:
        
            state_id (str): The state id.
            name (str): The name of the city.
        
    """
    state_id = ""
    name = ""