import os
import shutil

path = r"C:/Users/omp31/OneDrive/Desktop/data_analysit/python/"

file_name = os.listdir(path)
folder_name = ['csv files', 'image file', 'text file', 'pdf file']

# Create folders if not exist
for folder in folder_name:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)

# Move files
for file in file_name:
    if file.endswith(".csv"):
        shutil.move(path + file, path + "csv files/" + file)

    elif file.lower().endswith((".png", ".jpg", ".jpeg")):
        shutil.move(path + file, path + "image file/" + file)

    elif file.endswith(".txt"):
        shutil.move(path + file, path + "text file/" + file)

    elif file.endswith(".pdf"):
        shutil.move(path + file, path + "pdf file/" + file)
