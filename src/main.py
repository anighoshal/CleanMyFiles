# main.py

import os
import shutil
import logging
from datetime import datetime
from logger import setup_logger

# -------------------------------
# Week 1: Category Definitions
# -------------------------------

CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

# -------------------------------
# Week 1: Create Category Folders
# -------------------------------

def setup_target_folders(base_path):
    """Create target folders for each category if they do not exist."""
    for category in CATEGORIES.keys():
        folder_path = os.path.join(base_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")

# -------------------------------
# Week 2: File Scanning & Metadata
# -------------------------------

def scan_files(base_path):
    """Scan the base directory and return a list of files."""
    file_list = []
    for root, dirs, files in os.walk(base_path):
        if os.path.basename(root) in CATEGORIES.keys():
            continue
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_info = extract_metadata(file_path)
                file_list.append(file_info)
    return file_list

def extract_metadata(file_path):
    """Extract metadata from a file."""
    file_name = os.path.basename(file_path)
    extension = os.path.splitext(file_name)[1]
    size_kb = os.path.getsize(file_path) / 1024
    last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
    return {
        "name": file_name,
        "path": file_path,
        "extension": extension,
        "size_kb": size_kb,
        "last_modified": last_modified
    }

# -------------------------------
# Week 3: Categorization Logic
# -------------------------------

def get_file_category(extension):
    for category, ext_list in CATEGORIES.items():
        if extension.lower() in ext_list:
            return category
    return "Others"

def map_files_to_categories(file_list, base_path):
    file_map = []
    for file in file_list:
        category = get_file_category(file["extension"])
        target_folder = os.path.join(base_path, category)
        file_map.append({
            "source": file["path"],
            "destination": os.path.join(target_folder, file["name"]),
            "category": category
        })
    return file_map

# -------------------------------
# Week 4 & 5: File Movement & Logging
# -------------------------------

def move_file(source, destination):
    if not os.path.exists(source):
        logging.warning(f"Source file not found: {source}")
        return False
    if os.path.exists(destination):
        logging.info(f"Duplicate file skipped: {source}")
        return False
    try:
        shutil.move(source, destination)
        logging.info(f"Moved: {source} → {destination}")
        return True
    except Exception as e:
        logging.error(f"Error moving {source} → {destination}: {e}")
        return False

def organize_files(file_map):
    moved_count = 0
    for entry in file_map:
        success = move_file(entry["source"], entry["destination"])
        if success:
            moved_count += 1
        else:
            logging.warning(f"Failed to move: {entry['source']}")
    logging.info(f"Organizing complete. Total files moved: {moved_count}")
    print(f"\n✅ Organized {moved_count} files.")
    return moved_count  # ✅ Add this line


# -------------------------------
# Week 6: GUI Entry Point
# -------------------------------

def main():
    setup_logger()
    logging.info("Starting CleanMyFiles...")

    from gui import run_gui
    run_gui()

if __name__ == "__main__":
    main()
