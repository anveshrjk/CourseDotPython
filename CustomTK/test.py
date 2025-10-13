#customtkinter

import customtkinter as ctk

# Set the appearance mode (e.g., "System", "Light", "Dark")
ctk.set_appearance_mode("System")
# Set the default color theme (e.g., "blue", "green", "dark-blue")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("My CustomTkinter App")
app.geometry("400x300")

button = ctk.CTkButton(master=app, text="Hello CustomTkinter!")
button.pack(pady=20)

app.mainloop()