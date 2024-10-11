from Model.CheckFiles import CheckFiles
from Model.DataFormatter import DataFormatter
import Model.Pathways as Pathways


class CheckAndSetSavePath:

    @classmethod
    def check_and_set_save_path(cls, file_path: str) -> bool:
        if cls.check_save_path(file_path):
            cls.set_save_path(file_path)
            return True

        return False

    @classmethod
    def check_save_path(cls, file_path: str) -> bool:
        return CheckFiles.check_file_path(file_path)

    @classmethod
    def set_save_path(cls, file_path: str) -> None:
        Pathways.SAVE_PATH = file_path


class CheckAndSetCSV:

    # Faulty and correct csv files
    file_pathways_sorted = {
        "Correct_csv_files": [],
        "Faulty_csv_files": []
    }

    @classmethod
    def check_and_set_csv_files(cls, file_pathways: list) -> dict[str:list]:
        cls.check_csv_files(file_pathways)
        cls.set_csv_files()
        return cls.file_pathways_sorted

    @classmethod
    def check_csv_files(cls, file_pathways: list) -> None:
        """ Checks to see if csv files have correct format and can exist """
        if file_pathways:
            for file_pathway in file_pathways:
                correct_csv = (CheckFiles.check_file_path(file_pathway) and
                               CheckFiles.check_single_file_type(file_pathway, ".csv"))

                if correct_csv and cls.check_if_csv_unique(file_pathway):
                    cls.file_pathways_sorted["Correct_csv_files"].append(file_pathway)
                elif not correct_csv:
                    cls.file_pathways_sorted["Faulty_csv_files"].append(file_pathway)

    @classmethod
    def check_if_csv_unique(cls, file_pathway: str) -> bool:
        # False == It´s already added, True == it´s unique
        return file_pathway not in Pathways.DICTIONARY_PATHWAYS.values()

    @classmethod
    def set_csv_files(cls) -> None:
        for pathway in cls.file_pathways_sorted["Correct_csv_files"]:
            unit_name = DataFormatter.get_care_unit_name(pathway)
            Pathways.DICTIONARY_PATHWAYS[unit_name] = pathway




