def teacher_login(username, password):
    """
    Check teacher username and password.
    Returns True if login is correct, otherwise returns False.
    """
    teacher_username = "teacher"
    teacher_password = "1234"
    if username == teacher_username and password == teacher_password:
        return True
    else:
        return False
def student_login(data, username, password):
    """
    Check student username and password.
    data is a dictionary that contains all students.
    Returns True if login is correct, otherwise returns False.
    """
    if username in data:
        if data[username]["password"] == password:
            return True
            return False

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
    print(student_login(test_data, "ali", "wrong"))

