import pandas as pd
from DataFormatter import DataFormatter
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.workbook.workbook import Workbook

class FileProcessing:
    @staticmethod
    def reformat_data_csv(path: str) -> list:
        cleaned_data = []

        """ Method for getting data from a CSV file with work times of employees"""
        # Open file columns with Pandas, with no Header.
        df = pd.read_csv(path, header=None)

        for _ in df.columns:
            # Convert everything to lists
            cleaned_columns = df[_].str.split().tolist()

            # Iterate through all the lists and add each to the dictionary
            for column in range(2, len(cleaned_columns)):
                col = cleaned_columns[column]  # To shorten the name of the variable

                # Remove seperator with semicolons ";" in the csv files between weeks (columns)
                if len(set(col[0])) == 1:
                    continue

                # Check to see if there´s useless information for the transfer
                elif col[0] == "Ö;" or col[0] == "Förnamn;":
                    continue

                # Adds information to the list
                else:
                    formatted_data = FileProcessing.format_data(col)
                    cleaned_data.append(formatted_data)

        return cleaned_data  # Returns the cleaned data


    @staticmethod
    def format_data(data: list[str]) -> list[str]:
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

