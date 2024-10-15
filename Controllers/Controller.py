from Controllers.PopupMessage import PopupMessage
import Model.Data.ErrorMessages as ErrorMessages
from typing import Union
from Model.Enum.TransferStages import TransferStage
from Model.Data.ErrorMessages import ERROR_MESSAGES_TRANSFERSTAGE
from Model.Data.ResetData import ResetData


class FileTransferController:
    def __init__(self, model):
        self.model = model
        self.initialize_data()

    def initialize_data(self) -> None:
        """
        Sets the initial data of the program
        """
        if not self.model.initialize_data():
            PopupMessage.error_message(
                "Grundmallen kunde inte hittas. Vänligen se till att den finns innan du kör programmet")

    def check_and_add_csv_files(self, files_pathways: list[str]) -> list[str]:

        files_pathways_dict = self.model.check_and_set_csv_files(files_pathways)

        if files_pathways_dict["Faulty_csv_files"]:
            PopupMessage.error_message(
                f"Följande fil(-er) fungerade inte att öppna:\n{"\n".join(files_pathways_dict["Faulty_csv_files"])}")

        return files_pathways_dict["Correct_csv_files"]

    def check_and_set_save_pathway(self, save_pathway: str) -> bool:
        """
        Check to see if the save_path is correct input is correct
        """
        if self.model.check_and_set_save_pathway(save_pathway):
            return True

        else:
            PopupMessage.error_message("Katalog för filerna kunde inte väljas. Vänligen välja en annan.")
            return False

    def start_transfer(self) -> bool:
        # Checks to see if all user input is correct before proceeding
        if self.check_all_data():
            transfer_success = self.model.transfer_data_csv_to_excel()
            self.display_transfer_success(transfer_success)

            if transfer_success:
                FileTransferController.reset_gui_and_data()
                return True

        return False

    def get_save_path(self) -> str:
        return self.model.get_save_path()

    @staticmethod
    def reset_gui_and_data():
        ResetData.reset_data()

    def display_transfer_success(self, transfer_event_success: Union[bool, tuple[TransferStage, str]]):
        if transfer_event_success is True:
            PopupMessage.pop_up_message("Klart!", "Överföringen gick utan problem!")

        else:
            PopupMessage.error_message(f"{ERROR_MESSAGES_TRANSFERSTAGE[transfer_event_success[0]]}\n"
                                       f"Se över följande fil: {transfer_event_success[1]}")


    def remove_file(self, indexes_to_delete: tuple[int]) -> None:
        self.model.remove_csv_files(indexes_to_delete)

    def check_all_data(self) -> bool:
        """ Checks to see if all user input is correct """

        checked_paths: dict = self.model.check_all_pathways()

        for pathway in checked_paths:
            if not checked_paths[pathway]:
                PopupMessage.error_message(ErrorMessages.ERROR_MESSAGES_TRANSLATED[pathway])
                return False

        return True

    def get_files(self) -> list[str]:
        return self.model.get_current_csv_files()
