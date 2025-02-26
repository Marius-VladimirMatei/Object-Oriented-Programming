import csv
from datetime import datetime
from tkinter import filedialog


class DataExporter:
    # Class responsible for exporting data to a CSV file.

    @staticmethod
    def export_to_csv(data, is_selected_callback):
        # Export the list of selected data rows to CSV file.

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
                writer.writerow(["System Information:"])

                # Filter data based on selection, check if a metric is selected, using the callback
                for item in data:
                    metric_name = item[0]
                    if is_selected_callback(metric_name):
                        writer.writerow(item)

            return True
        except Exception as e:
            print(f"Export error: {str(e)}")
            return False
