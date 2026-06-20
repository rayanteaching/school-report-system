import tkinter as tk
from tkinter import messagebox
# .....guys_files..... (برای سازگاری با پروژه اصلی نگه داشته شده)
#from auth import teacher_login, student_login
from students import add_student
from grades import add_grade
from report import generate_report
from data import load_data, save_data

<<<<<<< HEAD
# .......main.........
=======

>>>>>>> 6659a77 (Connect Save Data button to save_with_feedback)
def main():
    root = tk.Tk()
    root.title("School Report System")
    root.geometry("400x400")

    title_label = tk.Label(root, text="School Report System", font=("Arial", 16))
    title_label.pack(pady=10)

    # ---------- فریم میانی (محتوای اصلی که پاک میشود) ----------
    middle_frame = tk.Frame(root)
    middle_frame.pack(expand=True, fill='both', pady=10)

    # ---------- بارگذاری داده‌ها هنگام شروع برنامه ----------
    students_data = load_data()

    # ---------- نوار وضعیت (پایین پنجره) ----------
    status_frame = tk.Frame(root)
    status_frame.pack(side='bottom', fill='x', pady=5)

    status_label = tk.Label(
        status_frame,
        text="Ready",
        relief='sunken',
        anchor='w'
    )
    status_label.pack(fill='x')

    def update_status(message):
        """نمایش پیام وضعیت در نوار پایین پنجره"""
        status_label.config(text=message)

    def save_with_feedback():
        """
        ذخیره داده‌ها و نمایش پیام وضعیت مناسب.
        این تابع باید بعد از هر تغییر در داده‌ها (ثبت دانش‌آموز، ثبت نمره و ...) صدا زده شود.
        """
        if save_data(students_data):
            update_status("Data saved successfully")
        else:
            update_status("Error while saving data")

    def clear_screen():
        """حذف تمام ویجتهای موجود در فریم میانی"""
        for widget in middle_frame.winfo_children():
            widget.destroy()

    def show_dashboard():
        clear_screen()

        # دکمهها (فقط ظاهر، بدون عملکرد)
        btn_add_student = tk.Button(middle_frame, text="Add Student", width=20)
        btn_add_student.pack(pady=5)

        btn_add_grade = tk.Button(middle_frame, text="Add Grade", width=20)
        btn_add_grade.pack(pady=5)

        btn_view_report = tk.Button(middle_frame, text="View Report", width=20)
        btn_view_report.pack(pady=5)

        btn_save_data = tk.Button(
            middle_frame,
            text="Save Data",
            width=20,
            command=save_with_feedback
        )
        btn_save_data.pack(pady=5)

        btn_logout = tk.Button(middle_frame, text="Logout", width=20)
        btn_logout.pack(pady=5)

    show_dashboard()

    # نمایش پیام مربوط به نتیجه بارگذاری داده‌ها
    if students_data:
        update_status("Data loaded successfully")
    else:
        update_status("Ready")

    root.mainloop()


if __name__ == "__main__":
    main()

