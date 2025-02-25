from src.models.base_model import BaseModel
from src.models.validator import Validator
from typing import Dict

class Track(BaseModel):
    def __init__(self, id: str, name: str, duration_seconds: int, artist_id: str):
        super(). __init__(id, name)
        self._duration_seconds = Validator.validate_number(duration_seconds)
        self._artist_id = Validator.validate_string(artist_id)

    def get_duration_minutes(self) -> str:
        """Converts the duration in seconds to a string in the format MM:SS."""
        minutes = self._duration_seconds // 60
        seconds = self._duration_seconds % 60
        return f"{minutes}:{seconds:02d}"

    def to_dict(self) -> Dict[str, str]:
        return {
            "id": self._id,
            "name": self._name,
            "duration_seconds": self._duration_seconds,
            "artist_id": self._artist_id,
        }

    def from_dict(dict):
        return Track(
            dict["id"],
            dict["name"],
            dict["duration_seconds"],
            dict["artist_id"],
        )


