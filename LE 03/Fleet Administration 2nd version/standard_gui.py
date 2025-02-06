import tkinter as tk
from tkinter import ttk
from vehicle_data_base import Vehicle_Data_Base
from car import Car
from cargo_truck import Cargo_truck
from motorcycle import Motorcycle
from bicycle import Bicycle



# Update the second dropdown based on the first selection
def update_vehicle_options(event):
    selected_type = vehicle_type_var.get()
    vehicle_dropdown['values'] = motorized_vehicles if selected_type == "Motorized" else non_motorized_vehicles
    vehicle_var.set(vehicle_dropdown['values'][0])  # Set default value
    update_vehicle_fields(None)  # Update fields


# Display additional fields based on vehicle selection
def update_vehicle_fields(event):
    for widget in vehicle_fields_frame.winfo_children():
        widget.destroy()  # Clear previous fields

    labels = []
    if vehicle_var.get() == "Car":
        labels = ["ID", "License Plate", "Brand", "Model", "Year", "Mileage", "Fuel Type", "Fuel Level",
                  "Number of Doors"]
    elif vehicle_var.get() == "Cargo truck":
        labels = ["ID", "License Plate", "Brand", "Model", "Year", "Mileage", "Fuel Type", "Fuel Level", "Current Load",
                  "Max Load"]
    elif vehicle_var.get() == "Motorcycle":
        labels = ["ID", "License Plate", "Brand", "Model", "Year", "Mileage", "Fuel Type", "Fuel Level"]
    elif vehicle_var.get() == "Bicycle":
        labels = ["ID", "Brand", "Model", "Year", "Type", "Gear Count"]

    entries = {}
    for label in labels:
        tk.Label(vehicle_fields_frame, text=label).pack(anchor="w")
        entry = tk.Entry(vehicle_fields_frame)
        entry.pack(fill="x", pady=2)
        entries[label] = entry


# Open a new window for refueling
def open_refuel_window():
    refuel_window = tk.Toplevel(root)
    refuel_window.title("Refuel Vehicle")
    refuel_window.geometry("400x300")
    label = tk.Label(refuel_window, text="Refueling in progress...", font=("Arial", 14))
    label.pack(pady=20)


# Main application window
root = tk.Tk()
root.title("Vehicle Selector")
root.geometry("1000x800")

# Vehicle type selection
vehicle_type_var = tk.StringVar()
vehicle_type_dropdown = ttk.Combobox(root, textvariable=vehicle_type_var, state="readonly")
vehicle_type_dropdown['values'] = ("Motorized", "NonMotorized")
vehicle_type_dropdown.current(0)
vehicle_type_dropdown.pack(pady=10)

# Vehicle selection
motorized_vehicles = ("Car", "Cargo truck", "Motorcycle")
non_motorized_vehicles = ("Bicycle",)
vehicle_var = tk.StringVar()
vehicle_dropdown = ttk.Combobox(root, textvariable=vehicle_var, state="readonly")
vehicle_dropdown.pack(pady=10)

# Buttons
save_button = tk.Button(root, text="Add Vehicle", command=lambda: print("Vehicle added!"))
save_button.pack(pady=10)

show_all_button = tk.Button(root, text="Show ALL Vehicles")
show_all_button.pack(pady=10)

refuel_button = tk.Button(root, text="Refuel Vehicle", command=open_refuel_window)
refuel_button.pack(pady=10)

# Frame for vehicle-specific fields
vehicle_fields_frame = tk.Frame(root)
vehicle_fields_frame.pack(pady=10, fill="x")

# List box to display vehicle entries
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10, fill="both", expand=True)

vehicle_listbox = tk.Listbox(listbox_frame)
vehicle_listbox.pack(fill="both", expand=True, padx=10, pady=10)

# Set initial options
update_vehicle_options(None)
vehicle_type_dropdown.bind("<<ComboboxSelected>>", update_vehicle_options)
vehicle_dropdown.bind("<<ComboboxSelected>>", update_vehicle_fields)

root.mainloop()
