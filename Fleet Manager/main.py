
import tkinter as tk
from tkinter import messagebox
import os
from vehicle import Truck, Motorcycle, Bicycle, Car

class FleetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fleet Management System")
        self.root.geometry("1200x1000")
        self.root.resizable(True, True)
        self.vehicles = []
        self.file_path = "vehicles.txt"

        # Category Selection
        tk.Label(root, text="Select Vehicle Category:").pack()
        self.category = tk.StringVar(value="Motorized")
        self.category_menu = tk.OptionMenu(root, self.category, "Motorized", "Non-Motorized", command=self.update_vehicle_menu)
        self.category_menu.pack()

        # Vehicle Type Selection
        tk.Label(root, text="Vehicle Type:").pack()
        self.vehicle_type = tk.StringVar(value="Car")
        self.vehicle_menu = tk.OptionMenu(root, self.vehicle_type, "Truck", "Car", "Motorcycle", "Bicycle", command=self.update_fuel_menu)
        self.vehicle_menu.pack()

        # Fuel Type Selection
        tk.Label(root, text="Fuel Type:").pack()
        self.fuel_type = tk.StringVar(value="Petrol")
        self.fuel_menu = tk.OptionMenu(root, self.fuel_type, "Petrol", "Diesel", "Electric", "None")
        self.fuel_menu.pack()

        # Input Fields
        self.entries = {}
        fields = ["Vehicle ID", "Brand", "Model", "Year", "Mileage", "Fuel Level"]
        for field in fields:
            tk.Label(root, text=f"{field}:").pack()
            entry = tk.Entry(root)
            entry.pack()
            self.entries[field] = entry

        # Additional Fields for Specific Vehicles
        self.extra_fields = {}
        extra_fields_data = {
            "Seating Capacity (Car)": "Seating Capacity",
            "Current Cargo (Truck)": "Current Cargo",
            "Max Load (Truck)": "Max Load",
            "Engine Size (Motorcycle)": "Engine Size",
        }

        for label, key in extra_fields_data.items():
            tk.Label(root, text=label).pack()
            self.extra_fields[key] = tk.Entry(root)
            self.extra_fields[key].pack()

        # Buttons
        tk.Button(root, text="Add Vehicle", command=self.add_vehicle).pack()
        tk.Button(root, text="Refuel Vehicle", command=self.open_refuel_window).pack()

        # Vehicle Listbox
        tk.Label(root, text="Fleet Vehicles:").pack()
        self.vehicle_listbox = tk.Listbox(root, width=100, height=15)
        self.vehicle_listbox.pack()

        # Load vehicles from file on startup
        self.load_vehicles()
        self.update_vehicle_menu("Motorized")
        self.show_vehicles()


    def update_fuel_menu(self, selected_vehicle):
        """ Update the fuel type dropdown based on vehicle type. """
        menu = self.fuel_menu["menu"]
        menu.delete(0, "end")

        if selected_vehicle in ["Truck", "Car", "Motorcycle"]:
            fuel_options = ["Petrol", "Diesel", "Electric"]
            self.fuel_type.set("Petrol")  # Default selection for motorized vehicles
        else:
            fuel_options = ["None"]
            self.fuel_type.set("None")  # Default for bicycles

        for option in fuel_options:
            menu.add_command(label=option, command=lambda value=option: self.fuel_type.set(value))


    def update_vehicle_menu(self, selected_category):
        """ Update vehicle type dropdown based on the selected category. """
        menu = self.vehicle_menu["menu"]
        menu.delete(0, "end")

        motorized = ["Truck", "Car", "Motorcycle"]
        non_motorized = ["Bicycle"]
        options = motorized if selected_category == "Motorized" else non_motorized

        self.vehicle_type.set(options[0])  # Set default selection
        for option in options:
            menu.add_command(label=option, command=lambda value=option: self.vehicle_type.set(value))

        self.update_fuel_menu(self.vehicle_type.get())

    def save_vehicles(self):
        """ Save vehicles to an external text file with all relevant attributes. """
        try:
            with open(self.file_path, "w") as file:
                for vehicle in self.vehicles:
                    if isinstance(vehicle, Car):
                        file.write(
                            f"{vehicle.vehicle_id},{vehicle.brand},{vehicle.model},{vehicle.year},{vehicle.mileage},Car,{vehicle.fuel_type},{vehicle.fuel_level},{vehicle.seating_capacity}\n")
                    elif isinstance(vehicle, Truck):
                        file.write(
                            f"{vehicle.vehicle_id},{vehicle.brand},{vehicle.model},{vehicle.year},{vehicle.mileage},Truck,{vehicle.fuel_type},{vehicle.fuel_level},{vehicle.current_cargo},{vehicle.max_load}\n")
                    elif isinstance(vehicle, Motorcycle):
                        file.write(
                            f"{vehicle.vehicle_id},{vehicle.brand},{vehicle.model},{vehicle.year},{vehicle.mileage},Motorcycle,{vehicle.fuel_type},{vehicle.fuel_level},{vehicle.engine_size}\n")
                    elif isinstance(vehicle, Bicycle):
                        file.write(
                            f"{vehicle.vehicle_id},{vehicle.brand},{vehicle.model},{vehicle.year},{vehicle.mileage},Bicycle\n")
            messagebox.showinfo("Success", "Vehicles saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save vehicles: {str(e)}")

    def load_vehicles(self):
        """ Load vehicles from an external text file with proper handling. """
        if not os.path.exists(self.file_path):
            return

        try:
            self.vehicles = []
            with open(self.file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    data = line.split(',')
                    if len(data) < 6:
                        continue

                    vehicle_id, brand, model, year, mileage, vehicle_type = data[:6]
                    year = int(year)
                    mileage = float(mileage)
                    fuel_type = data[6] if len(data) > 6 and vehicle_type != "Bicycle" else None
                    fuel_level = float(data[7]) if len(data) > 7 and vehicle_type != "Bicycle" else 0

                    if vehicle_type == "Car":
                        seating_capacity = int(data[8]) if len(data) > 8 else 0
                        vehicle = Car(vehicle_id, brand, model, year, mileage, fuel_type, fuel_level, seating_capacity)
                    elif vehicle_type == "Truck":
                        if len(data) < 10:
                            print(
                                f"Warning: Truck (ID: {vehicle_id}) is missing current_cargo and max_load. Skipping entry.")
                            continue
                        try:
                            current_cargo = float(data[8])
                            max_load = float(data[9])
                            vehicle = Truck(vehicle_id, brand, model, year, mileage, fuel_type, fuel_level,
                                            current_cargo, max_load)
                        except ValueError:
                            print(
                                f"Error: Invalid number format for Truck (ID: {vehicle_id}). Ensure current_cargo and max_load are numeric. Skipping entry.")
                            continue
                    elif vehicle_type == "Motorcycle":
                        engine_size = int(data[8]) if len(data) > 8 else 0
                        vehicle = Motorcycle(vehicle_id, brand, model, year, mileage, fuel_type, fuel_level,
                                             engine_size)
                    elif vehicle_type == "Bicycle":
                        vehicle = Bicycle(vehicle_id, brand, model, year, mileage)

                    self.vehicles.append(vehicle)
            self.show_vehicles()
        except ValueError as ve:
            messagebox.showerror("Error", f"Failed to load vehicles: {str(ve)}")
        except IndexError:
            messagebox.showerror("Error",
                                 "Failed to load vehicles: Data format issue. Ensure all fields are correctly entered.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load vehicles: {str(e)}")


    def add_vehicle(self):
        """ Add a new vehicle with proper field handling """
        try:
            vehicle_id = self.entries["Vehicle ID"].get()
            brand = self.entries["Brand"].get()
            model = self.entries["Model"].get()
            year = int(self.entries["Year"].get())
            mileage = float(self.entries["Mileage"].get())
            fuel_type = self.fuel_type.get() if self.vehicle_type.get() != "Bicycle" else None
            fuel_level = float(self.entries["Fuel Level"].get()) if self.vehicle_type.get() != "Bicycle" else 0

            if self.vehicle_type.get() == "Car":
                seating_capacity = int(self.extra_fields["Seating Capacity"].get())
                vehicle = Car(vehicle_id, brand, model, year, mileage, fuel_type, fuel_level, seating_capacity)
            elif self.vehicle_type.get() == "Truck":
                current_cargo = float(self.extra_fields["Current Cargo"].get())
                max_load = float(self.extra_fields["Max Load"].get())
                vehicle = Truck(vehicle_id, brand, model, year, mileage, fuel_type, fuel_level, current_cargo, max_load)
            elif self.vehicle_type.get() == "Motorcycle":
                engine_size = int(self.extra_fields["Engine Size"].get())
                vehicle = Motorcycle(vehicle_id, brand, model, year, mileage, fuel_type, fuel_level, engine_size)
            elif self.vehicle_type.get() == "Bicycle":
                vehicle = Bicycle(vehicle_id, brand, model, year, mileage)

            self.vehicles.append(vehicle)
            self.save_vehicles()
            self.show_vehicles()
            messagebox.showinfo("Success", f"{self.vehicle_type.get()} added successfully!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_vehicles(self):
        """ Display all stored vehicles with proper details """
        self.vehicle_listbox.delete(0, tk.END)

        if not self.vehicles:
            self.vehicle_listbox.insert(tk.END, "No vehicles in the fleet.")
            return

        for v in self.vehicles:
            vehicle_info = f"{v.__class__.__name__}: {v.vehicle_id} - {v.brand} {v.model}, {v.year}, {v.mileage} km"

            if isinstance(v, Car):
                vehicle_info += f", Fuel: {v.fuel_type} ({v.fuel_level}L), Seating: {v.seating_capacity}"
            elif isinstance(v, Truck):
                vehicle_info += f", Fuel: {v.fuel_type} ({v.fuel_level}L), Cargo: {v.current_cargo}kg, Max Load: {v.max_load}kg"
            elif isinstance(v, Motorcycle):
                vehicle_info += f", Fuel: {v.fuel_type} ({v.fuel_level}L), Engine: {v.engine_size}cc"



            self.vehicle_listbox.insert(tk.END, vehicle_info)

    def open_refuel_window(self):
        """ Open a new window for refueling a selected vehicle. """
        self.refuel_window = tk.Toplevel(self.root)
        self.refuel_window.title("Refuel Vehicle")
        self.refuel_window.geometry("300x200")  # Set the window size

        tk.Label(self.refuel_window, text="Select Vehicle ID:", font=("Arial", 12)).pack(pady=5)
        self.selected_vehicle_id = tk.StringVar()
        vehicle_ids = [v.vehicle_id for v in self.vehicles if hasattr(v, 'fuel_level')]
        self.vehicle_menu_refuel = tk.OptionMenu(self.refuel_window, self.selected_vehicle_id, *vehicle_ids)
        self.vehicle_menu_refuel.pack(pady=5)

        tk.Label(self.refuel_window, text="Enter Fuel Amount (L):", font=("Arial", 12)).pack(pady=5)
        self.fuel_amount_entry = tk.Entry(self.refuel_window, font=("Arial", 12))
        self.fuel_amount_entry.pack(pady=5)

        tk.Button(self.refuel_window, text="Refuel", font=("Arial", 12), command=self.refuel_vehicle).pack(pady=10)

    def refuel_vehicle(self):
        """ Update the fuel level of the selected vehicle. """
        vehicle_id = self.selected_vehicle_id.get()
        try:
            fuel_amount = float(self.fuel_amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                vehicle.fuel_level += fuel_amount
                messagebox.showinfo("Success", f"Refueled {fuel_amount}L. New Level: {vehicle.fuel_level}L")
                self.save_vehicles()
                self.show_vehicles()
                return

    def clear_fields(self):
        """ Clear input fields after adding a vehicle """
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        for entry in self.extra_fields.values():
            entry.delete(0, tk.END)



root = tk.Tk()
app = FleetApp(root)
root.mainloop()