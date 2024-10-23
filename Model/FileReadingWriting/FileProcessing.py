import pandas as pd
from Model.FileReadingWriting.DataFormatter import DataFormatter
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.workbook.workbook import Workbook

class FileProcessing:
    """
    This class is responsible for removing most of the unnecessary data in the .csv file, before it can be refined
    and used to write in the Excel class
    """
    @staticmethod
    def reformat_data_csv(path: str) -> list:
        cleaned_data = []

        # Open file columns with Pandas, with no Header.
        df = pd.read_csv(path, header=None)

        for _ in df.columns:
            # Convert everything to lists
            columns = df[_].str.split().tolist()

            # Iterate through all the lists, format the data and add it to the list
            for column in range(2, len(columns)):
                # To shorten the name of the variable
                processed_data = FileProcessing.clean_csv_data(columns[column])

                if processed_data:
                    cleaned_data.append(processed_data)

        return cleaned_data  # Returns the cleaned data

    @staticmethod
    def clean_csv_data(raw_data: list[str]) -> list[str]:
        if raw_data:
            # Check for specific useless information in the first row
            if raw_data[0] in {"Ö;", "Förnamn;"} or len(set(raw_data[0])) == 1:
                return []

            # Adds information to the list if all checks pass
            else:
                formatted_data = FileProcessing.format_csv_data(raw_data)
                return formatted_data


    @staticmethod
    def format_csv_data(data: list[str]) -> list[str]:
        #  1. Check what to format
        #  2. Call correct data formatter
        #  3. Return formatted data

        if data[0] == "Vecka":
            return DataFormatter.format_date(data)
        else:
            return DataFormatter.format_employee_work_time(data)



    @staticmethod
    def remove_work_sheet(worksheet: Worksheet, workbook: Workbook):
        workbook.remove(worksheet)

