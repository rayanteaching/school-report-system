import tkinter as tk
from tkinter import simpledialog
from report import generate_report


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_report_window(
    parent,
    data,
    username=None,
    on_back=None,
    update_status=None
):
    clear_frame(parent)

    if username is None:
        username = simpledialog.askstring(
            "View Report",
            "Enter student username:"
        )

        if not username:
            if update_status:
                update_status("Report cancelled")
            return

    title_label = tk.Label(
        parent,
        text="Report Card",
        font=("Segoe UI", 16, "bold")
    )
    title_label.pack(pady=10)

    report_box = tk.Text(
        parent,
        width=50,
        height=18,
        font=("Consolas", 10),
        wrap="word"
    )
    report_box.pack(
        padx=10,
        pady=10,
        fill="both",
        expand=True
    )

    if username not in data:
        report_text = "Student not found"

    else:
        grades = data[username]["grades"]

        if len(grades) == 0:
            report_text = (
                "Report Card\n"
                "--------------------\n"
                f"Student: {username}\n\n"
                "No grades available."
            )

        else:
            report_text = generate_report(
                data,
                username
            )

    report_box.config(state="normal")
    report_box.delete("1.0", tk.END)
    report_box.insert(
        tk.END,
        report_text
    )
    report_box.config(
        state="disabled"
    )

    button_frame = tk.Frame(parent)
    button_frame.pack(pady=5)

    back_button = tk.Button(
        button_frame,
        text="Back",
        command=(
            on_back
            if on_back
            else lambda: None
        )
    )
    back_button.pack(
        side="left",
        padx=5
    )

    exit_button = tk.Button(
        button_frame,
        text="Exit",
        command=parent.winfo_toplevel().destroy
    )
    exit_button.pack(
        side="left",
        padx=5
    )

    if update_status:
        update_status(
            "Report displayed"
        )


def run_test_window():

    root = tk.Tk()
    root.title("Report View Test")
    root.geometry("420x430")

    test_data = {
        "ali": {
            "password": "1111",
            "grades": {
                "math": 18,
                "science": 19,
                "english": 17
            }
        },

        "sara": {
            "password": "2222",
            "grades": {}
        }
    }

    main_frame = tk.Frame(root)
    main_frame.pack(
        expand=True,
        fill="both",
        padx=20,
        pady=20
    )

    status_var = tk.StringVar(
        value="Ready"
    )

    status_label = tk.Label(
        root,
        textvariable=status_var,
        relief="sunken",
        anchor="w"
    )
    status_label.pack(
        side="bottom",
        fill="x"
    )

    def update_status(message):
        status_var.set(message)


    def show_home_page():

        clear_frame(main_frame)

        title = tk.Label(
            main_frame,
            text="report test menu",
            font=("Segoe UI", 14, "bold")
        )
        title.pack(
            pady=15
        )


        ali_button = tk.Button(
            main_frame,
            text="Show ali report",
            command=lambda: show_report_window(
                parent=main_frame,
                data=test_data,
                username="ali",
                on_back=show_home_page,
                update_status=update_status
            )
        )

        ali_button.pack(
            pady=5
        )


        sara_button = tk.Button(
            main_frame,
            text="Show sara report",
            command=lambda: show_report_window(
                parent=main_frame,
                data=test_data,
                username="sara",
                on_back=show_home_page,
                update_status=update_status
            )
        )

        sara_button.pack(
            pady=5
        )


        reza_button = tk.Button(
            main_frame,
            text="Show reza report",
            command=lambda: show_report_window(
                parent=main_frame,
                data=test_data,
                username="reza",
                on_back=show_home_page,
                update_status=update_status
            )
        )

        reza_button.pack(
            pady=5
        )


    show_home_page()

    root.mainloop()


if __name__ == "__main__":
    run_test_window()