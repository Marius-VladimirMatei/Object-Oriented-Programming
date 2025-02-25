from src.models.track import Track
import json


class TrackController:
    def __init__(self, file_name: str):
        self._file_name = file_name
        self._track: dict[str, Track] = {}  # empty dictionary of tracks
        try:
            self.load_tracks()
        except:
            pass

    def add_track(self, track: Track) -> None:
        if track._id in self._track:
            raise ValueError(f"Track with id {track._id} already exists.")
        self._track[track._id] = track
        self.save_tracks()

    def save_tracks(self):
        data: dict[str, dict[str, str]] = {}

        for n, track in self._track.items():
            data[track._id] = track.to_dict()

        with open(self._file_name, "w") as f:
            json.dump(data, f, indent=4)

    def load_tracks(self) -> None:
        """
        Load tracks from a file and add them to the controller.
        """
        with open(self._file_name, "r") as f:
            data = json.load(f)
            for n, track in data.items():
                a = Track.from_dict(track)
                self.add_track(a)

    def delete_track(self, track_id: str) -> None:
        """
        Delete an track by their ID.
        Raises ValueError if track doesn't exist.
        """

        if track_id not in self._track:
            raise ValueError(f"Track with id {track_id} does not exist.")

        del self._track[track_id]
        self.save_tracks()
