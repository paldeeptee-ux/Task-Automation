import os
import shutil

source_folder = "images"
destination_folder = "moved_images"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Move JPG files
for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source = os.path.join(source_folder, file)
        destination = os.path.join(destination_folder, file)

        shutil.move(source, destination)
        print(f"{file} moved successfully!")

print("All JPG files moved.")