import os
from typing import Union, List, Dict
from SetInitialData import SetInitialData
import Model
import Error


class FileTransferController:
    def __init__(self, model: Model.ModelMain):
        self.model = model
        self.error = Error.Error

    def set_intial_data(self):
        if not SetInitialData.set_initial_data(self.model):  # Sets and checks all the initial data in the program
            self.error.error_message(
                "Grundmallen kunde inte hittas. Vänligen se till att den finns och start om programmet.")

    def add_csv_files(self, files: List[str], current_paths: List[str]) -> List[str]:
        valid_format_and_path = self.check_csv_files(files)
        unique_valid_csv_files = []

        # Update listbox with valid files
        for file in valid_format_and_path:
            if file not in current_paths:
                unique_valid_csv_files.append(file)

        return unique_valid_csv_files

    def check_all_data(self, files: Union[str, List[str]], save_path: str) -> bool:
        """ Checks to see if all user input is correct """

        # Check to see if parameters have data
        if not files:
            self.error.error_message("Du måste välja en eller flera filer ifrån TimeCare.")
        if not save_path:
            self.error.error_message("Du måste välja var alla filer ska sparas.")

        # Check to see if data is correct
        file_types = self.check_csv_files(files)
        save_path = self.check_file_path(save_path)

        return file_types and save_path

    def check_csv_files(self, files: Union[str, List[str]]) -> List[str]:
        """ Checks to see if csv files have correct format and can exist """
        if not files:
            return []

        #  Is a dict. 0 == valid files, 1 = not valid files
        csv_files = self.get_valid_csv_files(files)

        if csv_files["Faulty_csv_files"]:
            self.error.error_message(
             f"Följande fil(-er) fungerade inte att öppna {", ".join(csv_files["Faulty_csv_files"])}")

        return csv_files["Correct_csv_files"]

    def check_save_path(self, save_path: str) -> bool:
        """ Checks to see if all user input is correct """
        valid_save_path = self.check_file_path(save_path)

        if valid_save_path:
            self.save_path = save_path
            return True

        else:
            self.error.error_message("Ingen filväg var filerna ska sparas är vald")
            return False

    def get_valid_csv_files(self, files: Union[str, List[str]]) -> Dict[str, list]:
        # 0 == valid, 1 == invalid csv files
        csv_files = {
            "Correct_csv_files": [],
            "Faulty_csv_files": []
        }

        if isinstance(files, str):
            if self.check_file_is_csv(files) and self.check_file_path(files):
                csv_files["Correct_csv_files"].append(files)
            else:
                csv_files["Faulty_csv_files"].append(files)

        else:
            for file in files:
                valid_csv_file = self.check_file_is_csv(file) and self.check_file_path(file)

                if valid_csv_file:
                    csv_files["Correct_csv_files"].append(file)
                else:
                    csv_files["Faulty_csv_files"].append(file)

        return csv_files

    def check_file_is_csv(self, files: Union[str, List[str]]) -> bool:
        """ Checks to see if the file(s) are of .csv format """

        if isinstance(files, str):
            return self.check_single_file_type(files, ".csv")

        else:
            for p in files:
                if not self.check_single_file_type(p, ".csv"):
                    return False

            return True

    def check_file_paths(self, path: Union[str, List[str]]) -> bool:
        """ Checks to see if the file path exists with an input of a string or list of strings """
        if isinstance(path, str):
            return self.check_file_path(path)

        for p in path:
            if not self.check_file_path(p):
                return False

        return True

    def check_file_path(self, path: str) -> bool:
        return os.path.exists(path)

    def check_single_file_type(self, file_path: str, expected_extension: str) -> bool:
        """ Checks a single file's extension against the expected extension """
        _, file_extension = os.path.splitext(file_path)

        return file_extension.lower() == expected_extension.lower()

    def start_transfer(self, files, save_path) -> None:
        check = self.check_all_data(files, save_path)  # Checks to see if all user input is correct before proceeding

