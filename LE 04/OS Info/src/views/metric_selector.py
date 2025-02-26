import tkinter as tk
from tkinter import ttk


class MetricSelector:
    """
    Component for selecting metrics to export.
    """

    def __init__(self, parent):
        """
        Initialize the MetricSelector.

        Args:
            parent: Parent widget
        """
        # Create selection frame
        self.frame = ttk.LabelFrame(parent, text="Select Metrics to Export")

        # Create selection variables and checkboxes
        self.selected_metrics = {}
        metrics_frame = ttk.Frame(self.frame)
        metrics_frame.pack(fill="x", padx=10, pady=5)

        # Create columns for organization
        col1 = ttk.Frame(metrics_frame)
        col2 = ttk.Frame(metrics_frame)
        col1.pack(side=tk.LEFT, fill="y", expand=True)
        col2.pack(side=tk.LEFT, fill="y", expand=True)

        # System info metrics (first column)
        system_metrics = ["OS", "System Uptime", "Python Version", "CPU Cores"]
        for metric in system_metrics:
            var = tk.BooleanVar(value=True)
            self.selected_metrics[metric] = var
            ttk.Checkbutton(col1, text=metric, variable=var).pack(anchor="w")

        # Performance metrics (second column)
        performance_metrics = [
            "CPU Frequency",
            "CPU Usage",
            "Total Disk Space",
            "Disk Usage",
        ]
        for metric in performance_metrics:
            var = tk.BooleanVar(value=True)
            self.selected_metrics[metric] = var
            ttk.Checkbutton(col2, text=metric, variable=var).pack(anchor="w")

        # Select All / Deselect All buttons
        select_buttons = ttk.Frame(self.frame)
        select_buttons.pack(fill="x", padx=10, pady=5)
        ttk.Button(select_buttons, text="Select All", command=self.select_all).pack(
            side=tk.LEFT, padx=5
        )
        ttk.Button(select_buttons, text="Deselect All", command=self.deselect_all).pack(
            side=tk.LEFT, padx=5
        )

    def select_all(self):
        """Select all metrics."""
        for var in self.selected_metrics.values():
            var.set(True)

    def deselect_all(self):
        """Deselect all metrics."""
        for var in self.selected_metrics.values():
            var.set(False)

    def is_selected(self, metric_name):
        """
        Check if a metric is selected.

        Args:
            metric_name (str): Name of the metric

        Returns:
            bool: True if selected, False otherwise
        """
        return (
            metric_name in self.selected_metrics
            and self.selected_metrics[metric_name].get()
        )
