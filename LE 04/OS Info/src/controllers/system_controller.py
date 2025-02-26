import platform
import psutil
import sys
import time
import csv
from datetime import datetime
from tkinter import filedialog
from src.models.system_metric import SystemMetric


class SystemController:
    # Controller class responsible for gathering system information and handling data operations.

    def get_system_metrics(self):
        # Get current system metrics and returns a list of SystemMetric objects

        metrics = []

        # System Info
        metrics.append(SystemMetric("OS", platform.platform()))
        metrics.append(SystemMetric("System Uptime", self._get_uptime()))
        metrics.append(SystemMetric("Python Version", platform.python_version()))

        # Additional Python details using sys module
        metrics.append(SystemMetric("Python Path", sys.executable))
        metrics.append(SystemMetric("Python Implementation", sys.implementation.name))
        metrics.append(SystemMetric("Python Version (Full)", sys.version))

        # CPU Info
        cpu_freq = psutil.cpu_freq()
        cpu_count = psutil.cpu_count()
        cpu_usage = psutil.cpu_percent(interval=None)
        metrics.append(SystemMetric("CPU Cores", f"{cpu_count} cores"))
        if cpu_freq:
            metrics.append(SystemMetric("CPU Frequency", f"{cpu_freq.current:.1f} MHz"))
        metrics.append(SystemMetric("CPU Usage", f"{cpu_usage:.1f}%"))

        # Disk Info
        disk = psutil.disk_usage("/")
        total_disk_gb = disk.total / (1024**3)
        metrics.append(SystemMetric("Total Disk Space", f"{total_disk_gb:.1f} GB"))
        metrics.append(SystemMetric("Disk Usage", f"{disk.percent}%"))

        return metrics

    def _get_uptime(self):
        # Get system uptime as a formatted string and returns it

        try:
            uptime_seconds = time.time() - psutil.boot_time()
            days = int(uptime_seconds / 86400)
            hours = int((uptime_seconds % 86400) / 3600)
            minutes = int((uptime_seconds % 3600) / 60)
            return f"{days} days, {hours} hours, {minutes} minutes"
        except Exception:
            return "Unknown"

    def export_data(self, data, is_selected_callback):
        # Export the lsit of selected data rows to CSV file.

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Select file location
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        )

        if not filename:
            return False

        try:
            with open(filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)

                # Write header with timestamp
                writer.writerow(["OS Information Export"])
                writer.writerow(["Time of evaluation", timestamp])
                writer.writerow([])  # Empty row as separator

                # Write system information section
                writer.writerow(["System Information"])

                # Filter data based on selection
                # is_selected_callback - function to check if a metric is selected
                for item in data:
                    metric_name = item[0]
                    if is_selected_callback(metric_name):
                        writer.writerow(item)

            return True
        except Exception:
            return False
