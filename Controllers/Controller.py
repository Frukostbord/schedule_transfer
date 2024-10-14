from Controllers.Error import Error
import Model.Data.ErrorMessages as ErrorMessages


class FileTransferController:
    def __init__(self, model):
        self.model = model
        self.initialize_data()

    def initialize_data(self) -> None:
        """
        Sets the initial data of the program
        """
        if not self.model.initialize_data():
            Error.error_message(
                "Grundmallen kunde inte hittas. Vänligen se till att den finns innan du kör programmet")

    def check_and_add_csv_files(self, files_pathways: list[str]) -> list[str]:

        files_pathways_dict = self.model.check_and_set_csv_files(files_pathways)

        if files_pathways_dict["Faulty_csv_files"]:
            Error.error_message(
                f"Följande fil(-er) fungerade inte att öppna:\n{"\n".join(files_pathways_dict["Faulty_csv_files"])}")

        return files_pathways_dict["Correct_csv_files"]

    def check_and_set_save_pathway(self, save_pathway: str) -> bool:
        """
        Check to see if the save_path is correct input is correct
        """
        if self.model.check_and_set_save_pathway(save_pathway):
            return True

        else:
            Error.error_message("Katalog för filerna kunde inte väljas. Vänligen välja en annan.")
            return False

    def start_transfer(self) -> None:
        # Checks to see if all user input is correct before proceeding
        if self.check_all_data():
            self.model.transfer_data_csv_to_excel()

    def remove_file(self, indexes_to_delete: tuple[int]) -> None:
        self.model.remove_csv_files(indexes_to_delete)

    def check_all_data(self) -> bool:
        """ Checks to see if all user input is correct """

        checked_paths: dict = self.model.check_all_pathways()

        for pathway in checked_paths:
            if not checked_paths[pathway]:
                Error.error_message(ErrorMessages.ERROR_MESSAGES_TRANSLATED[pathway])
                return False

        return True

    def get_files(self) -> list[str]:
        return self.model.get_current_csv_files()
