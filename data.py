import json
import os

FILE_NAME = "students_data.json"


def save_data(data: dict) -> bool:
    """
    Save student data to the JSON file.

    Parameters:
        data (dict): The full students dictionary to persist.

    Returns:
        bool: True if saved successfully, False otherwise.
    """
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except (OSError, TypeError) as e:
        print(f"[ERROR] save_data failed: {e}")
        return False


def load_data() -> dict:
    """
    Load student data from the JSON file.

    Returns:
        dict: Students dictionary. Returns empty dict if file not found or corrupted.
    """
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            if not isinstance(data, dict):
                print("[WARNING] Data file has unexpected format. Returning empty dict.")
                return {}
            return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"[ERROR] Corrupted data file: {e}")
        return {}


if __name__ == "__main__":
    students_data = {
        "ali": {
            "password": "1111",
            "grades": {
                "math": 18,
                "science": 19
            }
        }
    }

    result = save_data(students_data)
    print(f"Save result: {result}")

    loaded_data = load_data()
    print(f"Loaded data: {loaded_data}")
