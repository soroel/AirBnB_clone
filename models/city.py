#!/usr/bin/python
""" holds class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of City """
    state_id = ""
    name = ""


    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
