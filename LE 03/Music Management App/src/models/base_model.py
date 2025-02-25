from abc import ABC, abstractmethod
from src.models.validator import Validator


class BaseModel(ABC):
    """
    Base model class for all the entities in the application.
    """

    def __init__(self, id: str, name: str):
        self._id = Validator.validate_string(id)
        self._name = Validator.validate_name(name)

    @abstractmethod
    def to_dict(self):
        """
        Converts the object to a dictionary used for serialization.
        """
        pass

    @abstractmethod
    def from_dict(dict):
        """
        Converts the object from a dictionary used for deserialization.
        """
        pass
