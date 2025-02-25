from src.models.artist import Artist
import tkinter as tk
from tkinter import ttk, messagebox
from src.controllers.artist_controller import ArtistController


class ArtistView(tk.Frame):
    def __init__(self, parent: tk.Tk, artist_controller: ArtistController):
        super().__init__(parent)
        self._artist_controller = artist_controller

        # Configure the frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Create Treeview
        self.tree = ttk.Treeview(self, columns=("ID", "Name"), show="headings")
        self.tree.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Configure columns
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")

        # Configure column widths
        self.tree.column("ID", width=5)
        self.tree.column("Name", width=200)

        # Create button frame
        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0, columnspan=2, pady=5)

        # Refresh button
        refresh_button = ttk.Button(
            button_frame, text="Refresh", command=self.refresh_artists
        )
        refresh_button.pack(side="left", padx=2)

        # Delete button
        delete_button = ttk.Button(
            button_frame, text="Delete Artist", command=self.delete_artist
        )
        delete_button.pack(side="left", padx=2)

        # Initial population of the tree
        self.refresh_artists()

    def refresh_artists(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add all artists to the tree
        for n, artist in self._artist_controller._artists.items():
            self.tree.insert("", "end", values=(artist._id, artist._name))

    def delete_artist(self):
        # Get the selected item
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an artist to delete.")
            return

        # Get the artist ID
        artist_id = self.tree.item(selected_item, "values")[0]

        # Delete the artist
        try:
            self._artist_controller.delete_artist(artist_id)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        # Refresh the tree
        self.refresh_artists()
