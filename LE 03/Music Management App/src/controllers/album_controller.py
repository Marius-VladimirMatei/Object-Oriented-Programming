from src.models.album import Album
import json


class AlbumController:
    def __init__(self, file_name: str):
        self._file_name = file_name
        self._albums: dict[str, Album] = {}  # empty dictionary of albums
        try:
            self.load_albums()
        except:
            pass

    def add_album(self, album: Album) -> None:
        if album._id in self._albums:
            raise ValueError(f"Album with id {album._id} already exists.")
        self._albums[album._id] = album
        self.save_albums()

    def save_albums(self):
        data: dict[str, dict[str, str]] = {}

        for n, album in self._albums.items():
            data[album._id] = album.to_dict()

        with open(self._file_name, "w") as f:
            json.dump(data, f, indent=4)

    def load_albums(self) -> None:
        """
        Load albums from a file and add them to the controller.
        """
        with open(self._file_name, "r") as f:
            data = json.load(f)
            for n, album in data.items():
                a = Album.from_dict(album)
                self.add_album(a)

    def delete_album(self, album_id: str) -> None:
        """
        Delete an album by its ID.
        Raises ValueError if album doesn't exist.
        """
        if album_id not in self._albums:
            raise ValueError(f"Album with id {album_id} does not exist.")

        del self._albums[album_id]
        self.save_albums()
