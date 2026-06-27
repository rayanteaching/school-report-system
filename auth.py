def teacher_login(username: str, password: str) -> bool:
    """
    Validate teacher credentials.

    Returns:
        bool: True if credentials match, False otherwise.
    """
    teacher_username = "teacher"
    teacher_password = "1234"
    return username == teacher_username and password == teacher_password


def student_login(data: dict, username: str, password: str) -> bool:
    """
    Validate student credentials against the data dictionary.

    Returns:
        bool: True if username exists and password matches, False otherwise.
    """
    if username not in data:
        return False
    return data[username]["password"] == password


if __name__ == "__main__":
    test_data = {
        "ali": {
            "password": "1111",
            "grades": {
                "math": 18
            }
        }
    }
    print(teacher_login("teacher", "1234"))   
    print(teacher_login("teacher", "wrong"))  
    print(student_login(test_data, "ali", "1111"))  
    print(student_login(test_data, "ali", "wrong"))