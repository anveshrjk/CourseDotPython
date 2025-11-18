import customtkinter as ctk
import time
import threading

# --- Setup ---
ctk.set_appearance_mode("dark")  # or "light"
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("4-7-8 Breathing App")
app.iconbitmap("icon.ico")
app.geometry("480x420")
app.resizable(False, False)

# --- Global state ---
is_running = False
cycle_count = 0

# --- UI Layout ---
title_label = ctk.CTkLabel(
    app, text="🧘 4-7-8 Breathing Exercise",
    font=("Poppins", 24, "bold"), text_color="#A0E4CB"
)
title_label.pack(pady=(25, 10))

instruction_label = ctk.CTkLabel(
    app, text="Press Start to Begin",
    font=("Poppins", 20), text_color="#EAEAEA"
)

instruction_label.pack(pady=10)

count_label = ctk.CTkLabel(
    app, text="", font=("Poppins", 60, "bold"), text_color="#B5FFD9"
)

count_label.pack(pady=20)

cycle_label = ctk.CTkLabel(
    app, text="Cycles completed: 0",
    font=("Poppins", 16), text_color="#CCCCCC"
)

cycle_label.pack(pady=(10, 30))

# Button frame
button_frame = ctk.CTkFrame(app, corner_radius=15)
button_frame.pack(pady=10)

# --- Functions ---
def breathing_sequence():
    global is_running, cycle_count
    if is_running:
        return
    is_running = True
    start_button.configure(state="disabled")
    reset_button.configure(state="normal")

    def run_cycle():
        global is_running, cycle_count
        while is_running:
            # Inhale phase (ascending 1→4)
            instruction_label.configure(text="🌬️ Inhale", text_color="#A8E6CF")
            for i in range(1, 5):
                if not is_running:
                    return
                count_label.configure(text=str(i))
                time.sleep(1)

            # Hold phase (ascending 1→7)
            instruction_label.configure(text="✋ Hold", text_color="#FFD3B6")
            for i in range(1, 8):
                if not is_running:
                    return
                count_label.configure(text=str(i))
                time.sleep(1)

            # Exhale phase (ascending 1→8)
            instruction_label.configure(text="😮 Exhale", text_color="#FFAAA5")
            for i in range(1, 9):
                if not is_running:
                    return
                count_label.configure(text=str(i))
                time.sleep(1)

            # Completed one cycle
            cycle_count += 1
            cycle_label.configure(text=f"Cycles completed: {cycle_count}")
            instruction_label.configure(text="💤 Relax briefly...", text_color="#EAEAEA")
            count_label.configure(text="")
            time.sleep(2)

    threading.Thread(target=run_cycle, daemon=True).start()

def reset_breathing():
    global is_running, cycle_count
    is_running = False
    cycle_count = 0
    instruction_label.configure(text="Press Start to Begin", text_color="#EAEAEA")
    count_label.configure(text="")
    cycle_label.configure(text="Cycles completed: 0")
    start_button.configure(state="normal")
    reset_button.configure(state="disabled")

# --- Buttons ---
start_button = ctk.CTkButton(
    button_frame, text="Start",
    command=breathing_sequence,
    font=("Poppins", 16, "bold"), width=120, height=40, corner_radius=12
)

start_button.grid(row=0, column=0, padx=15, pady=10)

reset_button = ctk.CTkButton(
    button_frame, text="Reset",
    command=reset_breathing,
    font=("Poppins", 16, "bold"), width=120, height=40,
    fg_color="#333333", hover_color="#555555",
    corner_radius=12, state="disabled"
)
reset_button.grid(row=0, column=1, padx=15, pady=10)

# Footer
footer_label = ctk.CTkLabel(
    app, text="Breathe deeply • Calm your nervous system",
    font=("Poppins", 13), text_color="#8F8F8F"
)
footer_label.pack(side="bottom", pady=15)

# --- Run ---
app.mainloop()
