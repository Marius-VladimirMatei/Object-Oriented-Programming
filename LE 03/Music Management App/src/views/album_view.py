import tkinter as tk
from tkinter import ttk, messagebox
from src.controllers.album_controller import AlbumController
from src.models.album import Album
from src.controllers.track_controller import TrackController
from src.views.create_album_dialog_box import CreateAlbumDialog
from src.controllers.artist_controller import ArtistController
from src.utils.time_utils import seconds_to_minutes_seconds


class AlbumView(tk.Frame):
    def __init__(
        self,
        parent: tk.Tk,
        album_controller: AlbumController,
        track_controller: TrackController,
        artist_controller: ArtistController,
    ):
        super().__init__(parent)
        self._album_controller = album_controller
        self._track_controller = track_controller
        self._artist_controller = artist_controller

        # Configure the frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)  # Add weight for tracks treeview

        # Create Albums Treeview
        self.albums_tree = ttk.Treeview(
            self,
            columns=("ID", "Name", "Year", "Artist name", "Total Time"),
            show="headings",
        )
        self.albums_tree.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Add scrollbar for albums
        albums_scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.albums_tree.yview
        )
        albums_scrollbar.grid(row=0, column=1, sticky="ns")
        self.albums_tree.configure(yscrollcommand=albums_scrollbar.set)

        # Configure albums columns
        self.albums_tree.heading("ID", text="ID")
        self.albums_tree.heading("Name", text="Name")
        self.albums_tree.heading("Year", text="Year")
        self.albums_tree.heading("Artist name", text="Artist name")
        self.albums_tree.heading("Total Time", text="Total Time")

        # Configure album column widths
        self.albums_tree.column("ID", width=50)
        self.albums_tree.column("Name", width=200)
        self.albums_tree.column("Year", width=50)
        self.albums_tree.column("Artist name", width=150)
        self.albums_tree.column("Total Time", width=100)

        # Create Tracks Treeview
        self.tracks_tree = ttk.Treeview(
            self,
            columns=("ID", "Name", "Duration", "Artist name"),
            show="headings",
        )
        self.tracks_tree.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # Add scrollbar for tracks
        tracks_scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.tracks_tree.yview
        )
        tracks_scrollbar.grid(row=1, column=1, sticky="ns")
        self.tracks_tree.configure(yscrollcommand=tracks_scrollbar.set)

        # Configure tracks columns
        self.tracks_tree.heading("ID", text="ID")
        self.tracks_tree.heading("Name", text="Name")
        self.tracks_tree.heading("Duration", text="Duration")
        self.tracks_tree.heading("Artist name", text="Artist name")

        # Configure track column widths
        self.tracks_tree.column("ID", width=50)
        self.tracks_tree.column("Name", width=200)
        self.tracks_tree.column("Duration", width=50)
        self.tracks_tree.column("Artist name", width=50)

        # Buttons frame
        button_frame = ttk.Frame(self)
        button_frame.grid(row=2, column=0, columnspan=2, pady=5)

        # Center the button frame
        self.columnconfigure(0, weight=1)
        button_frame.grid_configure(sticky="ew")
        button_frame.grid_columnconfigure(0, weight=1)

        # Create inner frame for buttons
        inner_button_frame = ttk.Frame(button_frame)
        inner_button_frame.grid(row=0, column=0)

        # Refresh button
        refresh_button = ttk.Button(
            inner_button_frame, text="Refresh", command=self.refresh_albums
        )
        refresh_button.pack(side=tk.LEFT, padx=5)

        # Create Album button
        create_button = ttk.Button(
            inner_button_frame, text="Create Album", command=self._show_create_dialog
        )
        create_button.pack(side=tk.LEFT, padx=5)

        # Delete Album button
        delete_button = ttk.Button(
            inner_button_frame, text="Delete Album", command=self.delete_album
        )
        delete_button.pack(side=tk.LEFT, padx=5)

        # Bind selection event
        self.albums_tree.bind("<<TreeviewSelect>>", self._on_album_selected)

        # Initial population of the tree
        self.refresh_albums()

    def _on_album_selected(self, event):
        selected_items = self.albums_tree.selection()
        if not selected_items:
            return

        # Clear existing tracks
        for item in self.tracks_tree.get_children():
            self.tracks_tree.delete(item)

        # Get selected album ID
        album_id = self.albums_tree.item(selected_items[0])["values"][0]
        a = self._album_controller._albums[str(album_id)]

        # for each track id in a._track_list
        # get track from track_controller
        # insert track into tracks_tree

        for track_id in a._track_list:
            # Skip if track doesn't exist anymore
            if str(track_id) not in self._track_controller._track:
                continue

            track = self._track_controller._track[str(track_id)]
            # Get artist name
            artist_name = "Unknown"
            artist = self._artist_controller._artists.get(track._artist_id)
            if artist:
                artist_name = artist._name

            # Converts duration to minutes and seconds
            duration_display = seconds_to_minutes_seconds(track._duration_seconds)
            self.tracks_tree.insert(
                "",
                "end",
                values=(
                    track._id,
                    track._name,
                    duration_display,  # Display duration in MM:SS format
                    artist_name,
                ),
            )

    def refresh_albums(self):
        # Clear existing items in both trees
        for item in self.albums_tree.get_children():
            self.albums_tree.delete(item)
        for item in self.tracks_tree.get_children():
            self.tracks_tree.delete(item)

        # Add all albums to the tree
        for album_id, album in self._album_controller._albums.items():
            # Calculate total time for album
            total_seconds = 0
            for track_id in album._track_list:
                track = self._track_controller._track.get(str(track_id))
                if track:
                    total_seconds += track._duration_seconds

            # Format total time
            total_time_display = seconds_to_minutes_seconds(total_seconds)

            # Get artist name from artist controller
            artist_name = "Unknown"  # Default value
            artist = self._artist_controller._artists.get(album._artist_id)
            if artist:
                artist_name = artist._name

            self.albums_tree.insert(
                "",
                "end",
                values=(
                    album._id,
                    album._name,
                    album._year,
                    artist_name,
                    total_time_display,
                ),
            )

    def _show_create_dialog(self):
        dialog = CreateAlbumDialog(
            self, self._album_controller, self._track_controller, self.refresh_albums
        )
        dialog.grab_set()  # Make the dialog modal - window stays on top until completion or dissmissed

    def delete_album(self):
        # Get the selected item
        selected_items = self.albums_tree.selection()
        if not selected_items:
            messagebox.showerror("Error", "Please select an album to delete.")
            return

        # Get the album ID
        album_id = self.albums_tree.item(selected_items, "values")[0]

        # Show confirmation dialog
        confirm = messagebox.askyesno(
            "Delete Album", "Are you sure you want to delete this album?"
        )

        if not confirm:
            return

        # Delete the album
        try:
            self._album_controller.delete_album(album_id)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        # Refresh the tree
        self.refresh_albums()
