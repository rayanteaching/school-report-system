import json
FILE_NAME = "students_data.json"
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
        
def load_data(): 
    try: 
        with open(FILE_NAME, "r") as file: 
            return json.load(file) 
    except FileNotFoundError: 
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
 
    save_data(students_data) 
 
    loaded_data = load_data() 
 
    print(loaded_data)
