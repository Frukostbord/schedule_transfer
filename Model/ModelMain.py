import Pathways


class ModelMain:

    def __init__(self):
        pass

    def set_program_pathway(self, pathway: str) -> None:
        Pathways.APPLICATION_PATHWAY = pathway

    def set_template_pathway(self, pathway: str) -> None:
        Pathways.TEMPLATE_WORKBOOK_PATHWAY = pathway

    def set_save_pathway(self, pathway: str) -> None:
        Pathways.SAVE_PATH = pathway

    def check_data(self) -> bool:
        check = self.check_pathways()

        return check

    def check_pathways(self) -> bool:
        pathways_exist = (
                Pathways.APPLICATION_PATHWAY and Pathways.DICTIONARY_PATHWAYS and Pathways.TEMPLATE_WORKBOOK_PATHWAY)
        return pathways_exist

    def transfer_data_csv_to_excel(self) -> None:
        pass