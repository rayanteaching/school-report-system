import tkinter as tk 
from tkinter import messagebox
#.....guys_files.....
from auth import teacher_login, student_login
from students import add_student
from grades import add_grade
from report import generate_report
from data import load_data, save_data

# --- Student 3 Task: Create add student form ---
def show_add_student_form():
    """
    Creates a GUI window for teachers to add a new student.
    As per Phase 2 requirements.
    """
    add_window = tk.Toplevel()
    add_window.title("Add Student")
    add_window.geometry("300x250")

    # Username field
    tk.Label(add_window, text="Username:").pack(pady=5)
    entry_username = tk.Entry(add_window)
    entry_username.pack(pady=5)

    # Password field (with masking for security)
    tk.Label(add_window, text="Password:").pack(pady=5)
    entry_password = tk.Entry(add_window, show="*") 
    entry_password.pack(pady=5)

    def submit_form():
        """
        Handles the logic for adding a student, including validation and error handling.
        """
        username = entry_username.get().strip()
        password = entry_password.get().strip()

        # Step 6: Error Handling & Validation
        # 1. Check if fields are empty
        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return

        try:
            # Step 5: Call existing functions to add student and save data
            success = add_student(username, password)
            
            if success:
                save_data()
                messagebox.showinfo("Success", "Student added successfully")
                add_window.destroy() # Close window after successful addition
            else:
                # 2. Check if username already exists
                messagebox.showerror("Error", "This username already exists")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Buttons: Add Student and Back
    btn_add = tk.Button(add_window, text="Add Student", command=submit_form)
    btn_add.pack(pady=10)

    btn_back = tk.Button(add_window, text="Back", command=add_window.destroy)
    btn_back.pack()
# ----------------------------------------------

#.......main.........
def main():
    root = tk.Tk()
    root.title("School Report System")
    root.geometry("400x400")

    title_label = tk.Label(root, text="School Report System", font=("Arial", 16))
    title_label.pack(pady=20)

    info_label = tk.Label(
        root,
        text="Main interface will be completed after other modules are merged.",
        wraplength=300)
    info_label.pack(pady=20)

    # --- Test Button for Student 3 Task ---
    # This button is added to test the form before the Teacher Dashboard is implemented.
    test_btn = tk.Button(
        root, 
        text="Test: Open Add Student Form", 
        command=show_add_student_form,
        bg="lightblue"
    )
    test_btn.pack(pady=20)
    # --------------------------------------

    root.mainloop()

if __name__ == "__main__": 
    main()

