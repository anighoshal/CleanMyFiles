# 🧹 CleanMyFiles – Intelligent File Organizer Tool

CleanMyFiles is a smart, GUI-based file organizer built with Python. It scans a selected folder, categorizes files by type, and moves them into neatly organized subfolders. Designed for speed, scalability, and simplicity, it’s perfect for students, professionals, and anyone tired of digital clutter.

---

## 🚀 Features

- ✅ Categorizes files into Documents, Images, Videos, Audio, Archives, and Others
- ✅ GUI built with Tkinter for easy folder selection and one-click organizing
- ✅ Optimized for large directories using generators and batch processing
- ✅ Threaded backend keeps GUI responsive during heavy operations
- ✅ Intelligent logging with rotating log files
- ✅ Duplicate file detection (by name) and skip logic
- ✅ Clean and professional `.exe` packaging for Windows users

---

## 🖥️ How It Works

1. Select a folder using the GUI
2. CleanMyFiles scans all files (excluding already organized folders)
3. Files are categorized based on extension
4. Each file is moved to its respective category folder
5. Logs are saved in `logs/organizer.log`

---

## 📦 Installation

### 🔧 Requirements
- Python 3.8+
- Tkinter (usually included with Python)
- Windows (for `.exe` version)

### 🐍 Run from Source
git clone https://github.com/your-username/CleanMyFiles.git
cd CleanMyFiles/src
python main.py

### 🧊 Run as Executable

If you don’t want to install Python, you can run CleanMyFiles as a standalone `.exe` file:

1. Download `CleanMyFiles.exe` from the [Releases](https://github.com/your-username/CleanMyFiles/releases) tab.
2. Double-click the file to launch the GUI.
3. Select a folder and click “Organize Files”.

> 💡 The `.exe` version includes a custom icon and runs without opening a terminal window.

---

## 🧠 Architecture


---

## 🛠️ Developer Notes

- Uses generator-based scanning for memory efficiency  
- Batch size for file movement is configurable (`default = 100`)  
- Logging level can be toggled between `INFO` and `DEBUG`  
- GUI runs in a separate thread to avoid freezing  

---

## 📈 Future Enhancements

- 🔍 Hash-based duplicate detection  
- 📊 Summary report generation (.txt or .csv)  
- 👀 Preview mode before organizing  
- 📅 Filters by date and file size  
- 🌙 Dark mode toggle  
- 📁 Custom category definitions via settings panel  

---

## 👨‍💻 Author

**Anirban**  
MTech Candidate | Python Developer | Academic Innovator

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for full details.
