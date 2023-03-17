#!/usr/bin/python3

''' Module by Michael Mensah && Frimpong Rijkaard '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' class Review that inherits from BaseModel
        Public class attributes
        (all initialized as empty string)

        Attributes:
        place_id, user_id, text
    '''
    place_id = ''
    user_id = ''
    text = ''
