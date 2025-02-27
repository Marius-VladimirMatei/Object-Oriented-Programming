from abc import ABC, abstractmethod


# Define all the base functionality for all models
class BaseModel(ABC):
    """Base model class for all models"""

    def __init__(self, id):
        self.id = id

    @abstractmethod
    def to_dict(self):
        """Convert object to dictionary for storage"""
        pass

    @abstractmethod
    @classmethod
    def from_dict(cls, data):
        """Create object from dictionary"""
        pass

    @abstractmethod
    def __str__(self):
        """String representation of the object"""
        pass
