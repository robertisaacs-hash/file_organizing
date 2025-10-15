# File Organizing Toolkit

A comprehensive Python toolkit for automated file management, organization, and desktop cleanup. This project provides utilities to efficiently organize files by type, rename files in bulk, and manage directory structures.

## 🚀 Features

- **Automated Desktop Organization**: Automatically sort files into appropriate folders based on file type
- **Bulk File Renaming**: Rename multiple files with customizable patterns
- **File Type Detection**: Smart detection of audio, video, image, and screenshot files
- **Safe File Operations**: Built-in error handling and directory creation
- **Cross-Platform Support**: Works on Windows, macOS, and Linux

## 📁 Project Structure

```
file-organizing/
├── file_organizing.py    # Core file management utilities
├── organize-desktop.py   # Desktop organization automation
└── README.md            # Project documentation
```

## 🔧 Requirements

- Python 3.6+
- Standard library modules: `os`, `shutil`, `pathlib`

No external dependencies required!

## 📖 Usage

### Desktop Organization (`organize-desktop.py`)

Automatically organizes your desktop by moving files into categorized folders:

- **Audio files** → `Documents/audio/`
- **Video files** → `Documents/video/`
- **Images** → `Documents/images/`
- **Screenshots** → `Documents/screenshots/`
- **Other files** → `Documents/`

**Supported file types:**
- Audio: `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, and more
- Video: `.mp4`, `.mov`, `.webm`, `.TS`, `.MTS`, and more
- Images: `.jpg`, `.png`, `.gif`, `.svg`, `.webp`, and more

```python
python organize-desktop.py
```

**⚠️ Important:** Update the file paths in the script to match your system before running.

### File Management Utilities (`file_organizing.py`)

Provides examples and utilities for common file operations:

- Directory navigation and working directory changes
- Bulk file renaming with custom patterns
- Directory creation with error handling
- File and folder copying/moving operations
- Safe file and directory deletion

## 🛠️ Configuration

Before running the scripts, update the file paths to match your system:

1. **In `organize-desktop.py`:**
   ```python
   os.chdir("/path/to/your/desktop")  # Update this path
   # Update destination paths in the move operations
   ```

2. **In `file_organizing.py`:**
   ```python
   os.chdir("/path/to/your/target/directory")  # Update this path
   ```

## 🔒 Safety Features

- **Non-destructive operations**: Files are moved, not deleted
- **Directory auto-creation**: Destination directories are created automatically
- **Error handling**: Built-in checks for file existence and permissions
- **Path validation**: Ensures safe file operations

## 💡 Use Cases

- **Digital Decluttering**: Automatically organize messy desktop or download folders
- **Media Management**: Sort large collections of photos, videos, and audio files
- **Batch Processing**: Rename files following specific naming conventions
- **System Maintenance**: Regular cleanup of temporary and misplaced files

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📄 License

This project is available for educational and personal use. Please ensure you have appropriate permissions before organizing files on shared systems.

## ⚡ Quick Start

1. Clone or download the repository
2. Update file paths in the scripts to match your system
3. Run the desired script:
   ```bash
   python organize-desktop.py  # For desktop organization
   python file_organizing.py   # For general file operations
   ```

---

**Note**: Always test scripts on a small set of files first to ensure they work as expected with your specific file structure and naming conventions.