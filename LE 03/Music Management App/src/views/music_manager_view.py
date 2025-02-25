import tkinter as tk
from tkinter import ttk
from src.views.artist_view import ArtistView
from src.controllers.artist_controller import ArtistController
from src.views.album_view import AlbumView
from src.controllers.album_controller import AlbumController
from src.views.create_entity_view import CreateEntityView
from src.views.track_view import TrackView
from src.controllers.track_controller import TrackController


class MusicManagerView(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root)
        self.create_widgets()

    def create_widgets(self):
        # Configure the frame to be responsive
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.pack(expand=True, fill="both", padx=10, pady=10)

        # Create header frame
        header_frame = ttk.Frame(self)
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        header_frame.columnconfigure(1, weight=1)

        # Create controllers
        self._artist_controller = ArtistController("artists.json")
        self._track_controller = TrackController("tracks.json")
        self._album_controller = AlbumController("albums.json")

        # Create notebook for tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0, sticky="nsew")

        # Create tabs
        self._artist_tab = ArtistView(self.notebook, self._artist_controller)
        self._album_tab = AlbumView(
            self.notebook,
            self._album_controller,
            self._track_controller,
            self._artist_controller,  # Add artist controller
        )
        self._track_tab = TrackView(
            self.notebook, self._track_controller, self._artist_controller
        )

        self._create_entity_tab = CreateEntityView(
            self.notebook,
            self._artist_controller,
            self._artist_tab.refresh_artists,
            self._track_controller,
            self._track_tab.refresh_tracks,
            self._album_controller,
            self._album_tab.refresh_albums,
        )

        # Add tabs to notebook
        self.notebook.add(self._artist_tab, text="Artists")
        self.notebook.add(self._album_tab, text="Albums")
        self.notebook.add(self._create_entity_tab, text="Create New")
        self.notebook.add(self._track_tab, text="Tracks")
