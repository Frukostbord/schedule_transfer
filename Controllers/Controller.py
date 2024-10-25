from typing import Union

from Model.Data.ResetData import ResetData
from Model.Enum.TransferStages import TransferStage


class FileTransferController:

    """
    Controller class.
    It´s main purpose is to:
    1. Execute methods called from the View.
    2. Call methods from the Model, which does all the calculations and checks.
    """
    def __init__(self, model):
        self.model = model

    def initialize_data(self) -> bool:
        """
        Sets the initial data of the program
        """
        return self.model.initialize_data()

    def check_and_add_csv_files(self, files_pathways: list[str]) -> dict[str:list[str]]:
        return self.model.check_and_set_csv_files(files_pathways)

    def check_and_set_save_pathway(self, save_pathway: str) -> bool:
        """
        Check to see if the save_path is correct input is correct
        """
        if self.model.check_and_set_save_pathway(save_pathway):
            return True
        return False

    def start_transfer(self) -> Union[bool, tuple[TransferStage, str]]:
        """
        Largest method which initiates the whole transfer process with data from the .csv file to the Excel file.
        :return: True if everything went fine
        """

        # Checks to see if all user input is correct before proceeding
        checked_data = self.check_all_data()

        if checked_data is True:
            # Starts transferring the data
            transfer_success = self.model.transfer_data_csv_to_excel()

            # Returns True if everything went fine
            if transfer_success == TransferStage.TRANSFER_COMPLETE:
                return True

            # If there was an error with a certain file
            else:
                return transfer_success

        else:
            # If the data wasn't up to snuff, return the
            return checked_data

    def get_save_path(self) -> str:
        return self.model.get_save_path()

    @staticmethod
    def reset_data():
        ResetData.reset_data()

    def remove_file(self, indexes_to_delete: tuple[int]) -> None:
        """
        Removes files from indexes in the tuple
        """
        self.model.remove_csv_files(indexes_to_delete)

    def check_all_data(self) -> Union[bool, dict[str:bool]]:
        """ Checks to see if all user input is correct """

        checked_paths: dict = self.model.check_all_pathways()

        # If all checks pass
        if all(checked_paths.values()):
            return True

        # If one or more checks fail
        return checked_paths

    def check_path(self, path: str) -> bool:
        return self.model.check_path(path)

    def get_csv_files(self) -> list[str]:
        return self.model.get_current_csv_files()
