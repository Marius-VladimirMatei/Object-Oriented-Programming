import tkinter as tk

from src.controllers.system_controller import SystemController
from src.views.info_panel import SystemInfoPanel
from src.views.metric_selector import MetricSelector
from src.views.control_panel import ControlPanel

# Main application view that integrates all UI components.


class SystemView(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)

        # Configure the frame to be responsive
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)  # For system info content
        self.rowconfigure(1, weight=0)  # For metrics selection
        self.rowconfigure(2, weight=0)  # For buttons
        self.pack(expand=True, fill="both", padx=10, pady=10)

        # Create controller
        self.controller = SystemController()

        # Create UI components using composition
        self.system_info = SystemInfoPanel(self)
        self.system_info.frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.metric_selector = MetricSelector(self)
        self.metric_selector.frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.control_panel = ControlPanel(self, self.export_data)
        self.control_panel.frame.grid(row=2, column=0, sticky="ew", pady=10)

        # Initial data load
        self.refresh_metrics()

        # Start automatic updates
        self.schedule_update()

    def refresh_metrics(self):
        # Update metrics displayed in the system info panel
        metrics = self.controller.get_system_metrics()

        self.system_info.update_metrics(metrics)

    def schedule_update(self):
        #   Schedule periodic updates
        self.refresh_metrics()
        self.after(1000, self.schedule_update)

    def export_data(self):
        # Export selected system information to a CSV file
        # Get data from the system info panel
        data = self.system_info.get_all_data()

        # Pass data and selection function to controller and export using the controller
        self.controller.export_data(data, self.metric_selector.is_selected)
