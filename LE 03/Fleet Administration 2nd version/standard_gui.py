import tkinter as tk
from tkinter import ttk
from vehicle_data_base import Vehicle_Data_Base
from car import Car
from cargo_truck import Cargo_truck
from motorcycle import Motorcycle
from bicycle import Bicycle


data_base = Vehicle_Data_Base("vehicles.txt")


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
        labels = ["ID", "License Plate", "Brand", "Model", "Year", "Mileage", "Select Fuel Type", "Fuel Level",
                  "Number of Doors"]
    elif vehicle_var.get() == "Cargo truck":
        labels = ["ID", "License Plate", "Brand", "Model", "Year", "Mileage", "Select Fuel Type", "Fuel Level", "Current Load",
                  "Max Load"]
    elif vehicle_var.get() == "Motorcycle":
        labels = ["ID", "License Plate", "Brand", "Model", "Year", "Mileage", "Select Fuel Type", "Fuel Level"]
    elif vehicle_var.get() == "Bicycle":
        labels = ["ID", "Brand", "Model", "Year", "Type", "Gear Count"]

    entries = {}
    for label in labels:
        tk.Label(vehicle_fields_frame, text=label).pack(anchor="w")

        if label == "Select Fuel Type":  # Add dropdown for fuel type
            fuel_types = ("Petrol", "Diesel", "Electric")
            fuel_var = tk.StringVar()
            fuel_dropdown = ttk.Combobox(vehicle_fields_frame, textvariable=fuel_var, state="readonly")
            fuel_dropdown['values'] = fuel_types
            fuel_dropdown.current(0)  # Default selection
            fuel_dropdown.pack(fill="x", pady=2)
            entries[label] = fuel_var  # Store variable instead of entry widget
        else:
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
root.title("Vehicle Management")
root.geometry("1200x1200")

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

def create_button(text, command):
    btn = tk.Button(root, text=text, command=command, width=20)
    btn.pack(pady=5)  # `fill="x"` expands it horizontally
    return btn


create_button("Add Vehicle", lambda: print("Vehicle added!"))



# SHOW ALL VEHICLES Button !!!!!!

def show_all_vehicles():
    data_base.load_vehicles()  # Load vehicles from file
    vehicle_listbox.delete(0, tk.END)  # Clear listbox before inserting new data

    vehicle_list = data_base.list_vehicles()  # Get formatted vehicle list

    for vehicle in vehicle_list:
        vehicle_listbox.insert(tk.END, vehicle)  # Insert into GUI listbox

create_button("Show ALL Vehicles", show_all_vehicles) # Button calls the new created function

# ------------------------------------------------------------------------------------------------


data_base.load_vehicles()
create_button("Show ALL Vehicles", lambda: data_base.list_vehicles(vehicle_listbox))
 #????????????



create_button("Show Cars", None)
create_button("Show Cargo Trucks", None)
create_button("Show Motorcycles", None)
create_button("Refuel Vehicle", open_refuel_window)


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
