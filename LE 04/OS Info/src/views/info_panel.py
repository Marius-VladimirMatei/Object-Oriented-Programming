import tkinter as tk
from tkinter import ttk


class SystemInfoPanel:
    """
    Component for displaying system information in a treeview.
    """

    def __init__(self, parent):
        """
        Initialize the SystemInfoPanel.

        Args:
            parent: Parent widget
        """
        # Create content frame for data display
        self.frame = ttk.LabelFrame(parent, text="System Information")

        # Configure the frame
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # Create treeview for data display
        columns = ("Metric", "Value")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        # Configure columns
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "Metric":
                self.tree.column(col, width=250, minwidth=150)
            elif col == "Value":
                self.tree.column(col, width=350, minwidth=200)

        # Add scrollbar
        self.scrollbar = ttk.Scrollbar(
            self.frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Arrange components
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

    def update_metrics(self, metrics):
        """
        Update the metrics displayed in the treeview.

        Args:
            metrics (list): List of SystemMetric objects
        """
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add data to treeview
        for metric in metrics:
            self.tree.insert("", "end", values=(metric.name, metric.value))

    def get_all_data(self):
        """
        Get all data currently in the treeview.

        Returns:
            list: List of [metric_name, value] pairs
        """
        data = []
        for item_id in self.tree.get_children():
            values = self.tree.item(item_id, "values")
            data.append([values[0], values[1]])
        return data
