import os
import sys
from datetime import datetime

# Add the src directory to Python's module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from utils.file_reader import filter_log_by_timestamp, read_log_file  # Import log reader

# Ask the user to enter the full log file path
log_file_path = input("Enter the full path of the log file: ").strip()

# Check if the file exists before proceeding
if not os.path.exists(log_file_path):
    print(f"Error: The file '{log_file_path}' does not exist. Please check the path and try again.")
    sys.exit(1)  # Exit the script if the file does not exist

# Read logs and detect log type
log_lines, log_type = read_log_file(log_file_path)

# ask user for timestamp range
start_time = input("Enter the start timestamp (YYYY/MM/DD HH:MM:SS) or press enter to skip: ")
end_time = input("Enter the end timestamp (YYYY/MM/DD HH:MM:SS) or press enter to skip: ")

# Convert the timestamp strings to datetime objects
if start_time:
    start_time = datetime.strptime(start_time, "%Y/%m/%d %H:%M:%S")
if end_time:
    end_time = datetime.strptime(end_time, "%Y/%m/%d %H:%M:%S")
    
# Filter logs based on the timestamp range
log_lines = filter_log_by_timestamp(log_lines, start_time, end_time)

# Print logs
if log_lines:
    print(f"\nDetected log type: {log_type}")
    print(f"Displaying first 10 logs from {log_file_path}:\n")
    
    for log in log_lines[:10]:  # Display the first 10 logs
        print(log.strip())  # Remove trailing newlines
else:
    print("No logs found or file is empty.")
