def teacher_login(username, password):
    teacher_username = "teacher"
    teacher_password = "1234"
    if username == teacher_username and password == teacher_password:
        return True
    else:
        return False
def student_login(data, username, password):

    if username in data:
        # اگر رمز درست بود برگردان True
        if data[username]["password"] == password:
            return True
        # اگر رمز اشتباه بود، همین‌جا False را برگردان
        else:
            return False
    return False # اگر یوزرنیم اصلاً در دیتابیس نبود


if __name__ == "__main__":
    test_data = {
        "ali": {
            "password": "1111",
            "grades": {
        "math": 18 }}}
    print(teacher_login("teacher", "1234"))
    print(teacher_login("teacher", "wrong"))
    print(student_login(test_data, "ali", "1111"))
    print(student_login(test_data, "ali", "wrong"))


