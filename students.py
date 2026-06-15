def add_student(data, username, password):
    """
    Add a new student to the data dictionary.
    Parameters:
        data: dictionary of all students
        username: new student's username
        password: new student's password
    Returns:
        updated data dictionary
    """
    if username in data:
        return data
    data[username] = {
    "password": password,
    "grades": {}
    }
    return data

if __name__ == "__main__":
    students_data = {}
    students_data = add_student(students_data, "ali",
"1111")
    students_data = add_student(students_data, "sara",
"2222")
    print(students_data)
