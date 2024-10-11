from Model.CheckInitialData import CheckInitialData
from Model.CheckAndSetPaths import CheckAndSetCSV, CheckAndSetSavePath
import Model.Pathways as Pathways


class ModelMain:

    def __init__(self):
        self.template_pathway = None
        self.application_pathway = None

    def initialize_data(self) -> bool:
        """
        Checks and sets the data when the application starts.
        Returns False if some of the file(s) in the start are missing
        """
        return CheckInitialData.check_initial_data()

    def check_and_set_save_pathway(self, save_pathway: str) -> bool:
        """
        Gets the save_pathway saved from the Controller. Checks it if it´s valid and then sets it.
        """
        return CheckAndSetSavePath.check_and_set_save_path(save_pathway)

    def check_data(self) -> bool:
        check = self.check_all_pathways()
        return check

    def check_and_set_csv_files(self, file_pathways: list) -> dict[str:list]:
        pathways_sorted = CheckAndSetCSV.check_and_set_csv_files(file_pathways)
        return pathways_sorted

    def check_all_pathways(self) -> bool:
        pathways_exist = (
                Pathways.APPLICATION_PATHWAY and Pathways.DICTIONARY_PATHWAYS and Pathways.TEMPLATE_WORKBOOK_PATHWAY)
        return pathways_exist

    def transfer_data_csv_to_excel(self) -> None:
        pass







