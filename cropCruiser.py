import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class CropCruiserGUI:
    def __init__(self, crop_cruiser, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.crop_cruiser = crop_cruiser

        # Create the main window
        self.window = tk.Tk()
        self.window.title("Crop Cruiser GUI")

        # Create a label to display the existing plants
        self.plants_label = tk.Label(self.window, text="Existing Plants:")
        self.plants_label.pack()

        # Create a listbox to show the existing plants
        self.plants_listbox = tk.Listbox(self.window)
        self.plants_listbox.pack()

        # Create buttons for adding and removing plants
        self.add_button = tk.Button(self.window, text="Add Plant", command=self.add_plant)
        self.add_button.pack()

        self.remove_button = tk.Button(self.window, text="Remove Plant", command=self.remove_plant)
        self.remove_button.pack()

        # Run the GUI main loop
        self.update_plants_list()
        self.window.mainloop()

    def update_plants_list(self):
        # Clear the existing plants listbox
        self.plants_listbox.delete(0, tk.END)

        # Update the plants listbox with the current existing plants
        for plant in self.crop_cruiser.plants:
            self.plants_listbox.insert(tk.END, plant.name)

    def add_plant(self):
        plant_name = tk.simpledialog.askstring("Add Plant", "Enter the plant name:")
        if plant_name:
            plant_type = tk.simpledialog.askstring("Add Plant", "Enter the plant type (Basil/Flower):")
            if plant_type.lower() == "basil":
                pot_number = tk.simpledialog.askinteger("Add Plant", "Enter the pot number:")
                if pot_number in self.crop_cruiser.used_plant_pots:
                    tk.messagebox.showerror("Error", "Pot number is already taken. Please enter a different pot number.")
                    tries = 0
                    while (pot_number in self.crop_cruiser.used_plant_pots) and (tries < 3):
                        pot_number = tk.simpledialog.askinteger("Add Plant", "Enter the pot number:")
                        print(tries)
                        tries += 1

                    if tries == 3:   
                        tk.messagebox.showerror("Error", "Too many tries. Please try again later.")
                        return

                watering_freq = random.choice(["daily", "twice a week", "weekly"])
                watering_amount = random.choice(["50ml", "100ml", "150ml"])
                growlight_intensity = random.choice(["low", "medium", "high"])
                growlight_time = random.choice(["6 hours", "8 hours", "10 hours"])
                plant = Basil(plant_name, pot_number, watering_freq, watering_amount,
                            growlight_intensity, growlight_time)
                self.crop_cruiser.add_plant(plant)
                self.update_plants_list()
                
            elif plant_type.lower() == "flower":
                pot_number = tk.simpledialog.askinteger("Add Plant", "Enter the pot number:")
                if pot_number in self.crop_cruiser.used_plant_pots:
                    tk.messagebox.showerror("Error", "Pot number is already taken. Please enter a different pot number.")
                    tries = 0
                    while (pot_number in self.crop_cruiser.used_plant_pots) and (tries < 3):
                        pot_number = tk.simpledialog.askinteger("Add Plant", "Enter the pot number:")
                        print(tries)
                        tries += 1

                    if tries == 3:   
                        tk.messagebox.showerror("Error", "Too many tries. Please try again later.")
                        return

                watering_freq = random.choice(["daily", "twice a week", "weekly"])
                watering_amount = random.choice(["50ml", "100ml", "150ml"])
                growlight_intensity = random.choice(["low", "medium", "high"])
                growlight_time = random.choice(["6 hours", "8 hours", "10 hours"])
                plant = Flower(plant_name, pot_number, watering_freq, watering_amount,
                            growlight_intensity, growlight_time)
                self.crop_cruiser.add_plant(plant)
                self.update_plants_list()

            else:
                tk.messagebox.showerror("Error", "Invalid plant type. Please enter 'Basil' or 'Flower'.")

    def remove_plant(self):
        selected_index = self.plants_listbox.curselection()
        if selected_index:
            selected_plant = self.crop_cruiser.plants[selected_index[0]]
            self.crop_cruiser.remove_plant(selected_plant)
            self.update_plants_list()


class CropCruiser():
    def __init__(self, model_number, num_plant_pots):
        self.model_number = model_number
        self.num_plant_pots = num_plant_pots
        self.used_plant_pots = []
        self.plants = []

    def add_plant(self, plant):
        if len(self.plants) < self.num_plant_pots:
            self.plants.append(plant)
            self.used_plant_pots.append(plant.pot_number)
            print(f"{plant.name} added to the Crop Cruiser.")
        else:
            print("Crop Cruiser is already full. Cannot add more plants.")

    def remove_plant(self, plant):
        if plant in self.plants:
            self.plants.remove(plant)
            self.used_plant_pots.remove(plant.pot_number)
            print(f"{plant.name} removed from the Crop Cruiser.")
        else:
            print(f"{plant.name} is not found in the Crop Cruiser.")


class Plant():
    def __init__(self, name, pot_number, watering_freq,
                 watering_amount, growlight_intensity, growlight_time):
        self.name = name
        self.pot_number = pot_number
        self.watering_freq = watering_freq
        self.watering_amount = watering_amount
        self.growlight_intensity = growlight_intensity
        self.growlight_time = growlight_time


class Basil(Plant):
    def __init__(self, name, pot_number, watering_freq,
                 watering_amount, growlight_intensity, growlight_time):
        super().__init__(name, pot_number, watering_freq,
                         watering_amount, growlight_intensity, growlight_time)


class Flower(Plant):
    def __init__(self, name, pot_number, watering_freq,
                 watering_amount, growlight_intensity, growlight_time):
        super().__init__(name, pot_number, watering_freq,
                         watering_amount, growlight_intensity, growlight_time)


# Create a Crop Cruiser
crop_cruiser = CropCruiser("CC001", 6)

# Create a Basil plant and add it to the Crop Cruiser
my_basil = Basil("Basil", 2, "daily", "50ml", "high", "8 hours")
my_flower = Flower("Rose", 2, "daily", "50ml", "high", "8 hours")
crop_cruiser.add_plant(my_basil)
crop_cruiser.add_plant(my_flower)


# Create the GUI for the Crop Cruiser
print(crop_cruiser.plants[0].name)
print(crop_cruiser.plants[1].name)

gui = CropCruiserGUI(crop_cruiser, "John Doe", 1)


