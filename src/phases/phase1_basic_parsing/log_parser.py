import os
import sys

# Add the src directory to Python's module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from utils.file_reader import read_log_file  # Importing utility function

# Define log file path
log_file_path = os.path.join("logs", "sample.log")

# Read logs using the utility function
logs = read_log_file(log_file_path)

# Print logs
if logs:
    print("📄 Log File Contents:")
    for log in logs:
        print(log.strip())  # Remove trailing newlines
else:
    print("⚠️ No logs found or file is empty.")
