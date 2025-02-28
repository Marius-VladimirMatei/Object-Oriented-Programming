from typing import Type, TypeVar, Generic
from src.models.base_model import BaseModel
import json

# Declare type variable T as a subclass of BaseModel
T = TypeVar("T", bound=BaseModel)


# Define a generic class Persistence that takes a type parameter T
# This class implements the persistence logic for any model that inherits from BaseModel
# This class can be particularized for customer, vehicle and rental


class Storage(Generic[T]):
    def __init__(self, storage_file: str, model_class: Type[T]):
        self.storage_file = storage_file
        self.model_class = model_class
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
            return [self.model_class.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open(self.storage_file, "w") as f:
            json.dump([item.to_dict() for item in self.data], f, indent=4)
