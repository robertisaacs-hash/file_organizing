# organize the desktop
# moves images, videos, screenshots, and audio files
# into corresponding folders
import os
import shutil
from pathlib import Path


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

# Get user's desktop and documents paths (cross-platform)
desktop_path = Path.home() / "Desktop"
documents_path = Path.home() / "Documents"

# Create organized folders if they don't exist
folders = {
    "audio": documents_path / "audio",
    "video": documents_path / "video", 
    "images": documents_path / "images",
    "screenshots": documents_path / "screenshots"
}

for folder in folders.values():
    folder.mkdir(exist_ok=True)

print(f"Organizing files from: {desktop_path}")
print(f"Moving files to: {documents_path}")

# Change to desktop directory
try:
    os.chdir(desktop_path)
except FileNotFoundError:
    print(f"Error: Desktop path not found: {desktop_path}")
    print("Please check if the Desktop folder exists.")
    exit(1)

# Process files
files_moved = 0
for file in os.listdir():
    if os.path.isfile(file):  # Only process files, not directories
        try:
            if is_audio(file):
                shutil.move(file, folders["audio"] / file)
                print(f"Moved audio: {file}")
            elif is_video(file):
                shutil.move(file, folders["video"] / file)
                print(f"Moved video: {file}")
            elif is_image(file):
                if is_screenshot(file):
                    shutil.move(file, folders["screenshots"] / file)
                    print(f"Moved screenshot: {file}")
                else:
                    shutil.move(file, folders["images"] / file)
                    print(f"Moved image: {file}")
            else:
                shutil.move(file, documents_path / file)
                print(f"Moved other: {file}")
            files_moved += 1
        except Exception as e:
            print(f"Error moving {file}: {e}")

print(f"\nOrganization complete! Moved {files_moved} files.")
