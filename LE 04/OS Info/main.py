import tkinter as tk
from src.views.system_view import SystemView


def main():
    """Main entry point for the application."""
    # Create root window
    root = tk.Tk()
    root.title("System Information Monitor")
    root.geometry("800x600")

    # Create application
    app = SystemView(root)

    # Start main event loop
    root.mainloop()


if __name__ == "__main__":
    main()
