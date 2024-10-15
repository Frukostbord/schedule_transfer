import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import Controllers
from typing import List

class FileTransferView:
    def __init__(self, master: tk.Tk, controller):
        self.master = master
        self.controller = controller
        self.master.title("Filöverföring - Ifrån Timecare till Excel")

        # Listbox to display selected files
        self.listbox_file_pathways = tk.Listbox(master, selectmode=tk.EXTENDED, width=100, height=10)
        self.listbox_file_pathways.grid(row=0, column=0, padx=10, pady=10)

        # Buttons
        self.button_add_files = tk.Button(master, text="Lägg till fil(-er)", command=self.add_csv_files)
        self.button_add_files.grid(row=0, column=1, padx=10, pady=(5, 90))

        self.button_remove = tk.Button(master, text="Ta bort vald fil(-er)", command=self.remove_selected_file)
        self.button_remove.grid(row=0, column=1, padx=10, pady=5)

        self.button_start = tk.Button(master, text="Börja överföring", command=self.start_transfer)
        self.button_start.grid(row=2, column=0, padx=10, pady=10)

        self.button_quit = tk.Button(master, text="Avsluta", command=self.quit_app)
        self.button_quit.grid(row=2, column=1, padx=10, pady=10)

        self.button_save_path = tk.Button(master, text="Sparas", command=self.save_path)
        self.button_save_path.grid(row=1, column=0, padx=(10, 550), pady=(10, 27))

        # Adding labels
        self.label_save_path = (
            tk.Label(master, text="Välj var filerna ska sparas",
                     font=("Arial", 9), width=65, wraplength=550, height=2, anchor="nw"))
        self.label_save_path.grid(row=1, column=0)


    def add_csv_files(self) -> None:
        files = list(filedialog.askopenfilenames(title="Välj filer som ska föras över ifrån"))

        if files:
            # Filter only valid files
            valid_files = self.controller.check_and_add_csv_files(files)

            self.add_files_to_listbox(valid_files)  # Adds files to listbox

    def add_files_to_listbox(self, files_to_add: List[str]) -> None:
        for file in files_to_add:
            self.listbox_file_pathways.insert(tk.END, file)

    def remove_selected_file(self):
        selected = self.listbox_file_pathways.curselection()
        if selected:
            selected_reversed = list(reversed(selected))
            self.controller.remove_file(selected_reversed)
            self.update_listbox()

    def update_listbox(self):
        self.listbox_file_pathways.delete(0, tk.END)
        current_csv_files = self.controller.get_files()

        for file in current_csv_files:
            self.listbox_file_pathways.insert(tk.END, file)

    def save_path(self):
        pathway = filedialog.askdirectory(title="Välj var filerna ska sparas")
        if self.controller.check_and_set_save_pathway(pathway):
            self.label_save_path.config(text=pathway)

    def start_transfer(self):
        if self.controller.start_transfer():
            self.reset_ui()

    def reset_ui(self):
        self.update_save_path()
        self.update_listbox()

    def update_save_path(self):
        save_path = self.controller.get_save_path()
        self.label_save_path.config(text=save_path)

    @staticmethod
    def show_error_message(message:str) -> None:
        messagebox.showerror("Error", message)

    @staticmethod
    def show_message(title: str, message: str) -> None:
        messagebox.showinfo(title, message)

    def quit_app(self):
        self.master.quit()
