import os, shutil

path = r"C:/Users/areeb/OneDrive/Documents/Miscellaneous/"

file_names = os.listdir(path)
folder_names = ['csv files', 'image files', 'text files', 'doc files', 'ppt files', 'pdf files', 'excel files', 'url files']

# Create folders if they don't exist
for folder_name in folder_names:
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        print(f"Creating folder: {folder_path}")
        os.makedirs(folder_path)

# Move files to the appropriate folders
for file in file_names:
    file_path = os.path.join(path, file)

    if os.path.isdir(file_path):
        # Skip directories
        print(f"Skipping directories: {file}")
        continue

    if file.endswith(".csv"):
        destination = os.path.join(path, "csv files", file)
    elif file.endswith((".png", ".jpeg", ".svg", 'jpg')):
        destination = os.path.join(path, "image files", file)
    elif file.endswith(".docx"):
        destination = os.path.join(path, "doc files", file)
    elif file.endswith(".ppt"):
        destination = os.path.join(path, "ppt files", file)
    elif file.endswith(".txt"):
        destination = os.path.join(path, "text files", file)
    elif file.endswith(".pdf"):
        destination = os.path.join(path, "pdf files", file)
    elif file.endswith(".xlsx"):
        destination = os.path.join(path, "excel files", file)
    elif file.endswith(".url"):
        destination = os.path.join(path, "url files", file)
    else:
        print(f"File '{file}' was not moved.")
        continue

    if not os.path.exists(destination):
        shutil.move(file_path, destination)
        print(f"Moved '{file}' to '{destination}'")
    else:
        print(f"File '{file}' already exists in the destination.")









