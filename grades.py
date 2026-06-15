def add_grade(data, username, subject, grade):
    """
    Add or update a grade for a student.
    Parameters:
    data: students dictionary
    username: student's username
    subject: lesson name
    grade: lesson grade
    Returns:
    updated data dictionary
    """
    if username not in data:
        return data
    data[username]["grades"][subject] = grade
    return data

#_______________________________________________________

def calculate_average(data, username):
    """
    Calculate student's average grade.
    Parameters:
    data: students dictionary
    username: student's username
    Returns:
    average grade
    """
    if username not in data:
        return 0
    grades = data[username]["grades"]
    if len(grades) == 0:
        return 0
    total = sum(grades.values())
    average = total / len(grades)
    return round(average, 2)

#TEST_____________________________________________________TEST

#if __name__ == "__main__":
 #   students_data = {
 #       "ali": {
 #           "password": "1111",
 #           "grades": {}
 #       }
 #   }
 #   add_grade(students_data, "ali", "math", 18)
 #   add_grade(students_data, "ali", "science", 20)
 #   add_grade(students_data, "ali", "english", 16)
 #   print(students_data)
 #   print(calculate_average(students_data, "ali"))
 
