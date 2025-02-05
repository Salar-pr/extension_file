import os
import glob
import tkinter as tk
from tkinter import ttk
import time


# دریافت نام فایل جاری
current_file = os.path.basename(__file__)

# دریافت لیست فایل‌ها در دایرکتوری جاری
file_list = glob.glob('*')

# مجموعه‌ای برای ذخیره پسوندها
extensions_set = set()

# استخراج پسوندها و اضافه کردن به مجموعه
for each_file in file_list:
    if each_file == current_file :
        continue
    if os.path.isfile(each_file):  # بررسی اینکه آیا فایل است
        _, extension = os.path.splitext(each_file)
        if extension:  # اگر پسوند وجود دارد
            extensions_set.add(extension.lstrip('.'))

# ایجاد پوشه‌ها بر اساس پسوندها


def create_folders():
    for ext in extensions_set:
        folder_name = ext + '_files'
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
            except OSError as e:
                print(f"Error creating directory {folder_name}: {e}")

# انتقال فایل‌ها به پوشه‌های مربوطه


def move_files():
    for each_file in file_list:
        if each_file == current_file:
            continue
        if os.path.isfile(each_file):  # بررسی اینکه آیا فایل است
            _, extension = os.path.splitext(each_file)
            if extension:  # اگر پسوند وجود دارد
                extension = extension.lstrip('.')
                dest_folder = extension + '_files'
                try:
                    os.rename(each_file, os.path.join(dest_folder, each_file))
                except OSError as e:
                    print(
                        f"Error moving file {each_file} to {dest_folder}: {e}")


def start_progress():
    progress.start()

    create_folders()
    move_files()
    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.05)
        progress['value'] = i
        # Update the GUI
        root.update_idletasks()
    progress.stop()


# GUI Setup
root = tk.Tk()
root.title("File sorting")
root.geometry("400x200")
root.configure(bg="#f0f0f0")

# Label
label = tk.Label(root, text="File Organizer",
                 font=("Arial", 14, "bold"), bg="#f0f0f0")
label.pack(pady=10)

# Progress Bar
progress = ttk.Progressbar(root, orient="horizontal",
                           length=300, mode="determinate")
progress.pack(pady=10)

# Start Button
start_button = tk.Button(root, text="Start Organization", command=start_progress, font=(
    "Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
start_button.pack(pady=10)

root.mainloop()
