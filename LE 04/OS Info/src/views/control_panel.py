import tkinter as tk
from tkinter import ttk


class ControlPanel:
    # Section designed for control buttons.

    def __init__(self, parent, export_callback):
        self.frame = ttk.Frame(parent)

        # Store callback
        self.export_callback = export_callback

        # Add Export button
        ttk.Button(self.frame, text="Export Data", command=self.export_callback).pack(
            side=tk.LEFT, padx=5
        )
