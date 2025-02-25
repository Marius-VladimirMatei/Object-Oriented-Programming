import tkinter as tk
from tkinter import ttk, messagebox
from src.models.album import Album
from src.controllers.album_controller import AlbumController
from src.controllers.track_controller import TrackController


class CreateAlbumDialog(tk.Toplevel):
    def __init__(
        self,
        parent,
        album_controller: AlbumController,
        track_controller: TrackController,
        refresh_callback,
    ):
        super().__init__(parent)
        self.title("Create New Album")
        self.album_controller = album_controller
        self.track_controller = track_controller
        self.refresh_callback = refresh_callback

        # Create entry fields
        ttk.Label(self, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.id_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.name_var).grid(
            row=1, column=1, padx=5, pady=5
        )

        ttk.Label(self, text="Year:").grid(row=2, column=0, padx=5, pady=5)
        self.year_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.year_var).grid(
            row=2, column=1, padx=5, pady=5
        )

        ttk.Label(self, text="Artist ID:").grid(row=3, column=0, padx=5, pady=5)
        self.artist_id_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.artist_id_var).grid(
            row=3, column=1, padx=5, pady=5
        )

        # Create track selection listbox
        ttk.Label(self, text="Select Tracks:").grid(
            row=4, column=0, columnspan=2, padx=5, pady=5
        )
        self.track_listbox = tk.Listbox(self, selectmode=tk.MULTIPLE, height=10)
        self.track_listbox.grid(
            row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew"
        )

        # Populate track listbox
        for track_id, track in self.track_controller._track.items():
            self.track_listbox.insert(tk.END, f"{track._id}: {track._name}")

        # Create buttons
        ttk.Button(self, text="Create Album", command=self._create_album).grid(
            row=6, column=0, columnspan=2, pady=10
        )

    def _create_album(self):
        try:
            # Create new album

            # Get selected tracks
            selected_indices = self.track_listbox.curselection()
            selected_tracks = [
                self.track_listbox.get(i).split(":")[0] for i in selected_indices
            ]

            album = Album(
                self.id_var.get(),
                self.name_var.get(),
                int(self.year_var.get()),
                self.artist_id_var.get(),
                selected_tracks,
            )

            # Add album to controller
            self.album_controller.add_album(album)

            # Update the view
            self.refresh_callback()

            messagebox.showinfo("Success", "Album created successfully!")
            self.destroy()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
