import tkinter as tk
from tkinter import messagebox
from auth import teacher_login, student_login
from students import add_student
from grades import add_grade
from report import generate_report
from data import load_data, save_data

def main():
    root = tk.Tk()
    root.title("School Report System")
    root.geometry("400x400")
    header_frame = tk.Frame(root)
    header_frame.pack(pady=10)

    title_label = tk.Label(
        header_frame,
        text="School Report System",
        font=("Arial", 16, "bold")
    )
    title_label.pack()
    middle_frame = tk.Frame(root)
    middle_frame.pack(expand=True, fill='both', pady=10)
    status_frame = tk.Frame(root)
    status_frame.pack(side='bottom', fill='x', pady=5)

    status_label = tk.Label(
        status_frame,
        text="Ready",
        relief='sunken',
        anchor='w'
    )
    status_label.pack(fill='x')

    def clear_screen():
        for widget in middle_frame.winfo_children():
            widget.destroy()

    def show_dashboard():
        clear_screen()  
        btn_add_student = tk.Button(middle_frame, text="Add Student", width=20)
        btn_add_student.pack(pady=5)

        btn_add_grade = tk.Button(middle_frame, text="Add Grade", width=20)
        btn_add_grade.pack(pady=5)

        btn_view_report = tk.Button(middle_frame, text="View Report", width=20)
        btn_view_report.pack(pady=5)

        btn_save_data = tk.Button(middle_frame, text="Save Data", width=20)
        btn_save_data.pack(pady=5)

        btn_logout = tk.Button(middle_frame, text="Logout", width=20)
        btn_logout.pack(pady=5)


    show_dashboard()

    
    root.mainloop()

if __name__ == "__main__":
    main()

