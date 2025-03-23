# File Manager

## Introduction
The **File Manager** is a comprehensive script designed to streamline file operations such as copying, deleting, renaming, compressing, searching, previewing, and cloud integration. This tool enhances productivity by simplifying file management tasks, ensuring efficiency, organization, and security.

---

## Features
This file manager provides the following functionalities:

1. **File Operations**
   - Copy, delete, rename, and compress files with ease.
2. **Search and Filter**
   - Locate files based on criteria such as extensions or modification dates.
3. **File Preview**
   - Quickly preview text, image, and video files without opening them in separate applications.
4. **Duplicate File Finder**
   - Detect and remove duplicate files to optimize storage.
5. **Temporary Storage**
   - Move files to a temporary storage area instead of deleting them immediately.
6. **Cloud Integration**
   - Upload files to cloud storage for remote access and collaboration.
7. **Disk Usage Statistics**
   - Analyze storage consumption and visualize disk usage.
8. **Undo**
   - Revert file operations to prevent accidental changes.

---

## Functions & Workflows

### 1️⃣ File Operations
#### `copyFile(fName: str, nDir: str)`
- **Real-Life Application:** Allows users to duplicate important files for backup or distribution.
- **Advantages:**
  - Redundancy: Prevents data loss.
  - Organization: Segregates files into different directories.
  - Collaboration: Enables sharing without modifying the original file.
- **Working:** Uses `shutil.copy()` to duplicate a file, with exception handling to manage errors.

#### `deleteFile(fName: str, fPath: str)`
- **Real-Life Application:** Frees up disk space and removes unnecessary data.
- **Advantages:**
  - Space Management: Clears storage.
  - Security: Removes sensitive data.
  - Organization: Keeps directories tidy.
- **Working:** Uses `os.remove()` after constructing the file path with `os.path.join()`.

#### `renameFile(fName: str, nName: str)`
- **Real-Life Application:** Organizes files by renaming them based on their content.
- **Advantages:**
  - Clarity: Improves readability.
  - Organization: Systematic categorization.
  - Version Control: Maintains different document versions.
- **Working:** Uses `os.rename()` to rename the file and logs changes for undo operations.

#### `compressFile(fName: str)`
- **Real-Life Application:** Reduces file sizes for storage efficiency and faster sharing.
- **Advantages:**
  - Space Saving: Conserves storage.
  - Efficiency: Accelerates transfers.
  - Archiving: Creates backup archives.
- **Working:** Uses `gzip` to compress files into `.gz` format.

---

### 2️⃣ Search and Filter
#### `searchAndFilter()`
- **Real-Life Application:** Helps locate important files in large datasets.
- **Advantages:**
  - Efficiency: Quickly finds files.
  - Organization: Categorizes files.
  - Time-saving: Reduces manual searches.
- **Working:** Uses `os.scandir()` and `fnmatch` for pattern matching with optional date filters.

---

### 3️⃣ File Preview
#### `filePreview()`
- **Real-Life Application:** Allows users to view file contents without opening them in separate applications.
- **Advantages:**
  - Convenience: Quick access.
  - Efficiency: Saves time.
  - Versatility: Supports multiple formats.
- **Working:** Uses PIL for images, `tkvideo` for videos, and standard file reading for text files.

---

### 4️⃣ Duplicate File Finder
#### `dup()`
- **Real-Life Application:** Eliminates redundant files to optimize storage.
- **Advantages:**
  - Space Management: Frees up space.
  - Efficiency: Reduces costs.
  - Organization: Keeps directories clean.
- **Working:** Computes MD5 hashes with `hashlib` to identify and delete duplicates.

---

### 5️⃣ Temporary Storage
#### `tempStorage()`
- **Real-Life Application:** Acts as a recycle bin before permanent deletion.
- **Advantages:**
  - Safety: Allows recovery.
  - Organization: Declutters while retaining recoverability.
  - Convenience: Temporary file holding.
- **Working:** Moves files to a hidden `.recycleBin` using `shutil.move()` and logs changes.

---

### 6️⃣ Cloud Integration
#### `cloud()`
- **Real-Life Application:** Ensures remote access to files for backup and collaboration.
- **Advantages:**
  - Accessibility: Access from anywhere.
  - Backup: Secure file storage.
  - Collaboration: Easy sharing.
- **Working:** Uses `PyDrive` to authenticate and upload files to Google Drive.

---

### 7️⃣ Disk Usage Statistics
#### `diskStats()`
- **Real-Life Application:** Analyzes disk space usage to plan for storage optimization.
- **Advantages:**
  - Insight: Detailed disk analysis.
  - Optimization: Identifies large files.
  - Planning: Helps with storage upgrades.
- **Working:** Uses `os.walk()` to calculate folder sizes and `matplotlib` for visualization.

---

### 8️⃣ Undo
#### `Undo()`
- **Real-Life Application:** Reverts accidental file modifications.
- **Advantages:**
  - Safety: Prevents unintended deletions.
  - Convenience: Allows corrections.
  - Efficiency: Saves time.
- **Working:** Uses an undo stack to track and restore changes.

---

## Installation & Usage

### **Requirements**
- Python 3.x
- Required Libraries:
  ```bash
  pip install shutil os gzip fnmatch hashlib PyDrive matplotlib tkvideo PIL
  ```

### **How to Use**
1. Clone the repository:
   ```bash
   git clone https://github.com/Arjun-Walia/file-manager.git
   cd file-manager
   ```
2. Run the script:
   ```bash
   python file_manager.py
   ```
3. Follow the on-screen instructions to perform file operations.

---

## Contribution
- Fork the repository.
- Create a feature branch (`git checkout -b feature-name`).
- Commit your changes (`git commit -m 'Added feature'`).
- Push to the branch (`git push origin feature-name`).
- Open a Pull Request.

---

## Conclusion
The **File Manager** provides an extensive suite of features to enhance file management efficiency. By leveraging functions like file operations, search, preview, and cloud integration, users can ensure an organized, secure, and productive digital workspace.
