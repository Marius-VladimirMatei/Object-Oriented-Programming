import tkinter as tk
from tkinter import ttk, messagebox
from src.controllers.artist_controller import ArtistController
from src.controllers.track_controller import TrackController
from src.models.artist import Artist
from src.models.track import Track
from src.controllers.album_controller import AlbumController
from src.utils.time_utils import minutes_seconds_to_seconds


class CreateEntityView(tk.Frame):
    def __init__(
        self,
        parent: tk.Tk,
        artist_controller: ArtistController,
        artist_refresh_callback,
        track_controller: TrackController,  # Add track controller parameter
        track_refresh_callback,  # Add track refresh callback
        album_controller: AlbumController,  # Add album controller parameter
        album_refresh_callback,  # Add album refresh callback
    ):
        super().__init__(parent)
        self._artist_controller = artist_controller
        self._artist_refresh_callback = artist_refresh_callback
        self._track_controller = track_controller  # Store track controller
        self._track_refresh_callback = (
            track_refresh_callback  # Store track refresh callback
        )

        # Configure grid
        self.columnconfigure(0, weight=1)

        # Create radio buttons for entity selection
        self.entity_var = tk.StringVar(value="artist")

        radio_frame = ttk.Frame(self)
        radio_frame.grid(row=0, column=0, pady=10, sticky="ew")

        ttk.Radiobutton(
            radio_frame,
            text="Artist",
            variable=self.entity_var,
            value="artist",
            command=self._toggle_fields,
        ).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(
            radio_frame,
            text="Track",
            variable=self.entity_var,
            value="track",
            command=self._toggle_fields,
        ).pack(side=tk.LEFT, padx=5)

        # Create form frame
        self.form_frame = ttk.LabelFrame(self, text="Create New Entity")
        self.form_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        # Common fields
        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()

        ttk.Label(self.form_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self.form_frame, textvariable=self.id_var).grid(
            row=0, column=1, padx=5, pady=5
        )

        ttk.Label(self.form_frame, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(self.form_frame, textvariable=self.name_var).grid(
            row=1, column=1, padx=5, pady=5
        )

        # Track-specific fields
        self.duration_var = tk.StringVar()
        self.artist_id_var = tk.StringVar()

        self.track_fields = []

        # Duration label with MM:SS format hint
        self.duration_label = ttk.Label(self.form_frame, text="Duration (MM:SS):")
        self.duration_entry = ttk.Entry(self.form_frame, textvariable=self.duration_var)
        self.track_fields.extend([self.duration_label, self.duration_entry])

        # Artist ID
        self.artist_label = ttk.Label(self.form_frame, text="Artist ID:")
        self.artist_entry = ttk.Entry(self.form_frame, textvariable=self.artist_id_var)
        self.track_fields.extend([self.artist_label, self.artist_entry])

        # Create button
        self.create_button = ttk.Button(
            self, text="Create", command=self._create_entity
        )
        self.create_button.grid(row=2, column=0, pady=10)

        # Initialize the form
        self._toggle_fields()

    def _toggle_fields(self):
        # Hide all track fields first
        for widget in self.track_fields:
            widget.grid_remove()

        if self.entity_var.get() == "track":
            # Show track fields
            self.duration_label.grid(row=2, column=0, padx=5, pady=5)
            self.duration_entry.grid(row=2, column=1, padx=5, pady=5)
            self.artist_label.grid(row=4, column=0, padx=5, pady=5)
            self.artist_entry.grid(row=4, column=1, padx=5, pady=5)

    def _create_entity(self):
        try:
            if self.entity_var.get() == "artist":
                artist = Artist(self.id_var.get(), self.name_var.get())
                self._artist_controller.add_artist(artist)
                self._artist_refresh_callback()
                messagebox.showinfo("Success", "Artist created successfully!")
            else:
                # Create track
                # COnvert MM:SS before creating track object
                duration_seconds = minutes_seconds_to_seconds(self.duration_var.get())

                track = Track(
                    self.id_var.get(),
                    self.name_var.get(),
                    duration_seconds,  # Pass duration in seconds
                    self.artist_id_var.get(),
                )
                self._track_controller.add_track(track)
                self._track_refresh_callback()
                messagebox.showinfo("Success", "Track created successfully!")

            # Clear fields
            self._clear_fields()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def _clear_fields(self):
        self.id_var.set("")
        self.name_var.set("")
        self.duration_var.set("")
        self.artist_id_var.set("")
