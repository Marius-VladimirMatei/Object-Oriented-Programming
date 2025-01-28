from track import Track
from album import Album

class MusicManager:
    def __init__(self):
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def remove_album(self, title):
        self.albums = [album for album in self.albums if album.title != title]

    def list_albums(self):
        for album in self.albums:
            print(album)

    def release_album(self, title):
        for album in self.albums:
            if album.title == title:
                print(album)
                return
        print("Album not found.")