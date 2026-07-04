import tkinter as tk
from tkinter import ttk, messagebox
from auth import teacher_login, student_login

# ─── Color Palette ────────────────────────────────────────────────
BG_MAIN       = "#1e2a3a"   # پس‌زمینه اصلی — آبی تیره
BG_CARD       = "#253447"   # کارت لاگین
BG_INPUT      = "#2e3f55"   # فیلد ورودی
ACCENT        = "#4f8ef7"   # آبی روشن — دکمه و تاکید
ACCENT_HOVER  = "#3a6fd8"
TEXT_PRIMARY  = "#e8edf3"   # متن اصلی
TEXT_MUTED    = "#8a9bb0"   # متن کم‌رنگ
SUCCESS_COLOR = "#2ecc71"
ERROR_COLOR   = "#e74c3c"
BORDER_COLOR  = "#3a5068"
# ──────────────────────────────────────────────────────────────────


def clear_frame(frame: tk.Frame) -> None:
    """Remove all widgets from the given frame."""
    for widget in frame.winfo_children():
        widget.destroy()


def _make_styled_entry(parent: tk.Frame, show: str = "") -> tk.Entry:
    """Return a styled Entry widget consistent with the app theme."""
    entry = tk.Entry(
        parent,
        show=show,
        font=("Segoe UI", 11),
        bg=BG_INPUT,
        fg=TEXT_PRIMARY,
        insertbackground=TEXT_PRIMARY,
        relief="flat",
        bd=0,
        highlightthickness=1,
        highlightbackground=BORDER_COLOR,
        highlightcolor=ACCENT,
        width=28,
    )
    return entry


def _make_label(parent: tk.Widget, text: str, small: bool = False) -> tk.Label:
    """Return a styled Label widget."""
    size = 9 if small else 10
    return tk.Label(
        parent,
        text=text,
        font=("Segoe UI", size),
        bg=BG_CARD,
        fg=TEXT_MUTED if small else TEXT_PRIMARY,
        anchor="w",
    )


def show_login_screen(
    parent: tk.Frame,
    data: dict,
    on_teacher_success=None,
    on_student_success=None,
    update_status=None,
) -> None:
    """
    Render the login form inside *parent*.

    Parameters:
        parent            : Container frame to render into.
        data              : Student data dictionary used for student auth.
        on_teacher_success: Callback called on successful teacher login.
        on_student_success: Callback(username) called on successful student login.
        update_status     : Callback(message) to update the status bar.
    """
    clear_frame(parent)
    parent.configure(bg=BG_CARD)

    # ── Header ──────────────────────────────────────────────────
    header = tk.Frame(parent, bg=ACCENT, height=4)
    header.pack(fill="x")

    icon_label = tk.Label(
        parent,
        text="🎓",
        font=("Segoe UI", 28),
        bg=BG_CARD,
        fg=TEXT_PRIMARY,
    )
    icon_label.pack(pady=(18, 2))

    title_label = tk.Label(
        parent,
        text="School Report System",
        font=("Segoe UI", 15, "bold"),
        bg=BG_CARD,
        fg=TEXT_PRIMARY,
    )
    title_label.pack()

    subtitle = tk.Label(
        parent,
        text="Sign in to continue",
        font=("Segoe UI", 9),
        bg=BG_CARD,
        fg=TEXT_MUTED,
    )
    subtitle.pack(pady=(2, 14))

    divider = tk.Frame(parent, bg=BORDER_COLOR, height=1)
    divider.pack(fill="x", padx=20, pady=(0, 14))

    # ── Form fields ─────────────────────────────────────────────
    form_frame = tk.Frame(parent, bg=BG_CARD)
    form_frame.pack(padx=30, fill="x")

    _make_label(form_frame, "Username").pack(anchor="w", pady=(0, 3))
    username_entry = _make_styled_entry(form_frame)
    username_entry.pack(fill="x", ipady=7, pady=(0, 12))

    _make_label(form_frame, "Password").pack(anchor="w", pady=(0, 3))
    password_entry = _make_styled_entry(form_frame, show="•")
    password_entry.pack(fill="x", ipady=7, pady=(0, 14))

    # ── Role selector ────────────────────────────────────────────
    role_var = tk.StringVar(value="Teacher")

    role_frame = tk.Frame(form_frame, bg=BG_CARD)
    role_frame.pack(fill="x", pady=(0, 16))

    role_title = _make_label(role_frame, "Login as:", small=True)
    role_title.configure(bg=BG_CARD)
    role_title.pack(anchor="w", pady=(0, 5))

    btn_row = tk.Frame(role_frame, bg=BG_CARD)
    btn_row.pack(fill="x")

    def make_role_btn(text: str, value: str) -> tk.Radiobutton:
        rb = tk.Radiobutton(
            btn_row,
            text=text,
            variable=role_var,
            value=value,
            font=("Segoe UI", 10),
            bg=BG_CARD,
            fg=TEXT_PRIMARY,
            selectcolor=BG_INPUT,
            activebackground=BG_CARD,
            activeforeground=ACCENT,
            cursor="hand2",
            bd=0,
            highlightthickness=0,
        )
        return rb

    make_role_btn("👨‍🏫  Teacher", "Teacher").pack(side="left", padx=(0, 20))
    make_role_btn("🧑‍🎓  Student", "Student").pack(side="left")

    # ── Error label (hidden by default) ─────────────────────────
    error_var = tk.StringVar(value="")
    error_label = tk.Label(
        form_frame,
        textvariable=error_var,
        font=("Segoe UI", 9),
        bg=BG_CARD,
        fg=ERROR_COLOR,
        anchor="w",
    )
    error_label.pack(fill="x", pady=(0, 6))

    # ── Login button ─────────────────────────────────────────────
    def _on_enter(e):
        login_btn.configure(bg=ACCENT_HOVER)

    def _on_leave(e):
        login_btn.configure(bg=ACCENT)

    login_btn = tk.Button(
        form_frame,
        text="Sign In",
        font=("Segoe UI", 11, "bold"),
        bg=ACCENT,
        fg="white",
        activebackground=ACCENT_HOVER,
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=10,
        pady=10,
        command=lambda: handle_login(),
    )
    login_btn.pack(fill="x", pady=(4, 0))
    login_btn.bind("<Enter>", _on_enter)
    login_btn.bind("<Leave>", _on_leave)

    # ── Helper functions ─────────────────────────────────────────
    def clear_entries() -> None:
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        username_entry.focus()

    def show_error(msg: str) -> None:
        error_var.set(f"⚠  {msg}")
        if update_status:
            update_status(msg)

    def handle_login() -> None:
        error_var.set("")
        username = username_entry.get().strip()
        password = password_entry.get()          # no strip — passwords may have spaces
        role = role_var.get()

        if not username or not password:
            show_error("Please fill in all fields.")
            clear_entries()
            return

        if role == "Teacher":
            if teacher_login(username, password):
                if update_status:
                    update_status("✓ Teacher login successful")
                if on_teacher_success:
                    on_teacher_success()
                return

        if role == "Student":
            if student_login(data, username, password):
                if update_status:
                    update_status("✓ Student login successful")
                if on_student_success:
                    on_student_success(username)
                return

        show_error("Invalid username or password.")
        clear_entries()

    # Bind Enter key to submit
    parent.bind_all("<Return>", lambda e: handle_login())
    username_entry.focus()


