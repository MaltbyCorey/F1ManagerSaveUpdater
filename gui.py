import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import main
from customtkinter import *


def open_save_file():
    save_path = filedialog.askopenfilename(filetypes=[("Save Files", "*.sav"), ("All Files", "*.*")])
    if save_path:
        messagebox.showinfo("File Selected", f"Selected file: {save_path}")
        main.unpack(save_path)


# Functions for F1 2025 Update options
def update_calendar():
    messagebox.showinfo("Update Calendar", "Calendar updated for F1 2025.")


def update_driver_roster():
    messagebox.showinfo("Update Driver Roster", "Driver roster updated for F1 2025.")


def update_driver_stats():
    messagebox.showinfo("Update Driver Stats", "Driver stats updated for F1 2025.")


def update_car_performance():
    messagebox.showinfo("Update Car Performance", "Car performance updated for F1 2025.")


def update_staff_roster():
    messagebox.showinfo("Update Staff Roster", "Staff roster updated for F1 2025.")


def update_staff_stats():
    messagebox.showinfo("Update Staff Stats", "Staff stats updated for F1 2025.")


def update_all():
    update_calendar()
    update_driver_roster()
    update_driver_stats()
    update_car_performance()
    update_staff_roster()
    update_staff_stats()


# Function to display F1 2025 Update menu
def show_f1_2025_update_menu():
    root.destroy()

    update_menu = tk.Tk()
    update_menu.title("F1 2025 Update Menu")
    update_menu.geometry("840x500")
    update_menu.resizable(False, False)

    # Add banner with image
    try:
        banner_image = Image.open("resources/F12025Banner.png")
        banner_image = banner_image.resize((840, 133), Image.Resampling.LANCZOS)  # Correct resizing method
        banner_photo = ImageTk.PhotoImage(banner_image)

        banner_label = tk.Label(update_menu, image=banner_photo)
        banner_label.image = banner_photo  # Keep a reference to avoid garbage collection
        banner_label.pack()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load banner image: {e}")

    options_frame = tk.Frame(update_menu)
    options_frame.pack(pady=10)

    tk.Button(options_frame, text="Update Calendar", command=update_calendar, width=30).pack(pady=5)
    tk.Button(options_frame, text="Update Driver Roster", command=update_driver_roster, width=30).pack(pady=5)
    tk.Button(options_frame, text="Update Driver Stats", command=update_driver_stats, width=30).pack(pady=5)
    tk.Button(options_frame, text="Update Car Performance", command=update_car_performance, width=30).pack(pady=5)
    tk.Button(options_frame, text="Update Staff Roster", command=update_staff_roster, width=30).pack(pady=5)
    tk.Button(options_frame, text="Update Staff Stats", command=update_staff_stats, width=30).pack(pady=5)
    tk.Button(options_frame, text="Update All", command=update_all, width=30).pack(pady=5)

    update_menu.mainloop()


def add_drivers():
    messagebox.showinfo("Add Drivers", "Feature to add drivers coming soon.")


# Main application window
root = tk.Tk()
root.title("F1 Manager Application")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="F1 Manager", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Open Save File", command=open_save_file, width=30).pack(pady=5)

tk.Button(root, text="F1 2025 Update", command=show_f1_2025_update_menu, width=30).pack(pady=5)

tk.Button(root, text="Add Drivers", command=add_drivers, width=30).pack(pady=5)

root.mainloop()
