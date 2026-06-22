import tkinter as tk 
from tkinter import ttk, messagebox 
from data import load_data, save_data
from auth import teacher_login, student_login
from students import add_student
from grades import add_grade
from report import generate_report
 
 
def main(): 
    data = load_data() 
 
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
        background="#f0f4fa") 
 
    style.configure( 
        "Dashboard.TButton", 
        font=("Segoe UI", 10), 
        padding=8, 
        width=22) 
 
    header_frame = tk.Frame(root, bg="#f0f4fa") 
    header_frame.pack(pady=(20, 10)) 
 
    title_label = ttk.Label( 
        header_frame, 
        text="School Report System", 
        style="Title.TLabel") 
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
        bd=1) 
    status_label.pack(fill="x") 
 
    def update_status(message): 
        status_var.set(message) 
 
    def clear_screen(): 
        for widget in middle_frame.winfo_children(): 
            widget.destroy() 
 
    def show_placeholder(title, message): 

 
        clear_screen() 
 
        page_title = tk.Label( 
            middle_frame, 
            text=title, 
            font=("Segoe UI", 14, "bold"), 
            bg="#f0f4fa", 
            fg="#2c3e50") 
        page_title.pack(pady=10) 
 
        info_label = tk.Label( 
            middle_frame, 
            text=message, 
            font=("Segoe UI", 10), 
            bg="#f0f4fa", 
            fg="#2c3e50", 
            wraplength=320) 
        info_label.pack(pady=10) 
 
        back_button = ttk.Button( 
            middle_frame, 
            text="Back to Dashboard", 
            style="Dashboard.TButton", 
            command=show_dashboard) 
 
        back_button.pack(pady=10) 
 
        update_status(title) 
 
    def save_with_feedback(): 
        try: 
            save_data(data) 
            update_status("Data saved successfully") 
        except Exception as error: 
            update_status("Error while saving data") 
            messagebox.showerror("Save Error", str(error)) 
 
    def show_dashboard(): 
        clear_screen() 
 
        dashboard_label = tk.Label( 
            middle_frame, 
            text="Main Dashboard", 
            font=("Segoe UI", 13, "bold"), 
            bg="#f0f4fa", 
            fg="#2c3e50") 
        dashboard_label.pack(pady=(0, 15)) 
 
        add_student_button = ttk.Button( 
 
            middle_frame, 
            text="Add Student", 
            style="Dashboard.TButton", 
            command=lambda: show_placeholder( 
                "Add Student", 
                "This form will be completed by Student 3.")) 
        add_student_button.pack(pady=5) 
 
        add_grade_button = ttk.Button( 
            middle_frame, 
            text="Add Grade", 
            style="Dashboard.TButton", 
            command=lambda: show_placeholder( 
                "Add Grade", 
                "This form will be completed by Student 4.")) 
        add_grade_button.pack(pady=5) 
 
        view_report_button = ttk.Button( 
            middle_frame, 
            text="View Report", 
            style="Dashboard.TButton", 
            command=lambda: show_placeholder( 
                "View Report", 
                "This section will be completed by Student 5."))  
 
        view_report_button.pack(pady=5) 
 
        save_data_button = ttk.Button( 
            middle_frame, 
            text="Save Data", 
            style="Dashboard.TButton", 
            command=save_with_feedback) 
        save_data_button.pack(pady=5) 
 
        logout_button = ttk.Button( 
            middle_frame, 
            text="Logout", 
            style="Dashboard.TButton", 
            command=lambda: show_placeholder( 
                "Login", 
                "The login screen will be completed by Student 2.")) 
        logout_button.pack(pady=5) 
 
        update_status("Ready") 
 
    show_dashboard() 
    root.mainloop() 
 
 
if __name__ == "__main__": 
    main() 

