import tkinter as tk
from tkinter import ttk, messagebox
from data import load_data, save_data
from add_student_ui import show_add_student_form
from grade_ui import show_add_grade_form
from login_ui import show_login_screen
from report_ui import show_report_window


def main():
    students_data = load_data()

    root = tk.Tk()
    root.title("School Report System")
    root.geometry("450x450")
    root.configure(bg="#f0f4fa")

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure(
        "Title.TLabel",
        font=("Segoe UI", 18, "bold"),
        foreground="#2c3e50",
        background="#f0f4fa"
    )
    style.configure(
        "Dashboard.TButton",
        font=("Segoe UI", 10),
        padding=8,
        width=24
    )

    header_frame = tk.Frame(root, bg="#f0f4fa")
    header_frame.pack(pady=(20, 10))

    title_label = ttk.Label(
        header_frame,
        text="School Report System",
        style="Title.TLabel"
    )
    title_label.pack()

    middle_frame = tk.Frame(root, bg="#f0f4fa")
    middle_frame.pack(expand=True, fill="both", pady=15, padx=30)

    status_var = tk.StringVar(value="Ready")
    status_frame = tk.Frame(root, bg="#dfe6e9")
    status_frame.pack(side="bottom", fill="x")
    status_label = tk.Label(
        status_frame,
        textvariable=status_var,
        font=("Segoe UI", 9),
        bg="#dfe6e9",
        fg="#2c3e50",
        anchor="w",
        padx=10,
        pady=4,
        relief="sunken",
        bd=1
    )
    status_label.pack(fill="x")

    # --- مرحله 2: وضعیت ساده برای کاربر فعلی ---
    session = {
        "username": None,
        "role": None
    }

    def update_status(message):
        status_var.set(message)

    # --- مرحله 3: clear_screen رنگ اصلی را هم برمی‌گرداند ---
    def clear_screen():
        middle_frame.configure(bg="#f0f4fa")
        for widget in middle_frame.winfo_children():
            widget.destroy()

    def save_with_feedback():
        result = save_data(students_data)
        if result is False:
            update_status("Error while saving data")
            messagebox.showerror("Save Error", "Data could not be saved.")
        else:
            update_status("Data saved successfully")
            messagebox.showinfo("Success", "Data saved successfully.")

    def show_student_report(username):
        show_report_window(
            parent=middle_frame,
            data=students_data,
            username=username,
            on_back=show_student_dashboard_wrapper,
            update_status=update_status
        )

    def show_student_dashboard_wrapper():
        # دکمه Back گزارش، برمی‌گردد به dashboard دانش‌آموز همان کاربر لاگین‌شده
        show_student_dashboard(session["username"])

    # --- مرحله 4: صفحه اول برنامه Login است ---
    def show_login_page():
        clear_screen()
        update_status("Please login")

        show_login_screen(
            parent=middle_frame,
            data=students_data,
            on_teacher_success=handle_teacher_login_success,
            on_student_success=handle_student_login_success,
            update_status=update_status
        )

    # --- مرحله 5: بعد از Login موفق Teacher ---
    def handle_teacher_login_success():
        session["username"] = "teacher"
        session["role"] = "teacher"

        update_status("Teacher logged in successfully")
        show_teacher_dashboard()

    # --- مرحله 6: بعد از Login موفق Student ---
    def handle_student_login_success(username):
        session["username"] = username
        session["role"] = "student"

        update_status(f"Student logged in successfully: {username}")
        show_student_dashboard(username)

    # --- مرحله 7: Dashboard مخصوص Teacher ---
    def show_teacher_dashboard():
        clear_screen()

        title_label = tk.Label(
            middle_frame,
            text="Teacher Dashboard",
            font=("Segoe UI", 13, "bold"),
            bg="#f0f4fa",
            fg="#2c3e50"
        )
        title_label.pack(pady=(0, 15))

        ttk.Button(
            middle_frame,
            text="Add Student",
            style="Dashboard.TButton",
            command=lambda: show_add_student_form(
                parent=middle_frame,
                data=students_data,
                on_back=show_teacher_dashboard,
                update_status=update_status
            )
        ).pack(pady=5)

        ttk.Button(
            middle_frame,
            text="Add Grade",
            style="Dashboard.TButton",
            command=lambda: show_add_grade_form(
                parent=middle_frame,
                data=students_data,
                on_back=show_teacher_dashboard,
                update_status=update_status
            )
        ).pack(pady=5)

        # انتخاب دانش‌آموز برای Teacher هنوز آماده نیست -> پیام واضح، نه سکوت
        ttk.Button(
            middle_frame,
            text="View Report",
            style="Dashboard.TButton",
            command=lambda: update_status("Teacher report view is not complete yet")
        ).pack(pady=5)

        ttk.Button(
            middle_frame,
            text="Save Data",
            style="Dashboard.TButton",
            command=save_with_feedback
        ).pack(pady=5)

        ttk.Button(
            middle_frame,
            text="Logout",
            style="Dashboard.TButton",
            command=logout
        ).pack(pady=5)

        update_status("Teacher logged in successfully")

    # --- مرحله 8: Dashboard ساده برای Student ---
    def show_student_dashboard(username):
        clear_screen()

        title_label = tk.Label(
            middle_frame,
            text=f"Student Dashboard: {username}",
            font=("Segoe UI", 13, "bold"),
            bg="#f0f4fa",
            fg="#2c3e50"
        )
        title_label.pack(pady=(0, 15))

        ttk.Button(
            middle_frame,
            text="View My Report",
            style="Dashboard.TButton",
            command=lambda: show_student_report(username)
        ).pack(pady=5)

        ttk.Button(
            middle_frame,
            text="Logout",
            style="Dashboard.TButton",
            command=logout
        ).pack(pady=5)

    # --- مرحله 9: Logout ---
    def logout():
        session["username"] = None
        session["role"] = None

        update_status("Logged out")
        show_login_page()

    # --- مرحله 10: شروع برنامه با Login ---
    show_login_page()
    root.mainloop()


if __name__ == "__main__":
    main()