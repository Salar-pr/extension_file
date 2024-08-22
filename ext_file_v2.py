import os
import glob
from khayyam import JalaliDate

# دریافت نام فایل جاری
current_file = os.path.basename(__file__)

# دریافت لیست فایل‌ها در دایرکتوری جاری
file_list = glob.glob('*')

# مجموعه‌ای برای ذخیره پسوندها
extensions_set = set()

# استخراج پسوندها و اضافه کردن به مجموعه
for each_file in file_list:
    if each_file == current_file:
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
                today  = JalaliDate.today().strftime("%A %d %B %Y")
                os.makedirs(today+ "/" +folder_name)
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
                    today  = JalaliDate.today().strftime("%A %d %B %Y")
                    os.rename(each_file,today + "/"+ dest_folder + each_file)
                except OSError as e:
                    print(
                        f"Error moving file {each_file} to {dest_folder}: {e}")


create_folders()
move_files()
