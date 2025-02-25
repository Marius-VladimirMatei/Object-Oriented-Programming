from src.models.base_model import BaseModel
from typing import Dict


class Artist(BaseModel):
    """ Represents the artist object in the application"""
    def __int__(self, id: str, name: str):
        super().__init__(id, name)

    def to_dict(self) -> Dict[str, str]:
        return {"id": self._id, "name": self._name}

    def from_dict(dict): # returns artist object from dictionary
        return Artist(dict["id"], dict["name"])