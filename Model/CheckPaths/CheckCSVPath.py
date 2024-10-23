from Model.CheckPaths.CheckFile import CheckFiles
from Model.FileReadingWriting.DataFormatter import DataFormatter
import Model.Data.Pathways as Pathways


class CheckCSVPath:
    """
    Responsible for checks related to .csv files.
    """

    @classmethod
    def check_csv_files(cls, file_pathways: list) -> dict[str:list[str]]:
        """
        Checks to see if csv files have correct format and can exist
        """

        # Faulty and correct csv files
        file_pathways_sorted = {
            "Correct_csv_files": [],
            "Faulty_csv_files": []
        }

        # If there are any files
        if file_pathways:
            # Check file for file, if they are correct and unique. Then sort them in the dictionary
            for file_pathway in file_pathways:
                correct_csv = (CheckFiles.check_pathway(file_pathway, ".csv"))

                if correct_csv and cls.check_if_csv_unique(file_pathway):
                    file_pathways_sorted["Correct_csv_files"].append(file_pathway)
                elif not correct_csv:
                    file_pathways_sorted["Faulty_csv_files"].append(file_pathway)

        return file_pathways_sorted

    @classmethod
    def check_if_csv_unique(cls, file_pathway: str) -> bool:
        """
        Check´s to see if a .csv file is unique
        :param file_pathway: .csv pathway
        :return: True if unique, else false
        """
        return file_pathway not in Pathways.DICTIONARY_PATHWAYS.values()





