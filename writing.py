import tkinter as tk

WHITE = "#F0F3FF"

class WritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text App")
        self.root.config(padx=100, pady=50, bg=WHITE)

        self.text = tk.Text(self.root, height=10, width=50)
        self.text.pack()

        self.timer = None
        self.start_timer()

        self.text.bind("<Key>", self.on_key_pressed)

    def on_key_pressed(self, event):
        if self.timer is not None:
            self.root.after_cancel(self.timer)
        self.start_timer()

    def start_timer(self):
        self.timer = self.root.after(5000, self.clear_text)  # Set the timer to 5 seconds (5000 milliseconds)

    def clear_text(self):
        self.text.delete(1.0, tk.END)
