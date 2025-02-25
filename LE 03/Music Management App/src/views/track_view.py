from src.models.track import Track
from src.controllers.track_controller import TrackController
from src.controllers.artist_controller import ArtistController
import tkinter as tk
from tkinter import ttk, messagebox
from src.utils.time_utils import seconds_to_minutes_seconds


class TrackView(tk.Frame):
    def __init__(
        self,
        parent: tk.Tk,
        track_controller: TrackController,
        artist_controller: ArtistController,
    ):
        super().__init__(parent)
        self._track_controller = track_controller
        self._artist_controller = artist_controller

        # Configure the frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Create Treeview
        self.tree = ttk.Treeview(
            self,
            columns=(
                "ID",
                "Name",
                "Duration",
                "Artist name",
            ),
            show="headings",
        )
        self.tree.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Configure columns
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Duration", text="Duration")
        self.tree.heading("Artist name", text="Artist name")  # Changed heading text

        # Configure column widths
        self.tree.column("ID", width=50)
        self.tree.column("Name", width=200)
        self.tree.column("Duration", width=50)
        self.tree.column("Artist name", width=150)  # Increased width for artist name

        # Create button frame
        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0, columnspan=2, pady=5)

        # Refresh button
        refresh_button = ttk.Button(
            button_frame, text="Refresh", command=self.refresh_tracks
        )
        refresh_button.pack(side="left", padx=2)

        # Delete button
        delete_button = ttk.Button(
            button_frame, text="Delete Track", command=self.delete_track
        )
        delete_button.pack(side="left", padx=2)

        # Initial population of the tree
        self.refresh_tracks()

    def refresh_tracks(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add all tracks to the tree

        for n, track in self._track_controller._track.items():
            # Get artist name from artist controller
            # artist_name = (self._artist_controller._artists.get(track._artist_id)

            # Get artist name from artist controller
            artist_name = "Unknown"  # Default value
            artist = self._artist_controller._artists.get(track._artist_id)
            if artist:
                artist_name = artist._name

            # Convert duration to MM:SS format
            duration_display = seconds_to_minutes_seconds(track._duration_seconds)

            self.tree.insert(
                "",
                "end",
                values=(
                    track._id,
                    track._name,
                    duration_display,  # Display MM:SS format
                    artist_name,  # Display artist name instead of ID
                ),
            )

    def delete_track(self):
        # Get the selected item
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a track to delete")

        # Get the track ID
        track_id = self.tree.item(selected_item, "values")[0]

        # Show confirmation dialog
        confirm = messagebox.askyesno(
            "Delete track", "Are you sure you want to delete this track?"
        )

        if not confirm:
            return

        # Delete the track
        try:
            self._track_controller.delete_track(track_id)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        # Refresh the tree
        self.refresh_tracks()
