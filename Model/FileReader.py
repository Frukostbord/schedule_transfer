from os import path
class FileReader:
    """Class for controlling that the files read are correct"""
    @staticmethod
    def check_files(path_csv: str, path_excel_out: str):
        return FileReader.check_path_csv_excel(path_csv) and FileReader.check_path_excel_out(path_excel_out)

    @staticmethod
    def check_path_csv_excel(path_csv_excel: str) -> bool:
        """ Checks if the file for the incoming data file is correct Otherwise, it returns False """
        # Checking if the filepath exists and is correct
        if path.exists(path_csv_excel):
            if path.isfile(path_csv_excel) and path_csv_excel.endswith(".csv"):
                return True

        return False

    @staticmethod
    def check_path_excel_out(path_excel_out) -> bool:
        """ Checks if the file for the outgoing data file is correct. Otherwise, it returns False """
        # Checking if the filepath exists and is correct
        if path.exists(path_excel_out):
            if path.isfile(path_excel_out) and path_excel_out.endswith(".xlsx"):
                return True

        return False
