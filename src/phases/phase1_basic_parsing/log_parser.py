import os
import sys

# Add the src directory to Python's module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from utils.file_reader import read_log_file  # Import log reader

# Ask the user to enter the full log file path
log_file_path = input("Enter the full path of the log file: ").strip()

# Check if the file exists before proceeding
if not os.path.exists(log_file_path):
    print(f"Error: The file '{log_file_path}' does not exist. Please check the path and try again.")
    sys.exit(1)  # Exit the script if the file does not exist

# Read logs and detect log type
log_lines, log_type = read_log_file(log_file_path)

# Print logs
if log_lines:
    print(f"\nDetected log type: {log_type}")
    print(f"Displaying first 10 logs from {log_file_path}:\n")
    
    for log in log_lines[:10]:  # Display the first 10 logs
        print(log.strip())  # Remove trailing newlines
else:
    print("No logs found or file is empty.")
