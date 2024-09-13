import json
from typing import Any

class DataHandler:
    """
    A utility class for handling data operations such as loading JSON data, saving reports, and logging messages.
    """

    @staticmethod
    def load_device_data(filename: str) -> Any:
        """
        Load JSON data from a file.

        Args:
            filename (str): The path to the JSON file.

        Returns:
            Any: Parsed JSON data as a Python object.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from the file '{filename}'.")
            return None

    @staticmethod
    def save_report(report: str, filename: str) -> None:
        """
        Save a report string to a file.

        Args:
            report (str): The content to be saved.
            filename (str): The path to the file where the report will be saved.
        """
        try:
            with open(filename, 'w') as file:
                file.write(report)
            print(f"Report successfully saved to '{filename}'.")
        except IOError as e:
            print(f"Error: Failed to write to the file '{filename}'. {e}")

    @staticmethod
    def append_to_log(log_filename: str, message: str) -> None:
        """
        Append a message to a log file.

        Args:
            log_filename (str): The path to the log file.
            message (str): The message to append to the log.
        """
        try:
            with open(log_filename, 'a') as log_file:
                log_file.write(message + "\n")
            print(f"Message successfully appended to log '{log_filename}'.")
        except IOError as e:
            print(f"Error: Failed to write to the log file '{log_filename}'. {e}")
