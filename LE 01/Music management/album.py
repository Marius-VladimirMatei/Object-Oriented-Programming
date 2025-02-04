from track import Track

# Album class and methods

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