# ─── Standalone test window ────────────────────────────────────────

def run_test_window() -> None:
    """Launch a self-contained test window for login_ui."""
    root = tk.Tk()
    root.title("Login — School Report System")
    root.geometry("400x520")
    root.configure(bg=BG_MAIN)
    root.resizable(False, False)

    # Center on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - 200
    y = (root.winfo_screenheight() // 2) - 260
    root.geometry(f"400x520+{x}+{y}")

    test_data = {
        "ali": {
            "password": "1111",
            "grades": {"math": 18},
        }
    }

    # Card wrapper
    card = tk.Frame(root, bg=BG_CARD, bd=0, highlightthickness=1,
                    highlightbackground=BORDER_COLOR)
    card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=480)

    # Status bar
    status_var = tk.StringVar(value="Ready")
    status_bar = tk.Label(
        root,
        textvariable=status_var,
        font=("Segoe UI", 9),
        bg="#131c27",
        fg=TEXT_MUTED,
        anchor="w",
        padx=10,
        pady=4,
    )
    status_bar.pack(side="bottom", fill="x")

    def update_status(msg: str) -> None:
        color = SUCCESS_COLOR if "successful" in msg else (ERROR_COLOR if "fail" in msg.lower() else TEXT_MUTED)
        status_bar.configure(fg=color)
        status_var.set(msg)

    def show_success_page(title: str) -> None:
        clear_frame(card)
        card.configure(bg=BG_CARD)
        tk.Frame(card, bg=ACCENT, height=4).pack(fill="x")
        tk.Label(card, text="✅", font=("Segoe UI", 36), bg=BG_CARD).pack(pady=(30, 6))
        tk.Label(card, text=title, font=("Segoe UI", 13, "bold"),
                 bg=BG_CARD, fg=TEXT_PRIMARY).pack()
        tk.Label(card, text="You are now logged in.", font=("Segoe UI", 9),
                 bg=BG_CARD, fg=TEXT_MUTED).pack(pady=(4, 24))

        back_btn = tk.Button(
            card, text="← Back to Login",
            font=("Segoe UI", 10),
            bg=BG_INPUT, fg=TEXT_PRIMARY,
            activebackground=BORDER_COLOR, activeforeground=TEXT_PRIMARY,
            relief="flat", bd=0, cursor="hand2", pady=8,
            command=lambda: show_login_screen(
                card, test_data,
                on_teacher_success=lambda: show_success_page("Welcome, Teacher!"),
                on_student_success=lambda u: show_success_page(f"Welcome, {u}!"),
                update_status=update_status,
            ),
        )
        back_btn.pack(padx=30, fill="x")

    show_login_screen(
        parent=card,
        data=test_data,
        on_teacher_success=lambda: show_success_page("Welcome, Teacher!"),
        on_student_success=lambda u: show_success_page(f"Welcome, {u}!"),
        update_status=update_status,
    )

    root.mainloop()


if __name__ == "__main__":
    run_test_window()
