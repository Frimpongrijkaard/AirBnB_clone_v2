#!/usr/bin/python3

''' Module by Michael Mensah && Frimpong Rijkaard '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' class User that inherits from BaseModel
        Public class attributes
        (all initialized as empty string)

        Attributes:
        email, password, first_name, last_name
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
