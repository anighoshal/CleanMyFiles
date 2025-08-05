# src/main.py

import os

# Define categories and their associated file extensions
CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "others": []
}

# Target directory to organize files
base_dir = os.path.expanduser("~/Downloads")  # We can change this to any directory we want to organize

# Function to create target folders for each category
def setup_target_folders(base_path):
    """Create target folders for each category if they do not exist."""
    for category in CATEGORIES.keys():
        folder_path = os.path.join(base_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")

# Run initialization
if __name__ == "__main__":
    print("Initializing CleanMyFiles in : {base_dir}")
    setup_target_folders(base_dir)
    print("Setup complete.")




