import tkinter as tk
from tkinter import ttk, messagebox
from auth import teacher_login, student_login
from students import add_student
from grades import add_grade
from report import generate_report
from data import load_data, save_data

def main():
    root = tk.Tk()
    root.title("School Report System")
    root.geometry("450x450")
    root.configure(bg='#f0f4fa')  
    style = ttk.Style()
    style.theme_use('clam') 
    style.configure('Title.TLabel',
                    font=('Segoe UI', 18, 'bold'),
                    foreground='#2c3e50',
                    background='#f0f4fa')
    style.configure('TButton',
                    font=('Segoe UI', 10),
                    padding=8,
                    relief='flat',
                    background='#ffffff',
                    foreground='#2c3e50',
                    borderwidth=1,
                    focusthickness=0,
                    focuscolor='none')
    style.map('TButton',
              background=[('active', '#d9e2ef'), ('pressed', '#b0c4de')],
              foreground=[('active', '#1a2634')])

    style.configure('AddStudent.TButton', background='#27ae60', foreground='white')
    style.map('AddStudent.TButton',
              background=[('active', '#2ecc71'), ('pressed', '#1e8449')])

    style.configure('AddGrade.TButton', background='#2980b9', foreground='white')
    style.map('AddGrade.TButton',
              background=[('active', '#3498db'), ('pressed', '#1f618d')])

    style.configure('ViewReport.TButton', background='#8e44ad', foreground='white')
    style.map('ViewReport.TButton',
              background=[('active', '#9b59b6'), ('pressed', '#6c3483')])

    style.configure('SaveData.TButton', background='#f39c12', foreground='white')
    style.map('SaveData.TButton',
              background=[('active', '#f1c40f'), ('pressed', '#d68910')])

    style.configure('Logout.TButton', background='#e74c3c', foreground='white')
    style.map('Logout.TButton',
              background=[('active', '#ec7063'), ('pressed', '#b03a2e')])
    header_frame = tk.Frame(root, bg='#f0f4fa')
    header_frame.pack(pady=(20, 10))

    title_label = ttk.Label(
        header_frame,
        text="📚 School Report System",
        style='Title.TLabel'
    )
    title_label.pack()
    middle_frame = tk.Frame(root, bg='#f0f4fa')
    middle_frame.pack(expand=True, fill='both', pady=15, padx=30)
    status_frame = tk.Frame(root, bg='#dfe6e9')
    status_frame.pack(side='bottom', fill='x', pady=(0, 5))

    status_label = tk.Label(
        status_frame,
        text="✅ Ready",
        font=('Segoe UI', 9),
        bg='#dfe6e9',
        fg='#2c3e50',
        anchor='w',
        padx=10,
        pady=3,
        relief='sunken',
        bd=1
    )
    status_label.pack(fill='x')

    def clear_screen():
        for widget in middle_frame.winfo_children():
            widget.destroy()

    def show_dashboard():
        clear_screen()
        btn_add_student = ttk.Button(
            middle_frame,
            text="➕ Add Student",
            style='AddStudent.TButton',
            width=20
        )
        btn_add_student.pack(pady=6)

        btn_add_grade = ttk.Button(
            middle_frame,
            text="📝 Add Grade",
            style='AddGrade.TButton',
            width=20
        )
        btn_add_grade.pack(pady=6)

        btn_view_report = ttk.Button(
            middle_frame,
            text="📊 View Report",
            style='ViewReport.TButton',
            width=20
        )
        btn_view_report.pack(pady=6)

        btn_save_data = ttk.Button(
            middle_frame,
            text="💾 Save Data",
            style='SaveData.TButton',
            width=20
        )
        btn_save_data.pack(pady=6)

        btn_logout = ttk.Button(
            middle_frame,
            text="🚪 Logout",
            style='Logout.TButton',
            width=20
        )
        btn_logout.pack(pady=6)
    show_dashboard()

    root.mainloop()

if __name__ == "__main__":
    main()