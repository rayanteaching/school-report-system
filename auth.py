STAFF = {
    "teacher": {
        "password": "1234",
        "role": "teacher"
    },
    "nazem": {
        "password": "5678",
        "role": "nazem"
    },
    "moaven": {
        "password": "9999",
        "role": "moaven"
    }
}


def staff_login(username, password):
    """
    Login for teacher, nazem, and moaven.
    Returns role string if successful, None otherwise.
    """
    if username in STAFF:
        if STAFF[username]["password"] == password:
            return STAFF[username]["role"]
    return None


def teacher_login(username, password):
    role = staff_login(username, password)
    return role == "teacher"


def nazem_login(username, password):
    role = staff_login(username, password)
    return role == "nazem"


def moaven_login(username, password):
    role = staff_login(username, password)
    return role == "moaven"


def student_login(data, username, password):
    if username in data:
        if data[username]["password"] == password:
            return True
    return False


if __name__ == "__main__":
    test_data = {
        "ali": {
            "password": "1111",
            "grades": {"math": 18}
        }
    }

    print("--- Staff Login Tests ---")
    print(staff_login("teacher", "1234"))   # teacher
    print(staff_login("nazem", "5678"))     # nazem
    print(staff_login("moaven", "9999"))    # moaven
    print(staff_login("nazem", "wrong"))    # None

    print("--- Student Login Tests ---")
    print(student_login(test_data, "ali", "1111"))   # True
    print(student_login(test_data, "ali", "wrong"))  # False
