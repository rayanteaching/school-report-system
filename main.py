import tkinter as tk
from tkinter import ttk, messagebox
from data import load_data, save_data


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


