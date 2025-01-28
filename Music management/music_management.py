# Music Management App

class Track:
    def __init__(self, title, file_name, length):
        self.title = title
        self.file_name = file_name
        self.length = length  # Format: "HH:MM:SS"


    def get_length_in_seconds(self):
        hours, minutes, seconds = map(int, self.length.split(":"))  # map converts each string into an integer
        return hours * 3600 + minutes * 60 + seconds

    def __str__(self):
        return f"{self.title}, duration: [{self.length}]"


class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.tracks = []  # list to hold the track objects in an album

    def add_track(self, track):
            self.tracks.append(track)

    def remove_track(self, track_or_title):
        if isinstance(track_or_title, str):  # If it's a string (title)
            self.tracks = [track for track in self.tracks if track.title != track_or_title]
        elif isinstance(track_or_title, Track):  # If it's a Track object
            self.tracks = [track for track in self.tracks if track != track_or_title]


    def get_total_length(self):
        total_seconds = sum(track.get_length_in_seconds() for track in self.tracks)
        hours = total_seconds // 3600 # integer division to convert into full minute, removing remainder
        minutes = (total_seconds % 3600) // 60  # integer division to convert into full minute, removing remainder
        seconds = total_seconds % 60 # modulo operator to calculate remaining seconds
        return f"{hours:02}:{minutes:02}:{seconds:02}"  # display 2 digits for hours, minutes, and seconds


    def __str__(self):
        album_details = f"Album: {self.title}\nFrom: {self.artist}\nLength: {self.get_total_length()}\nTracklist: \n"
        for i, track in enumerate(self.tracks, start=1): # index number in the output list
            album_details += f"Track {i}: {track}\n"
        return album_details


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

    # Usage


if __name__ == "__main__":
    # Create tracks
    track1 = Track("Speak to Me", "speak_to_me.mp3", "00:03:57")
    track2 = Track("On the Run", "on_the_run.mp3", "00:03:34")
    track3 = Track("Time", "time.mp3", "00:07:05")
    track4 = Track("Echoes", "echoes.mp3", "01:23:45")

    # Create an album and add tracks
    album = Album("The Dark Side of the Moon", "Pink Floyd")
    album.add_track(track1)
    album.add_track(track2)
    album.add_track(track3)
    album.add_track(track4)

    # Manage albums
    manager = MusicManager()  # instance of an object from MusicManager class
    manager.add_album(album)

    # List all albums
    print("List All Albums:")
    manager.list_albums()

    # Release album
    print("Released Album:")
    manager.release_album("The Dark Side of the Moon")

    # Remove track
    print("Track 4 removoed from the album.")
    album.remove_track(track4)

    # Display album after removing track and calculate updated total length
    print(f"Album after removing track '{track4}':")
    print(album)

    # Calculate and display updated total playing time of the album
    print(f"Updated Total Playing Time of '{album.title}': {album.get_total_length()}")

    # Display details of a track
    print(f"\nTrack Details: {track1}")



    """ # Calculate and display total playing time of the album
    print(f"Total Playing Time of '{album.title}': {album.get_total_length()}")
   
    # Remove track
    album.remove_track(track4)

    # List all tracks in the album after removal
    print(f"\nAlbum after removing '{track4}' track:")
    print(album) """


