# File sorter 

> A small Python script that organizes files in a folder by their extensions (e.g., all .jpg files go into a “jpg” folder).

## What This Does 
This program scans a directory, creates folders based on file types, moves files into their respective folders, and removes any empty directories afterward.

## Why I Built This
- To learn how to work with file handling and directories in Python.

- To solve the problem of messy folders full of random files.

- Because I was curious about how automation scripts work behind the scenes. 
## Quick Start
```bash
cd file-sorter
python file-sorter.py
```
Or run the compiled version:
```bash
file-sorter.exe
```
## Features

- Automatically organizes files by their extensions.

- Creates folders only when needed.

- Cleans up by deleting empty folders. 

## What I learned 

- How to use os, shutil, and os.path for file and folder manipulation.

- How to safely move files and handle missing folders.

- How to turn a Python script into an executable (.exe) with PyInstaller. 

## Notes / Future Improvements 

- Add a GUI file picker to select folders without typing paths.

- Handle duplicate filenames automatically (e.g., add (1), (2) when needed).

- Show a progress bar or simple visual feedback.

---
*Built as part of my learning journey*
