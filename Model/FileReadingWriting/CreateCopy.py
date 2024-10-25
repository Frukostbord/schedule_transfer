import shutil

from Model.Data import Pathways
from Model.FileReadingWriting.DataFormatter import DataFormatter


class CreateCopy:
    """
    Creates a copy of a file
    """

    @staticmethod
    def create_excel_copy(care_unit_unformatted: str) -> str:
        # Getting the care unit name
        care_unit = DataFormatter.get_care_unit_name(care_unit_unformatted)

        # Setting save path
        save_path = r"{}".format(Pathways.SAVE_PATH+"/"+care_unit+".xlsx")

        # Creating a Excel copy
        shutil.copy(Pathways.TEMPLATE_WORKBOOK_PATHWAY, save_path)

        return save_path

