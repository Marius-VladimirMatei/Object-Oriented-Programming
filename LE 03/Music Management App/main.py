import tkinter as tk
from tkinter import ttk, messagebox
from src.views.music_manager_view import MusicManagerView


def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Music Management App")

    app = MusicManagerView(root)
    app.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
