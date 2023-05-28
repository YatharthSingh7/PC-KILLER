import os
import time
import tkinter as tk
from tkinter import messagebox

# Function to start the countdown
def start_countdown():
    # Get the input value from the entry field
    try:
        minutes = float(entry.get())
        if minutes <= 0:
            messagebox.showerror("Error", "Please enter a positive value.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        return

    # Convert time to seconds
    seconds = minutes * 60

    # Disable the entry field and start button
    entry.config(state=tk.DISABLED)
    start_button.config(state=tk.DISABLED)

    # Countdown loop
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
        countdown_label.config(text=str(seconds))

    # When countdown reaches zero, execute system shutdown
    if seconds == 0:
        messagebox.showinfo("Countdown Finished", "System will now shut down.")
        os.system("shutdown /s")
    else:
        messagebox.showinfo("Countdown Finished", "Countdown finished without shutting down the system.")

# Create the main window
window = tk.Tk()
window.title("Countdown Timer")
window.geometry("300x150")

# Create GUI elements
label = tk.Label(window, text="Enter Time in Minutes:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

start_button = tk.Button(window, text="Start Countdown", command=start_countdown)
start_button.pack(pady=10)

countdown_label = tk.Label(window, text="")
countdown_label.pack()

# Run the main window loop
window.mainloop()