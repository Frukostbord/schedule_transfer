import shutil
from Model.FileReadingWriting.DataFormatter import DataFormatter
from Model.Data import Pathways


class CreateCopy:

    @staticmethod
    def create_copy(care_unit_unformatted: str) -> str:
        care_unit = DataFormatter.get_care_unit_name(care_unit_unformatted)
        save_path = r"{}".format(Pathways.SAVE_PATH+"/"+care_unit+".xlsx")

        shutil.copy(Pathways.TEMPLATE_WORKBOOK_PATHWAY, save_path)

        return save_path

