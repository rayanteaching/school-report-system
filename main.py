import tkinter as tk 
from tkinter import messagebox
#.....guys_files.....
from auth import teacher_login, student_login
from students import add_student
from grades import add_grade
from report import generate_report
from data import load_data, save_data
#.......main.........
def main():
    root = tk.Tk()
    root.title("School Report System")
    root.geometry("400x300")
    
    global students_data
    students_data = load_data()

    title_label = tk.Label(root, text="School Report System", font=("Arial", 16))
    title_label.pack(pady=20)

    info_label = tk.Label(
        root,
        text="Main interface will be completed after other modules are merged.",
        wraplength=300)
    info_label.pack(pady=20)
    
def show_grade_entry_window(username):
    grade_window = tk.Toplevel()
    grade_window.title("Add Grade")
    grade_window.geometry("300x200")

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

        if grade_numeric < 0 or grade_numeric > 20:
            messagebox.showerror("Error", "Grade must be between 0 and 20")
            return

        # بارگزاری داده‌ها
        data = load_data()

        # بررسی وجود دانش‌آموز
        if user not in data:
            messagebox.showerror("Error", "Student not found")
            return
        
        # ثبت نمره
        data = add_grade(data, user, subject, grade_numeric)
        save_data(data)

        messagebox.showinfo("Success", "Grade added successfully")
        grade_window.destroy()  # بستن پنجره

    # ساخت ویجت‌ها
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

# در main()، بعد از تعریف ویجت‌های اصلی، یک دکمه برای نمایش فرم ثبت نمره اضافه کنید.
    tk.Button(root, text="Add Grade", command=lambda: show_grade_entry_window("teacher")).pack(pady=10)
 
    root.mainloop()
if __name__ == "__main__": 
    main()

