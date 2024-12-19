CHOICE ONE: File Operations
Copying Files
Function: copyFile(fName: str, nDir: str)
Real-Life Application:
Copying files is an essential task in data management, allowing users to duplicate important 
documents, photos, and other digital assets for backup or distribution purposes.
Advantages:
•Redundancy: Creates backup copies to prevent data loss.
•Organization: Allows users to segregate and organize files across different directories.
•Collaboration: Enables sharing of documents without altering the original file.
Working:
The function uses the shutil.copy method to duplicate a file from its current location to a 
specified directory. Exception handling ensures any issues during the copy process are gracefully 
managed.
Deleting Files
Function: deleteFile(fName: str, fPath: str)
Real-Life Application:
Deleting files is a routine activity to free up disk space, remove outdated or unnecessary data, and 
maintain a tidy digital workspace.
Advantages:
•Space Management: Frees up storage by removing unneeded files.
•Security: Eliminates sensitive data that is no longer needed.
•Organization: Helps in maintaining an uncluttered directory structure.
Working:
The function constructs the file path using os.path.join and deletes the file with os.remove. 
The action is logged in an undo stack for potential restoration.
Renaming Files
Function: renameFile(fName: str, nName: str)
Real-Life Application:
Renaming files helps in organizing and easily identifying files based on their content or purpose.
Advantages:
•Clarity: Improves file name readability and understanding.
•Organization: Helps in systematic categorization of files.
•Version Control: Assists in maintaining different versions of a document.
Working:
This function renames a file using os.rename, updating the file name to the new specified name, 
and logs the change for undo operations.
Compressing Files
Function: compressFile(fName: str)
Real-Life Application:
Compressing files is useful for saving disk space and preparing files for efficient sharing and 
transfer over the internet.
Advantages:
•Space Saving: Reduces file size, conserving storage.
•Efficiency: Facilitates faster file transfer.
•Archiving: Helps in creating archives for backup purposes.
Working:
The function uses gzip to compress a file, reading the original file and writing its compressed 
form to a new file with a .gz extension.
CHOICE TWO: Search and Filter
Function: searchAndFilter()
Real-Life Application:
Searching and filtering files based on specific criteria such as extensions or modification dates 
streamlines the process of locating important documents in a large dataset.
Advantages:
•Efficiency: Quickly finds relevant files.
•Organization: Helps in categorizing and organizing files.
•Time-saving: Reduces the time spent on manual file searches.
Working:
The function uses os.scandir to iterate through files in a directory, matching them against a 
specified pattern using fnmatch. An optional date filter adds further specificity.
CHOICE THREE: File Preview
Function: filePreview()
Real-Life Application:
Previewing files allows users to quickly view the contents of a file without needing to open it in its 
native application, which is particularly useful for text, data, image, and video files.
Advantages:
•Convenience: Quickly accesses file contents.
•Efficiency: Saves time by avoiding full application launches.
•Versatility: Supports multiple file types including text, binary data, images, and videos.
Working:
Depending on the file extension, the function reads and displays text files, deserializes and prints 
binary data, opens images using PIL, and plays videos using tkvideo.
CHOICE FOUR: Duplicate File Finder
Function: dup()
Real-Life Application:
Finding and removing duplicate files helps in decluttering storage and ensuring there is no 
redundancy in file storage.
Advantages:
•Space Management: Frees up disk space by removing duplicates.
•Efficiency: Reduces storage costs.
•Organization: Keeps directories clean and organized.
Working:
The function computes the MD5 hash of files using hashlib, comparing them to identify 
duplicates. Duplicate files are deleted to conserve space.
CHOICE FIVE: Temporary Storage
Function: tempStorage()
Real-Life Application:
Temporarily storing files can be useful when files need to be moved out of the way but not 
permanently deleted, similar to a recycle bin.
Advantages:
•Safety: Files are not immediately deleted, allowing for recovery.
•Organization: Helps in decluttering while retaining recoverability.
•Convenience: Temporary storage without permanent deletion.
Working:
The function moves files to a hidden .recycleBin directory within the user's home directory, 
logging the move for potential undo operations.
CHOICE SIX: Cloud Integration
Function: cloud()
Real-Life Application:
Uploading files to the cloud ensures data is backed up and accessible from anywhere, enhancing 
collaboration and security.
Advantages:
•Accessibility: Files can be accessed from any location with internet connectivity.
•Backup: Ensures important files are backed up remotely.
•Collaboration: Facilitates easy sharing with collaborators.
Working:
The function uses PyDrive to authenticate with Google Drive, create a file on the drive, and 
upload the specified file.
CHOICE SEVEN: Disk Usage Statistics
Function: diskStats()
Real-Life Application:
Analyzing disk usage helps in understanding storage consumption, identifying space hogs, and 
planning for storage upgrades or cleanup.
Advantages:
•Insight: Provides detailed insights into disk usage.
•Optimization: Helps in optimizing storage.
•Planning: Aids in planning for future storage needs.
Working:
The function calculates the size of directories using os.walk and plots the results using 
matplotlib to visually represent the disk usage statistics.
CHOICE EIGHT: Undo
Function: Undo()
Real-Life Application:
The ability to undo file operations ensures that accidental changes can be reverted, providing a 
safety net during file management.
Advantages:
•Safety: Protects against accidental deletions or renames.
•Convenience: Allows for corrections without redoing work.
•Efficiency: Saves time and effort by providing a quick way to revert actions.
Working:
The function uses an undo stack to track actions such as deletions, renames, and restores. It reverts 
the most recent action using the stored information.
Conclusion
A comprehensive file manager script is an invaluable tool in the modern digital workspace. It 
simplifies file operations, enhances efficiency, and provides robust features for searching, 
previewing, and managing files. By leveraging these functionalities, users can maintain an 
organized, secure, and efficient file system, ensuring their digital life is streamlined and productive.
This guide has provided an in-depth look at the uses, advantages, and workings of each function, 
demonstrating the practical applications and technological underpinnings of an essential file 
manager. By understanding and utilizing these functions, users can achieve a higher level of 
productivity and organization in their daily file management tasks.
