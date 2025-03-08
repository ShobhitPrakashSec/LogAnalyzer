import os
import re
from datetime import datetime

def detect_log_type(log_lines):
    """
    Detects the log file type based on its content.
    Returns 'web_server', 'system', 'application', or 'unknown'.
    """
    web_server_pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - (GET|POST|PUT|DELETE)")
    system_pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - (ERROR|WARNING|INFO)")
    application_pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - (APP|DB|API)")

    for line in log_lines:
        if web_server_pattern.search(line):
            return "web_server"
        elif system_pattern.search(line):
            return "system"
        elif application_pattern.search(line):
            return "application"

    return "unknown"

def read_log_file(file_path):
    """
    Reads a log file and returns its contents as a list of lines along with the detected log type.
    If the file does not exist, it prints an error and returns an empty list.
    """
    if not os.path.exists(file_path):
        print(f"Log file not found: {file_path}")
        return [], "unknown"

    with open(file_path, "r") as file:
        log_lines = file.readlines()

    log_type = detect_log_type(log_lines)
    return log_lines, log_type

def filter_log_by_timestamp(log_lines, start_time=None, end_time=None):
    """
    Filters log entries based on the given timestamp range.

    Args:
    - log_lines (list): List of log entries.
    - start_time (datetime, optional): Start time for filtering.
    - end_time (datetime, optional): End time for filtering.

    Returns:
    - list: Filtered log entries.
    """
    filtered_logs = []

    for line in log_lines:
        match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
        if match:
            log_time = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
            
            if (not start_time or log_time >= start_time) and (not end_time or log_time <= end_time):
                filtered_logs.append(line)

    return filtered_logs

def filter_log_by_keyword(log_lines, keyword):
    """
    Filters logs that contain a specific keyword.
    """
    if not keyword:
        return log_lines  # No filtering needed

    return [line for line in log_lines if keyword.lower() in line.lower()]