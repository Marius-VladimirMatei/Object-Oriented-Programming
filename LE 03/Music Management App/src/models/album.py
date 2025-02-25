from src.models.base_model import BaseModel
from src.models.validator import Validator


class Album(BaseModel):
    def __init__(
        self, id: str, name: str, year: int, artist_id: str, track_list: list[str]
    ):
        super().__init__(id, name)
        self._artist_id = Validator.validate_string(artist_id)
        self._year = Validator.validate_number(year)
        self._track_list = Validator.validate_track_list(track_list)

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "year": self._year,
            "artist_id": self._artist_id,
            "track_list": self._track_list,
        }

    def from_dict(dict):
        return Album(
            dict["id"],
            dict["name"],
            dict["year"],
            dict["artist_id"],
            dict["track_list"],
        )
