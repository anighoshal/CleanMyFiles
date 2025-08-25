# Week 1 : Initializing category folders in target directory

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



# Week 2 : File detection and Metadata extraction
# Let's add a new function to scan and list files

def scan_files(base_path):
    """Scan the base directory and return a list of files."""
    file_list = []

    for root, dirs, files in os.walk(base_path):
        # Skip the category folders we created
        if os.path.basename(root) in CATEGORIES.keys():
            continue

        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_info = extract_metadata(file_path)
                file_list.append(file_info)

    return file_list


# Extract metadata from each file
from datetime import datetime
def extract_metadata(file_path):
    """Extract metadata from a file."""
    file_name = os.path.basename(file_path)
    extension = os.path.splitext(file_name)[1]
    size_bytes = os.path.getsize(file_path)
    size_kb = size_bytes / 1024  # Convert to KB
    last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')

    return {
        "name": file_name,
        "path": file_path,
        "extension": extension,
        "size_kb": size_kb,
        "last_modified": last_modified
    }

# Update the main function to include file scanning

if __name__ == "__main__":
    print(f"Initializing CleanMyFiles in: {base_dir}")
    setup_target_folders(base_dir)

    print("\nScanning files...")
    files = scan_files(base_dir)
    print(f"Found {len(files)} files:\n")

    for f in files:
        print(f"{f['name']} | {f['extension']} | {f['size_kb']:.2f} KB | Last Modified: {f['last_modified']}")



# Week 3: File categorization logic
# Function to categorize files based on their extensions

def get_file_category(extension):
    # Return the category based on file extension
    for category, ext_list in CATEGORIES.items():
        if extension.lower() in ext_list:
            return category
    return "Others"

# Building the file to folder mapping

def map_files_to_categories(file_list):
    # Map each file to its destination folder based on category
    file_map = []

    for file in file_list:
        category = get_file_category(file["extension"])
        target_folder = os.path.join(base_dir, category)
        file_map.append({
            "source": file["path"],
            "destination": os.path.join(target_folder, file["name"]),
            "category": category
        })
    return file_map

# Update the main function to include file mapping
if __name__ == "__main__":
    print(f"Initializing CleanMyFiles in: {base_dir}")
    setup_target_folders(base_dir)

    print("\nScanning files...")
    files = scan_files(base_dir)
    print(f"Found {len(files)} files.\n")

    print("\nCategorizing files...")
    file_map = map_files_to_categories(files)

    for entry in file_map:
        print(f"{entry['source']} -> {entry['destination']} ({entry['category']})")



