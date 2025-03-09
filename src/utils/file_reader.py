import os
import re
from datetime import datetime

def detect_log_type(log_lines):
    """
    Detects the log file type based on its content.
    Returns 'web_server', 'system', 'application', or 'unknown'.
    """
    web_server_patterns = [
        r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - (GET|POST|PUT|DELETE)",
        r"\b(GET|POST|PUT|DELETE) /[^\s]+ HTTP/\d\.\d\b"
    ]
    system_patterns = [
        r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - (ERROR|WARNING|INFO|DEBUG|CRITICAL)",
        r"\b(ERROR|WARNING|INFO|DEBUG|CRITICAL):"
    ]
    application_patterns = [
        r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - (APP|DB|API)",
        r"\b(APP|DB|API):"
    ]

    scores = {"web_server": 0, "system": 0, "application": 0}
    
    for line in log_lines:
        for pattern in web_server_patterns:
            if re.search(pattern, line):
                scores["web_server"] += 1
        for pattern in system_patterns:
            if re.search(pattern, line):
                scores["system"] += 1
        for pattern in application_patterns:
            if re.search(pattern, line):
                scores["application"] += 1
                
    best_match = max(scores, key=scores.get)

    return best_match if scores[best_match] > 0 else "unknown"

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

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def categorize_logs_by_level(log_lines, keyword=None):
    """
    Categorizes log entries by their log level and applies keyword filtering if provided.
    Returns a dictionary where keys are log levels and values are lists of log entries.
    """
    categorized_logs = {level: [] for level in LOG_LEVELS}
    
    for line in log_lines:
        for level in LOG_LEVELS:
            if f"{level}:" in line:
                if keyword is None or keyword.lower() in line.lower():  # Apply keyword filter
                    categorized_logs[level].append(line)
                break
    
    return categorized_logs

