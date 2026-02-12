import customtkinter as ctk
import json
import os

# Set appearance mode and color theme
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class SettingsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mouse Mover Settings")
        self.geometry("400x350")
        
        # Define config file path (in the same directory as this script)
        self.config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")
        self.load_settings()

        # Grid configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0) # Space

        # Title Label
        self.label_title = ctk.CTkLabel(self, text="Settings", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Interval Setting
        self.frame_interval = ctk.CTkFrame(self)
        self.frame_interval.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.frame_interval.grid_columnconfigure(1, weight=1)

        self.label_interval = ctk.CTkLabel(self.frame_interval, text="Move Interval (seconds):")
        self.label_interval.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.value_interval = ctk.CTkLabel(self.frame_interval, text=str(self.settings["interval"]))
        self.value_interval.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        self.slider_interval = ctk.CTkSlider(self.frame_interval, from_=1, to=60, number_of_steps=59, command=self.update_interval_label)
        self.slider_interval.set(self.settings["interval"])
        self.slider_interval.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="ew")

        # Distance Setting
        self.frame_distance = ctk.CTkFrame(self)
        self.frame_distance.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.frame_distance.grid_columnconfigure(1, weight=1)

        self.label_distance = ctk.CTkLabel(self.frame_distance, text="Move Distance (pixels):")
        self.label_distance.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.value_distance = ctk.CTkLabel(self.frame_distance, text=str(self.settings["distance"]))
        self.value_distance.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        self.slider_distance = ctk.CTkSlider(self.frame_distance, from_=1, to=50, number_of_steps=49, command=self.update_distance_label)
        self.slider_distance.set(self.settings["distance"])
        self.slider_distance.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="ew")

        # Save Button
        self.button_save = ctk.CTkButton(self, text="Save & Close", command=self.save_settings)
        self.button_save.grid(row=3, column=0, padx=20, pady=20)

    def load_settings(self):
        defaults = {"interval": 5, "distance": 10}
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, "r") as f:
                    data = json.load(f)
                    self.settings = {**defaults, **data}
            else:
                self.settings = defaults
        except Exception as e:
            print(f"Error loading settings: {e}")
            self.settings = defaults

    def update_interval_label(self, value):
        self.settings["interval"] = int(value)
        self.value_interval.configure(text=str(int(value)))

    def update_distance_label(self, value):
        self.settings["distance"] = int(value)
        self.value_distance.configure(text=str(int(value)))

    def save_settings(self):
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
        self.destroy()

if __name__ == "__main__":
    app = SettingsApp()
    app.mainloop()
