import Model.Data.Pathways as Pathways
from Model.FileReadingWriting.DataFormatter import DataFormatter


class SetCSVPath:

    @staticmethod
    def set_csv_files(pathways: list[str]) -> None:
        for pathway in pathways:
            unit_name = DataFormatter.get_care_unit_name(pathway)
            Pathways.DICTIONARY_PATHWAYS[unit_name] = pathway
