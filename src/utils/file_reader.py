import os

def read_log_file(file_path):
    """
    Reads a log file and returns its contents as a list of lines.
    If the file does not exist, it prints an error and returns an empty list.
    """
    if not os.path.exists(file_path):
        print(f"Log file not found: {file_path}")
        return []

    with open(file_path, "r") as file:
        return file.readlines()
