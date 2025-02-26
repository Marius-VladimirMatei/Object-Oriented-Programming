import platform
import psutil
import sys
import time
from src.models.system_metric import SystemMetric
from src.utils.data_exporter import DataExporter


class SystemController:
    # Controller class responsible for gathering system information and handling data operations.

    def get_system_metrics(self):
        # Get current system metrics and returns a list of SystemMetric objects

        metrics = []

        # Collect metrics from each category
        metrics.extend(self._get_system_info())
        metrics.extend(self._get_python_info())
        metrics.extend(self._get_cpu_info())
        metrics.extend(self._get_memory_info())
        metrics.extend(self._get_disk_info())

        return metrics

        # All helper functions below are meant to be called by get_system_metrics and organize the metrics into logical groups.

    def _get_system_info(self):
        # Basic system information metrics.

        metrics = []
        metrics.append(SystemMetric("OS", platform.platform()))
        metrics.append(SystemMetric("System Uptime", self._get_uptime()))
        metrics.append(
            SystemMetric("Platform", f"{platform.system()} {platform.release()}")
        )
        metrics.append(SystemMetric("Architecture", platform.machine()))

        return metrics

    def _get_python_info(self):
        # Python-related metrics.

        metrics = []
        metrics.append(SystemMetric("Python Version", platform.python_version()))
        metrics.append(SystemMetric("Python Path", sys.executable))
        metrics.append(SystemMetric("Python Implementation", sys.implementation.name))
        metrics.append(SystemMetric("Python Version (Full)", sys.version))

        return metrics

    def _get_cpu_info(self):
        # CPU-related metrics.

        metrics = []
        cpu_freq = psutil.cpu_freq()
        cpu_count = psutil.cpu_count()
        cpu_usage = psutil.cpu_percent(interval=None)

        metrics.append(SystemMetric("CPU Cores", f"{cpu_count} cores"))
        if cpu_freq:
            metrics.append(SystemMetric("CPU Frequency", f"{cpu_freq.current:.1f} MHz"))
        metrics.append(SystemMetric("CPU Usage", f"{cpu_usage:.1f}%"))

        return metrics

    def _get_memory_info(self):
        # Memory-related metrics.

        metrics = []

        # Get virtual memory information - converted to Gb (1024*1024*1024)
        virtual_mem = psutil.virtual_memory()
        total_ram_gb = virtual_mem.total / (1024**3)
        available_ram_gb = virtual_mem.available / (1024**3)
        used_ram_gb = virtual_mem.used / (1024**3)

        # Get swap memory information
        swap_mem = psutil.swap_memory()
        total_swap_gb = swap_mem.total / (1024**3)
        used_swap_gb = swap_mem.used / (1024**3)

        # Add metrics
        metrics.append(SystemMetric("Total RAM", f"{total_ram_gb:.2f} GB"))
        metrics.append(SystemMetric("Available RAM", f"{available_ram_gb:.2f} GB"))
        metrics.append(SystemMetric("Used RAM", f"{used_ram_gb:.2f} GB"))
        metrics.append(SystemMetric("RAM Usage", f"{virtual_mem.percent}%"))

        # Add swap metrics if swap exists
        if total_swap_gb > 0:
            metrics.append(SystemMetric("Total Swap", f"{total_swap_gb:.2f} GB"))
            metrics.append(SystemMetric("Used Swap", f"{used_swap_gb:.2f} GB"))
            metrics.append(SystemMetric("Swap Usage", f"{swap_mem.percent}%"))

        return metrics

    def _get_disk_info(self):
        # Disk-related metrics.

        metrics = []
        disk = psutil.disk_usage("/")
        total_disk_gb = disk.total / (1024**3)

        metrics.append(SystemMetric("Total Disk Space", f"{total_disk_gb:.1f} GB"))
        metrics.append(SystemMetric("Disk Usage", f"{disk.percent}%"))
        metrics.append(
            SystemMetric("Free Disk Space", f"{disk.free / (1024**3):.1f} GB")
        )

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
        # Export system information to a CSV file.

        # Export data using the DataExporter utility
        DataExporter.export_to_csv(data, is_selected_callback)
