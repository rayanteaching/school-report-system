import tkinter as tk 
from tkinter import messagebox

from grades import add_grade as add_grade_logic 
from data import load_data, save_data

def show_grade_entry_window(): 
    grade_window = tk.Toplevel()
    grade_window.title("Add Grade")
    grade_window.geometry("300x250")

    def submit_grade(): 
        user = username_entry.get()
        subject = subject_entry.get()
        grade = grade_entry.get()

        if not user or not subject or not grade:
            messagebox.showerror("Error", "Please fill all fields")
            return

        try:
            grade_numeric = float(grade)
        except ValueError:
            messagebox.showerror("Error", "Grade must be a number")
            return

        if not (0 <= grade_numeric <= 20):
            messagebox.showerror("Error", "Grade must be between 0 and 20")
            return

        data = load_data()
        if user not in data:
            messagebox.showerror("Error", "Student not found")
            return
        
        
        data = add_grade_logic(data, user, subject, grade_numeric)
        save_data(data)
        messagebox.showinfo("Success", "Grade added successfully")
        grade_window.destroy()  

    tk.Label(grade_window, text="Username:").pack()
    username_entry = tk.Entry(grade_window)
    username_entry.pack()

    tk.Label(grade_window, text="Subject:").pack()
    subject_entry = tk.Entry(grade_window)
    subject_entry.pack()

    tk.Label(grade_window, text="Grade:").pack()
    grade_entry = tk.Entry(grade_window)
    grade_entry.pack()

    tk.Button(grade_window, text="Add Grade", command=submit_grade).pack(pady=10)
    tk.Button(grade_window, text="Back", command=grade_window.destroy).pack(pady=5)

def main():
    root = tk.Tk()
    root.title("School Report System")
    root.geometry("400x300")

    tk.Label(root, text="School Report System", font=("Arial", 16)).pack(pady=20)
    
    
    tk.Button(root, text="Add Grade", command=show_grade_entry_window).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__": 
    main()
