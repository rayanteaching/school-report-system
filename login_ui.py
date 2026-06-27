import tkinter as tk
from tkinter import ttk, messagebox
from auth import teacher_login, student_login



def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_login_screen(
    parent,
    data,
    on_teacher_success=None,
    on_student_success=None,
    update_status=None
):
    clear_frame(parent)

    title_label = tk.Label(
        parent,
        text="Login",
        font=("Segoe UI", 16, "bold")
    )
    title_label.pack(pady=10)

    username_label = tk.Label(parent, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(parent, width=30)
    username_entry.pack(pady=5)

    password_label = tk.Label(parent, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(parent, width=30, show="*")
    password_entry.pack(pady=5)

    role_var = tk.StringVar(value="Teacher")
    role_frame = tk.Frame(parent)
    role_frame.pack(pady=10)

    teacher_radio = tk.Radiobutton(
        role_frame,
        text="Teacher",
        variable=role_var,
        value="Teacher"
    )
    teacher_radio.pack(side="left", padx=10)

    student_radio = tk.Radiobutton(
        role_frame,
        text="Student",
        variable=role_var,
        value="Student"
    )
    student_radio.pack(side="left", padx=10)

    def clear_entries():
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        username_entry.focus()

    def handle_login():
        username = username_entry.get().strip()
        password = password_entry.get()
        role = role_var.get()

        if username == "" or password == "":
            messagebox.showerror("Login Error", "Please fill all fields")
            clear_entries()
            if update_status:
                update_status("Login failed")
            return

        if role == "Teacher":
            login_success = teacher_login(username, password)
            if login_success:
                if update_status:
                    update_status("Teacher login successful")
                if on_teacher_success:
                    on_teacher_success()
                return

        if role == "Student":
            login_success = student_login(data, username, password)
            if login_success:
                if update_status:
                    update_status("Student login successful")
                if on_student_success:
                    on_student_success(username)
                return

        messagebox.showerror("Login Error", "Invalid username or password")
        clear_entries()
        if update_status:
            update_status("Login failed")

    login_button = ttk.Button(
        parent,
        text="Login",
        command=handle_login
    )
    login_button.pack(pady=10)

    username_entry.focus()


def run_test_window():
    root = tk.Tk()
    root.title("Login Test")
    root.geometry("350x350")

    test_data = {
        "ali": {
            "password": "1111",
            "grades": {
                "math": 18
            }
        }
    }

    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)

    status_var = tk.StringVar(value="Ready")
    status_label = tk.Label(
        root,
        textvariable=status_var,
        relief="sunken",
        anchor="w"
    )
    status_label.pack(side="bottom", fill="x")

    def update_status(message):
        status_var.set(message)

    def show_teacher_page():
        clear_frame(main_frame)
        label = tk.Label(
            main_frame,
            text="Teacher login successful",
            font=("Segoe UI", 12, "bold")
        )
        label.pack(pady=20)

    def show_student_page(username):
        clear_frame(main_frame)
        label = tk.Label(
            main_frame,
            text=f"Student login successful: {username}",
            font=("Segoe UI", 12, "bold")
        )
        label.pack(pady=20)

    show_login_screen(
        parent=main_frame,
        data=test_data,
        on_teacher_success=show_teacher_page,
        on_student_success=show_student_page,
        update_status=update_status
    )

    root.mainloop()


if __name__ == "__main__":
    run_test_window()