import tkinter as tk
from tkinter import ttk, messagebox
from students import add_student
from data import save_data


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_add_student_form(parent, data, on_back=None, update_status=None):
    clear_frame(parent)

    title_label = tk.Label(
        parent,
        text="Add Student",
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

    def clear_entries():
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        username_entry.focus()

    def handle_add_student():
        username = username_entry.get().strip()
        password = password_entry.get()

        if username == "" or password == "":
            messagebox.showerror("Input Error", "Please fill all fields")
            clear_entries()
            if update_status:
                update_status("Add student failed")
            return

        if username in data:
            messagebox.showerror("Input Error", "This username already exists")
            clear_entries()
            if update_status:
                update_status("Duplicate username")
            return

        add_student(data, username, password)
        save_data(data)
        messagebox.showinfo("Success", "Student added successfully")

        clear_entries()

        if update_status:
            update_status("Student added successfully")

    add_button = ttk.Button(
        parent,
        text="Add Student",
        command=handle_add_student
    )
    add_button.pack(pady=10)

    back_button = ttk.Button(
        parent,
        text="Back",
        command=on_back
    )
    back_button.pack(pady=5)

    username_entry.focus()


def run_test_window():
    root = tk.Tk()
    root.title("Add Student Test")
    root.geometry("350x350")

    test_data = {}

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

        open_form_button = ttk.Button(
            main_frame,
            text="Open Add Student Form",
            command=lambda: show_add_student_form(
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
