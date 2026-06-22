import tkinter as tk
from tkinter import ttk, messagebox
from grades import add_grade
from data import save_data


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_add_grade_form(parent, data, on_back=None, update_status=None):
    clear_frame(parent)

    title_label = tk.Label(
        parent,
        text="Add Grade",
        font=("Segoe UI", 16, "bold")
    )
    title_label.pack(pady=10)

    username_label = tk.Label(parent, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(parent, width=30)
    username_entry.pack(pady=5)

    subject_label = tk.Label(parent, text="Subject:")
    subject_label.pack()
    subject_entry = tk.Entry(parent, width=30)
    subject_entry.pack(pady=5)

    grade_label = tk.Label(parent, text="Grade:")
    grade_label.pack()
    grade_entry = tk.Entry(parent, width=30)
    grade_entry.pack(pady=5)

    def clear_entries():
        username_entry.delete(0, tk.END)
        subject_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
        username_entry.focus()

    def handle_add_grade():
        username = username_entry.get().strip()
        subject = subject_entry.get().strip()
        grade_text = grade_entry.get().strip()

        if username == "" or subject == "" or grade_text == "":
            messagebox.showerror("Input Error", "Please fill all fields")
            clear_entries()
            if update_status:
                update_status("Add grade failed")
            return

        if username not in data:
            messagebox.showerror("Input Error", "Student not found")
            clear_entries()
            if update_status:
                update_status("Student not found")
            return

        try:
            grade = float(grade_text)
        except ValueError:
            messagebox.showerror("Input Error", "Grade must be a number")
            grade_entry.delete(0, tk.END)
            grade_entry.focus()
            if update_status:
                update_status("Invalid grade")
            return

        if grade < 0 or grade > 20:
            messagebox.showerror("Input Error", "Grade must be between 0 and 20")
            grade_entry.delete(0, tk.END)
            grade_entry.focus()
            if update_status:
                update_status("Grade out of range")
            return

        add_grade(data, username, subject, grade)
        save_data(data)
        messagebox.showinfo("Success", "Grade added successfully")
        clear_entries()

        if update_status:
            update_status("Grade added successfully")

    add_button = ttk.Button(
        parent,
        text="Add Grade",
        command=handle_add_grade
    )
    add_button.pack(pady=10)

    if on_back is not None:
        back_button = ttk.Button(
            parent,
            text="Back",
            command=on_back
        )
        back_button.pack(pady=5)

    username_entry.focus()


def run_test_window():
    root = tk.Tk()
    root.title("Add Grade Test")
    root.geometry("350x400")

    test_data = {
        "ali": {
            "password": "1111",
            "grades": {}
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

    def show_home_page():
        clear_frame(main_frame)

        label = tk.Label(
            main_frame,
            text="Home Page",
            font=("Segoe UI", 14, "bold")
        )
        label.pack(pady=20)

        info_label = tk.Label(
            main_frame,
            text="Test student: ali / 1111",
            font=("Segoe UI", 10)
        )
        info_label.pack(pady=5)

        open_form_button = ttk.Button(
            main_frame,
            text="Open Add Grade Form",
            command=lambda: show_add_grade_form(
                parent=main_frame,
                data=test_data,
                on_back=show_home_page,
                update_status=update_status
            )
        )
        open_form_button.pack(pady=10)

    show_home_page()
    root.mainloop()


if __name__ == "__main__":
    run_test_window()
