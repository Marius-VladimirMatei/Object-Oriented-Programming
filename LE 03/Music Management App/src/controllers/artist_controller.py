from src.models.artist import Artist
import json


class ArtistController:
    def __init__(self, file_name: str):
        self._file_name = file_name
        self._artists: dict[str, Artist] = {}  # empty dictionary of artists
        try:
            self.load_artists()
        except:
            pass

    def add_artist(self, artist: Artist) -> None:
        if artist._id in self._artists:
            raise ValueError(f"Artist with id {artist._id} already exists.")
        self._artists[artist._id] = artist
        self.save_artists()

    def save_artists(self):
        data: dict[str, dict[str, str]] = {}

        for n, artist in self._artists.items():
            data[artist._id] = artist.to_dict()

        with open(self._file_name, "w") as f:
            json.dump(data, f, indent=4)

    def load_artists(self) -> None:
        """
        Load artists from a file and add them to the controller.
        """
        with open(self._file_name, "r") as f:
            data = json.load(f)
            for n, artist in data.items():
                a = Artist.from_dict(artist)
                self.add_artist(a)

    def delete_artist(self, artist_id: str) -> None:
        """
        Delete an artist by their ID.
        Raises ValueError if artist doesn't exist.
        """

        if artist_id not in self._artists:
            raise ValueError(f"Artist with id {artist_id} does not exist.")

        del self._artists[artist_id]
        self.save_artists()
