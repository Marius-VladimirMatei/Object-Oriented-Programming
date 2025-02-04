from track import Track
from album import Album
from music_manager import MusicManager

# main function with examples of usage

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
    print("Track 4 removed from the album.")
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
