import os
import re

def detect_log_type(log_lines):
    """
    Detects the log type based on its content.
    Returns 'web_server', 'system', 'application', or 'unknown'.
    """
    # Define patterns for each log type
    web_server_pattern = re.compile(r"(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}) - (GET|POST|PUT|DELETE)")
    system_pattern = re.compile(r"(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}) - (ERROR|WARNING|INFO)")
    application_pattern = re.compile(r"(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}) - (APP|DB|API)")

    # Check the first few lines of the log file
    for line in log_lines:
        if web_server_pattern.match(line):
            return "web_server"
        elif system_pattern.match(line):
            return "system"
        elif application_pattern.match(line):
            return "application"

    return "unknown"

def read_log_file(file_path):
    """
    Reads a log file and returns its contents as a list of lines along with detected log type.
    If the file does not exist, it prints an error and returns an empty list and 'unknown'.
    """
    if not os.path.exists(file_path):
        print(f"Log file not found: {file_path}")
        return [], "unknown"  # Returning empty list and 'unknown' log type

    with open(file_path, "r") as file:
        log_lines = file.readlines()  # Read file content

    log_type = detect_log_type(log_lines)  # Detect log type
    print(f"Detected log type: {log_type} Logs ({len(log_lines)} lines)")  # Debugging message

    return log_lines, log_type  # Return both logs and log type
