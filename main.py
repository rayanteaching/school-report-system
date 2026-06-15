import tkinter as tk 
from tkinter import messagebox
#.....guys_files.....
# from auth import teacher_login, student_login
# from students import add_student
# from grades import add_grade
# from report import generate_report
# from data import load_data, save_data
#.......main.........
def main():
    root = tk.Tk()
    root.title("School Report System")
    root.geometry("400x300")

    title_label = tk.Label(root, text="School Report System", font=("Arial", 16))
    title_label.pack(pady=20)

    info_label = tk.Label(
        root,
        text="Main interface will be completed after other
        modules are merged.",
        wraplength=300)
    info_label.pack(pady=20)

    root.mainloop()
if __name__ == "__main__": 
    main()

