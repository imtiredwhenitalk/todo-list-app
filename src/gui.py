import tkinter as tk
from tkinter import simpledialog, messagebox

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Лист задач")

        self.tasks = []  

        self.listbox = tk.Listbox(self.root, width=40, height=10)
        self.listbox.pack(padx=10, pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        self.add_btn = tk.Button(btn_frame, text="Додати задачу", command=self.add_task)
        self.add_btn.pack(side=tk.LEFT, padx=5)

        self.view_btn = tk.Button(btn_frame, text="Переглянути опис", command=self.view_description)
        self.view_btn.pack(side=tk.LEFT, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Видалити задачу", command=self.delete_task)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        title = simpledialog.askstring("Назва задачі", "Введіть назву задачі:")
        if title:
            description = simpledialog.askstring("Опис задачі", "Введіть опис задачі:")
            self.tasks.append({'title': title, 'description': description or ""})
            self.listbox.insert(tk.END, title)

    def view_description(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Необхідно вибрати", "Будь ласка, виберіть задачу.")
            return
        idx = selected[0]
        desc = self.tasks[idx]['description']
        messagebox.showinfo("Опис задачі", desc if desc else "Немає опису.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        idx = selected[0]
        self.listbox.delete(idx)
        del self.tasks[idx]

    def run(self):
        self.root.mainloop()