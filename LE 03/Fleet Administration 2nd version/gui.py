import tkinter as tk
from tkinter import messagebox, ttk
from vehicle_data_base import Vehicle_Data_Base
from car import Car
from cargo_truck import Cargo_truck
from motorcycle import Motorcycle
from bicycle import Bicycle

db = Vehicle_Data_Base()
db.load_vehicles()



class FleetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fleet Management System")
        self.root.geometry("900x1200")
        self.root.resizable(True, True)


        # Category Selection
        tk.Label(root, text="Select Vehicle Category:").pack()
        self.category = tk.StringVar(value="Motorized")
        self.category_menu = tk.OptionMenu(root, self.category, "Motorized", "Non-Motorized", command=self.update_vehicle_menu)
        self.category_menu.pack()


        # Vehicle Type Selection
        tk.Label(root, text="Vehicle Type:").pack()
        self.vehicle_type = tk.StringVar(value="Car")
        self.vehicle_menu = tk.OptionMenu(root, self.vehicle_type, "Car", "Truck", "Motorcycle", "Bicycle", command=self.update_vehicle_fields)
        self.vehicle_menu.pack()


        self.vehicle_fields_frame = tk.Frame(root)
        self.vehicle_fields_frame.pack(pady=10, fill="x")

        # Buttons
        tk.Button(root, text="Add Vehicle", command=self.add_vehicle, width=20, height=2).pack(pady=5)
        tk.Button(root, text="List Vehicles", command=self.list_vehicles, width=20, height=2).pack(pady=5)
        tk.Button(root, text="Refuel Vehicle", command=self.open_refuel_window, width=20, height=2).pack(pady=5)
        tk.Button(root, text="Show Fuel Summary", command=self.calculate_fuel_totals, width=20, height=2).pack(pady=5)

        # Listbox to display all data
        tk.Label(root, text="Fleet Vehicles Output:").pack()
        self.vehicle_listbox = tk.Listbox(root, width=10, height=50)
        self.vehicle_listbox.pack(pady=40, padx=10, fill="both", expand=True)

        self.entries = {}  # Store input fields
        self.update_vehicle_menu("Motorized")
        self.update_vehicle_fields("Car")  # Ensure initial fields are loaded
        self.list_vehicles()


    # vehicle menu
    def update_vehicle_menu(self, selected_category):
        menu = self.vehicle_menu["menu"]
        menu.delete(0, "end")
        motorized = ["Car", "Truck", "Motorcycle"]
        non_motorized = ["Bicycle"]
        options = motorized if selected_category == "Motorized" else non_motorized

        self.vehicle_type.set(options[0])  # Ensure first option is selected
        for option in options:
            menu.add_command(label=option,
                             command=lambda value=option: self.vehicle_type.set(value) or self.update_vehicle_fields(
                                 value))

        self.update_vehicle_fields(options[0])  # Ensure the first option is updated correctly


    # proper input fields by type
    def update_vehicle_fields(self, vehicle_type=None):

        for widget in self.vehicle_fields_frame.winfo_children():
            widget.destroy()  # Clear previous fields

        self.entries = {}  # Reset input fields dictionary

        if vehicle_type is None:
            vehicle_type = self.vehicle_type.get()

        vehicle_fields = {
            "Car": ["ID", "License Plate", "Brand", "Model", "Year", "Mileage", "Fuel Type", "Fuel Level",
                    "Number of Doors"],
            "Truck": ["ID", "License Plate", "Brand", "Model", "Year", "Mileage", "Fuel Type", "Fuel Level",
                      "Current Load", "Max Load"],
            "Motorcycle": ["ID", "License Plate", "Brand", "Model", "Year", "Mileage", "Fuel Type", "Fuel Level"],
            "Bicycle": ["ID", "Brand", "Model", "Year", "Type", "Gear Count"]
        }

        if vehicle_type not in vehicle_fields:
            return

        for label in vehicle_fields[vehicle_type]:
            tk.Label(self.vehicle_fields_frame, text=label, anchor="center").pack(side="top", fill="both", padx=170, pady=1)

            if label == "Fuel Type":
                fuel_types = ("Petrol", "Diesel", "Electric")
                fuel_var = tk.StringVar()
                fuel_dropdown = ttk.Combobox(self.vehicle_fields_frame, textvariable=fuel_var, state="readonly",
                                             width=40)
                fuel_dropdown['values'] = fuel_types
                fuel_dropdown.current(0)
                fuel_dropdown.pack(pady=2, padx=5)  # Keeps input field centered
                self.entries[label] = fuel_var
            else:
                entry = tk.Entry(self.vehicle_fields_frame, width=50)
                entry.pack(pady=2, padx=5)  # Keeps input field centered
                self.entries[label] = entry


    # Add new vehicle to db
    def add_vehicle(self):
        vehicle_id = self.entries["ID"].get()
        brand = self.entries.get("Brand", tk.StringVar()).get()
        model = self.entries.get("Model", tk.StringVar()).get()
        year = self.entries.get("Year", tk.StringVar()).get()
        vehicle_type = self.vehicle_type.get()

        try:
            year = int(year)  # Ensure year is an integer
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Make sure year is a number.")
            return

        # Motorized vehicles have mileage and fuel level
        mileage = fuel_type = fuel_level = 0  # Default values for non-motorized vehicles
        if vehicle_type in ["Car", "Truck", "Motorcycle"]:
            mileage = self.entries.get("Mileage", tk.StringVar()).get()
            fuel_type = self.entries.get("Fuel Type", tk.StringVar()).get()
            fuel_level = self.entries.get("Fuel Level", tk.StringVar()).get()

            try:
                mileage = int(mileage)  # Convert mileage to integer
                fuel_level = float(fuel_level) if fuel_type != "None" else 0  # Convert fuel level to float
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Make sure mileage and fuel level are numbers.")
                return

        # Create appropriate vehicle object
        if vehicle_type == "Truck":
            current_load = self.entries.get("Current Load", tk.StringVar()).get()
            max_load = self.entries.get("Max Load", tk.StringVar()).get()
            try:
                current_load = int(current_load)
                max_load = int(max_load)
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Make sure 'Current Load' and 'Max Load' are numbers.")
                return
            vehicle = Cargo_truck(vehicle_id, "", brand, model, year, mileage, fuel_type, fuel_level, current_load,
                                  max_load)

        elif vehicle_type == "Car":
            doors = self.entries.get("Number of Doors", tk.StringVar()).get()
            try:
                doors = int(doors)
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Make sure 'Number of Doors' is a number.")
                return
            vehicle = Car(vehicle_id, "", brand, model, year, mileage, fuel_type, fuel_level, doors)

        elif vehicle_type == "Motorcycle":
            vehicle = Motorcycle(vehicle_id, "", brand, model, year, mileage, fuel_type, fuel_level)

        else:  # Bicycle case
            gear_count = self.entries.get("Gear Count", tk.StringVar()).get()
            try:
                gear_count = int(gear_count)
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Make sure 'Gear Count' is a number.")
                return
            vehicle = Bicycle(vehicle_id, brand, model, year, "Bicycle", gear_count)

        db.add_vehicle(vehicle)
        db.save_vehicle()
        self.list_vehicles()
        messagebox.showinfo("Success", f"{vehicle_type} added successfully!")

        # **Clear input fields after adding a vehicle**
        for entry in self.entries.values():
            if isinstance(entry, tk.Entry):
                entry.delete(0, tk.END)
            elif isinstance(entry, tk.StringVar):
                entry.set("")  # Clear dropdown selections

        messagebox.showinfo("Success", f"{vehicle_type} added successfully!")


    # new windown for refuel
    def open_refuel_window(self):

        self.refuel_window = tk.Toplevel(self.root)
        self.refuel_window.title("Refuel Vehicle")
        self.refuel_window.geometry("300x200")

        tk.Label(self.refuel_window, text="Select Vehicle ID:").pack()

        self.selected_vehicle_id = tk.StringVar()

        # Get vehicle IDs for motorized vehicles only
        vehicle_ids = [v.id for v in db.vehicles if hasattr(v, 'fuel_level')]

        if not vehicle_ids:
            messagebox.showwarning("No Vehicles", "No motorized vehicles available for refueling.")
            self.refuel_window.destroy()
            return

        # Dropdown for selecting vehicle ID
        self.vehicle_menu_refuel = ttk.Combobox(self.refuel_window, textvariable=self.selected_vehicle_id,
                                                state="readonly")
        self.vehicle_menu_refuel['values'] = vehicle_ids
        self.vehicle_menu_refuel.pack(pady=5)

        if vehicle_ids:
            self.selected_vehicle_id.set(vehicle_ids[0])  # Select first vehicle by default

        tk.Label(self.refuel_window, text="Enter Fuel Amount (L):").pack()
        self.fuel_amount_entry = tk.Entry(self.refuel_window)
        self.fuel_amount_entry.pack(pady=5)

        tk.Button(self.refuel_window, text="Refuel", command=self.refuel_vehicle).pack(pady=10)


    # Refuel by selected id
    def refuel_vehicle(self):

        vehicle_id = self.selected_vehicle_id.get()

        if not vehicle_id:
            messagebox.showerror("Error", "Please select a vehicle.")
            return

        try:
            fuel_amount = float(self.fuel_amount_entry.get())
            if fuel_amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number.")
            return

        # Find the vehicle and update its fuel level
        for vehicle in db.vehicles:
            if vehicle.id == int(vehicle_id):  # Convert to integer for comparison
                if hasattr(vehicle, "fuel_level"):
                    vehicle.refuel(fuel_amount)  # Use the built-in method
                    messagebox.showinfo("Success", f"Refueled {fuel_amount}L. New Level: {vehicle.fuel_level}L")
                    db.save_vehicle()
                    self.list_vehicles()
                    self.refuel_window.destroy()
                    return

        messagebox.showerror("Error", "Vehicle not found or fuel level not available.")

    # Fuel by type
    def calculate_fuel_totals(self):
        fuel_totals = db.calculate_fuel_totals()  # Get fuel totals

        if not fuel_totals:
            messagebox.showinfo("Fuel Summary", "No fuel data available.")
            return

        summary = ""
        for fuel, amount in fuel_totals.items():
            summary += f"{fuel}: {amount} liters\n"

        messagebox.showinfo("Fuel Summary", f"Total Fuel Breakdown:\n{summary}")




    def list_vehicles(self):
        # Display list of vehicles
        self.vehicle_listbox.delete(0, tk.END)
        db.list_vehicles(self.vehicle_listbox)



root = tk.Tk()
app = FleetApp(root)
root.mainloop()
