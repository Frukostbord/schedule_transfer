import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from typing import Union

import View.ErrorMessages as ErrorMessages


class FileTransferView:

    """
    Main view of the application.
    The user can:
    1. Add .csv files to a list box
    2. Remove .csv files from the listbox
    3. Add a directory where files should be saved
    4. Transfer data from the .csv file(s) to the Excel file(s)
    """
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
        """
        Adds .csv files to the listbox by allowing the user to select
        """

        files = list(filedialog.askopenfilenames(title="Välj filer som ska föras över ifrån"))

        # If any files have been selected
        if files:
            # Sorted .csv files in a dictionary:
            # "Faulty_csv_files" can´t be added
            # "Correct_csv_files" are files that have been added to the model
            sorted_files = self.controller.check_and_add_csv_files(files)

            # If there are any faulty .csv files, display an error message of them
            if sorted_files["Faulty_csv_files"]:
                FileTransferView.show_error_message(
                    f"Följande fil(-er) fungerade inte att öppna:\n{"\n".join(sorted_files["Faulty_csv_files"])}")

            # If any csv. files were correct, get the new data from the model and display them
            if sorted_files["Correct_csv_files"]:
                self.update_listbox()

    def remove_selected_file(self) -> None:
        """
        If one or several files are removed, remove the data from the model through the controller.
        Then update the listbox from the data in the model through the controller.
        """

        # Gets files selected by the user
        selected = self.listbox_file_pathways.curselection()

        # Removes selected files, if any are selected
        if selected:
            self.controller.remove_file(selected)
            self.update_listbox()

    def update_listbox(self) -> None:
        """
        Deletes all data in the listbox, then gets the new data from the model through the controller
        """

        self.listbox_file_pathways.delete(0, tk.END)
        current_csv_files = self.controller.get_csv_files()

        for file in current_csv_files:
            self.listbox_file_pathways.insert(tk.END, file)

    def save_path(self) -> None:
        """
        Checks to see if the save path selected by the user is correct.
        """

        # Open directory selection
        pathway = filedialog.askdirectory(title="Välj var filerna ska sparas")

        if pathway:
            if self.controller.check_and_set_save_pathway(pathway):
                self.update_save_path()

            else:
                self.show_message("Sökväg för att spara filer",
                                  "Något gick fel vid val av sökväg var filerna ska sparas.\n"
                                  "Du har inte tillgång eller så har sökvägen flyttats")

    def start_transfer(self) -> None:
        """
        Large method which starts the whole transfer process of the data from the .csv files to newly created
        Excel files.
        """

        # True if it went well, else has information on where it went wrong
        transfer_outcome = self.controller.start_transfer()

        # If everything went fine: Display a success message to the user,
        # open the directory, reset data and update the UI
        if transfer_outcome is True:
            self.successful_transfer()

        # If everything did not go well, show what and where it went wrong for the user
        else:
            self.transfer_unsuccessful(transfer_outcome)

    def display_check_data_fail(self):
        self.show_error_message("Grundmallen och/eller filerna med alla data har flyttats, är öppna eller ändrade.")

    def successful_transfer(self) -> None:
        """
        If the transfer of data from the .csv files to the Excel files are correct, call the following methods below
        """
        self.show_message("Klart!", "Överföringen gick utan problem!")
        self.open_save_directory()
        self.controller.reset_data()
        self.update_ui()

    def transfer_unsuccessful(self, transfer_problem: Union[tuple, dict]) -> None:
        if isinstance(transfer_problem, tuple):
            self.problem_transfer(transfer_problem)
        elif isinstance(transfer_problem, dict):
            self.problem_data_check(transfer_problem)

    def problem_data_check(self, data_checks: dict) -> None:
        """
        This method checks each data check and display each error that occurred
        :param data_checks: a dictionary with all data checks, where each False boolean value is a faulty check
        """
        # Go through all the data checks and display an error for each faulty check
        for data_check in data_checks:
            if not data_checks[data_check]:
                self.show_error_message(ErrorMessages.ERROR_MESSAGE_CHECK_DATA[data_check])

    def problem_transfer(self, transfer_problem: tuple) -> None:
        """
        Checks the data in the parameter and displays it accordingly to the user.
        :param transfer_problem: The data of the encountered problem during transferring of data.
        """

        error_message = ""
        problem_encountered = transfer_problem[0]
        file_path = transfer_problem[1]

        error_message += ErrorMessages.ERROR_MESSAGES_TRANSFERSTAGE[problem_encountered]
        error_message += f"\nVänligen se över följande fil: {file_path}"

        self.show_error_message(error_message)

    def update_ui(self) -> None:
        """
        Updates the UI information for the user:
        - Save path
        - CSV files in listbox
        """
        self.label_save_path.config(text="Välj var filerna ska sparas")
        self.update_listbox()

    def open_save_directory(self) -> None:
        """
        Gets the save path from the Controller -> Model, then opens the file directory.
        """
        save_path: str = self.controller.get_save_path()

        if self.controller.check_path(save_path):
            os.startfile(save_path)

    def update_save_path(self) -> None:
        """
        Gets Save path from Controller -> Model,
        then saves it in the label next to the "Sparas" button.
        """
        save_path = self.controller.get_save_path()
        self.label_save_path.config(text=save_path)

    @staticmethod
    def show_error_message(message: str) -> None:
        """
        Shows error message to user
        :param message: Error message
        """
        messagebox.showerror("Error", message)

    @staticmethod
    def show_message(title: str, message: str) -> None:
        """
        Shows a message to the user
        :param title: Title of messagebox
        :param message: Message to user
        """
        messagebox.showinfo(title, message)

    def quit_app(self) -> None:
        """
        Quits the application
        """
        self.master.quit()
