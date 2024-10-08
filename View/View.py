import tkinter as tk
from tkinter import filedialog

class FileTransferView:
    def __init__(self, master, viewmodel):
        self.master = master
        self.viewmodel = viewmodel
        self.master.title("Filöverföring - Ifrån Timecare till Excel")

        # Listbox to display selected files
        self.listbox_file_pathways = tk.Listbox(master, width=100, height=10)
        self.listbox_file_pathways.grid(row=0, column=0, padx=10, pady=10)

        # Buttons
        self.add_button1 = tk.Button(master, text="Lägg till fil(-er)", command=self.add_files)
        self.add_button1.grid(row=0, column=1, padx=10, pady=(5, 90))  # Add button at the top right

        self.remove_button = tk.Button(master, text="Ta bort vald fil(-er)", command=self.remove_selected_file)
        self.remove_button.grid(row=0, column=1, padx=10, pady=5)  # Remove button below add button

        self.start_button = tk.Button(master, text="Börja överföring", command=self.start_transfer)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)  # Start button at the bottom left

        self.quit_button = tk.Button(master, text="Avsluta", command=self.quit_app)
        self.quit_button.grid(row=1, column=1, padx=10, pady=10)  # Quit button at the bottom right

    def add_files(self):
        files = filedialog.askopenfilenames(title="Välj filer som ska föras över ifrån")
        if files:
            self.viewmodel.add_files(files)
            self.update_listbox()

    def remove_selected_file(self):
        selected = self.listbox_file_pathways.curselection()  # Get the index of the selected file
        if selected:
            index = selected[0]
            self.viewmodel.remove_file(index)
            self.update_listbox()

    def update_listbox(self):
        self.listbox_file_pathways.delete(0, tk.END)  # Clear the listbox
        for file in self.viewmodel.get_files():  # Update listbox with current files
            self.listbox_file_pathways.insert(tk.END, file)

    def start_transfer(self):
        files = self.viewmodel.get_files()
        print("Påbörjar filöverföring", files)

    def quit_app(self):
        self.master.quit()
