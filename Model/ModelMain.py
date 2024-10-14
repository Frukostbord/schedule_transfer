# Local applications
from Model.InitializeData.InitializeData import InitializeData
from Model.CheckPaths.CheckCSVPath import CheckCSVPath
from Model.CheckPaths.CheckSavePath import CheckSavePath
from Model.SetPaths.SetSavePath import SetSavePath
from Model.SetPaths.SetCSVPath import SetCSVPath
from Model.CheckPaths.CheckFile import CheckFiles
from Model.FileReadingWriting.FileTransfer import FileTransfer
from Model.RemoveFiles.RemoveCSVFiles import RemoveCSVFiles
import Model.Data.Pathways as Pathways


class ModelMain:

    def __init__(self):
        self.template_pathway = None
        self.application_pathway = None
        self.file_transfer = None

    def initialize_data(self) -> bool:
        """
        Checks and sets the data when the application starts.
        Returns False if some of the file(s) in the start are missing
        """
        return InitializeData.initialize_data()

    def check_and_set_save_pathway(self, save_pathway: str) -> bool:
        """
        Gets the save_pathway saved from the Controller. Checks it if it´s valid and then sets it.
        """
        if CheckSavePath.check_save_path(save_pathway):
            SetSavePath.set_save_path(save_pathway)
            return True

        return False


    def check_and_set_csv_files(self, file_pathways: list) -> dict[str:list[str]]:
        """
        :param file_pathways: Dictionary of correct and faulty csv_files
        keys:
        "Correct_csv_files"
        "Faulty_csv_files"
        :return: returns faulty csv_files to be sent as error
        """

        pathways_sorted = CheckCSVPath.check_csv_files(file_pathways)
        SetCSVPath.set_csv_files(pathways_sorted["Correct_csv_files"])

        return pathways_sorted

    def check_all_pathways(self) -> dict[str:bool]:
        check_pathways: dict = {
            "Application_pathway": bool(Pathways.APPLICATION_PATHWAY),
            "CSV_files": CheckFiles.check_pathways(Pathways.DICTIONARY_PATHWAYS.values()),
            "Save_path": CheckFiles.check_pathway(Pathways.SAVE_PATH),
            "Template_path": CheckFiles.check_pathway(Pathways.TEMPLATE_WORKBOOK_PATHWAY)
        }

        return check_pathways

    def transfer_data_csv_to_excel(self) -> None:
        for pathway in Pathways.DICTIONARY_PATHWAYS:
            self.file_transfer = FileTransfer(Pathways.DICTIONARY_PATHWAYS[pathway])
            self.file_transfer.start_transfer()

    def remove_csv_files(self, index_files_to_remove: tuple[int]) -> None:
        RemoveCSVFiles.remove_csv_files(index_files_to_remove)

    def get_current_csv_files(self) -> list[str]:
        return Pathways.DICTIONARY_PATHWAYS.values()
