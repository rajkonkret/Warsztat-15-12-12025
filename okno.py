"""
Prosty interfejs GUI w tkinter.
Funkcje:
- formularz (Imię, Wiek) z przyciskiem "Dodaj" dodającym wiersz do tabeli
- tabela (ttk.Treeview) z listą wpisów
- przyciski: Usuń zaznaczone, Wyczyść wszystko
- menu: Plik -> Zapisz jako CSV, Zakończ; Pomoc -> O programie
- pasek stanu

Uruchomienie: python okno.py
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
from pathlib import Path


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Prosty program - Tkinter")
        self.root.geometry("720x420")

        self._create_menu()
        self._create_widgets()
        self._create_statusbar()

        # przykładowe dane
        self._populate_sample()

    def _create_menu(self):
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Zapisz jako...", command=self.save_csv)
        filemenu.add_separator()
        filemenu.add_command(label="Zakończ", command=self.root.quit)
        menubar.add_cascade(label="Plik", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="O programie", command=self._about)
        menubar.add_cascade(label="Pomoc", menu=helpmenu)

        self.root.config(menu=menubar)

    def _create_widgets(self):
        main = ttk.Frame(self.root, padding=(10, 10))
        main.pack(fill=tk.BOTH, expand=True)

        left = ttk.Frame(main)
        left.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Label(left, text="Imię:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.name_var = tk.StringVar()
        ttk.Entry(left, textvariable=self.name_var, width=25).grid(row=0, column=1, pady=2)

        ttk.Label(left, text="Wiek:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.age_var = tk.StringVar()
        ttk.Entry(left, textvariable=self.age_var, width=25).grid(row=1, column=1, pady=2)

        btn_add = ttk.Button(left, text="Dodaj", command=self.add_record)
        btn_add.grid(row=2, column=0, columnspan=2, pady=(8, 2), sticky=tk.EW)

        btn_remove = ttk.Button(left, text="Usuń zaznaczone", command=self.remove_selected)
        btn_remove.grid(row=3, column=0, columnspan=2, pady=2, sticky=tk.EW)

        btn_clear = ttk.Button(left, text="Wyczyść wszystko", command=self.clear_all)
        btn_clear.grid(row=4, column=0, columnspan=2, pady=2, sticky=tk.EW)

        left.columnconfigure(1, weight=1)

        right = ttk.Frame(main)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        cols = ("name", "age")
        self.tree = ttk.Treeview(right, columns=cols, show="headings", selectmode="extended")
        self.tree.heading("name", text="Imię")
        self.tree.heading("age", text="Wiek")
        self.tree.column("name", width=200)
        self.tree.column("age", width=80, anchor=tk.CENTER)

        vsb = ttk.Scrollbar(right, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=vsb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.LEFT, fill=tk.Y)

    def _create_statusbar(self):
        self.status = tk.StringVar(value="Gotowy")
        status_bar = ttk.Label(self.root, textvariable=self.status, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def _about(self):
        messagebox.showinfo("O programie", "Przykładowe okno tkinter\nAutor: wygenerowane")

    def _populate_sample(self):
        sample = [("Ala", 29), ("Bartek", 34)]
        for name, age in sample:
            self.tree.insert("", "end", values=(name, age))
        self._update_status()

    def add_record(self):
        name = self.name_var.get().strip()
        age = self.age_var.get().strip()
        if not name:
            messagebox.showwarning("Brak imienia", "Proszę podać imię.")
            return
        if age:
            try:
                age_i = int(age)
                if age_i < 0:
                    raise ValueError()
            except Exception:
                messagebox.showwarning("Nieprawidłowy wiek", "Wiek powinien być nieujemną liczbą całkowitą.")
                return
        else:
            age_i = ""

        self.tree.insert("", "end", values=(name, age_i))
        self.name_var.set("")
        self.age_var.set("")
        self._update_status()

    def remove_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Brak zaznaczenia", "Nie wybrano żadnego wiersza do usunięcia.")
            return
        for item in sel:
            self.tree.delete(item)
        self._update_status()

    def clear_all(self):
        if messagebox.askyesno("Potwierdź", "Czy na pewno usunąć wszystkie wiersze?"):
            for item in self.tree.get_children():
                self.tree.delete(item)
            self._update_status()

    def save_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV","*.csv"), ("All files","*.*")])
        if not path:
            return
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(("Imię", "Wiek"))
                for item in self.tree.get_children():
                    writer.writerow(self.tree.item(item, "values"))
            self.status.set(f"Zapisano: {Path(path).name}")
        except Exception as e:
            messagebox.showerror("Błąd zapisu", f"Nie można zapisać pliku: {e}")

    def _update_status(self):
        rows = len(self.tree.get_children())
        self.status.set(f"Wiersze: {rows}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

