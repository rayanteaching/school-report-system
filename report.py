from grades import calculate_average

def generate_report(data, username):
    
    if username not in data:
        return "Student not found"
    
    report_text = f"Report Card for {username}\n\n"
    
    grades = data[username]["grades"]
 
    for subject, grade in grades.items():
        report_text += f"{subject}: {grade}\n"
 
    average = calculate_average(data, username)
 
    report_text += f"\nAverage: {average}"
 
    return report_text
    
if __name__ == "__main__":
    test_data = {
            "ali": {
                "password": "1111",
                "grades": {
                    "math": 18,
                    "science": 19,
                    "english": 17
                    }
                }
            }
    print(generate_report(test_data, "ali"))

