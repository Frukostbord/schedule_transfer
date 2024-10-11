from Controllers.Error import Error
import Model.Pathways as Pathways


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
                f"Följande fil(-er) fungerade inte att öppna {", ".join(files_pathways_dict["Faulty_csv_files"])}")

        return files_pathways_dict["Correct_csv_files"]

    def check_all_data(self, files, save_path: str) -> bool:
        """ Checks to see if all user input is correct """

        # Check to see if parameters have data
        if not files:
            Error.error_message("Du måste välja en eller flera filer ifrån TimeCare.")
        if not save_path:
            Error.error_message("Du måste välja var alla filer ska sparas.")

        # Check to see if data is correct
        file_types = self.check_csv_files(files)
        save_path = self.check_file_path(save_path)

        return file_types and save_path


    def check_and_set_save_pathway(self, save_pathway: str) -> bool:
        """
        Check to see if the save_path is correct input is correct
        """
        if self.model.check_and_set_save_pathway(save_pathway):
            return True

        else:
            Error.error_message("Katalog för filerna kunde inte väljas. Vänligen välja en annan.")
            return False

        return True


    def start_transfer(self, files, save_path) -> None:
        check = self.check_all_data(files, save_path)  # Checks to see if all user input is correct before proceeding

