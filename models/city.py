#!/usr/bin/python3

''' Module by Michael Mensah && Frimpong Rijkaard '''
from models.base_model import BaseModel


class City(BaseModel):
    ''' class City that inherits from BaseModel
        Public class attributes
        (all initialized as empty string)

        Attributes:
        state_id, name
    '''
    state_id = ''
    name = ''
