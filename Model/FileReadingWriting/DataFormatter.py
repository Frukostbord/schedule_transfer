import os
from Model.Data.MinimumStaff import MINIMUM_STAFF
class DataFormatter:
    @staticmethod
    def format_date(data: list[str]) -> list[str]:
        """ Method for getting the date in the correct information """
        date_formatted = []

        week = DataFormatter.get_week(data[:2])
        date_formatted.append(week)

        for i in range(3, len(data), 2):
            clean_string = data[i].replace(";", "")  # Removes ";"
            date_formatted.append(clean_string)

        return date_formatted


    @staticmethod
    def remove_semicolon(string: str) -> str:
        new_string = string.replace(";", "")
        return new_string

    @staticmethod
    def format_employee_work_time(data: list) -> list:
        cleaned_data = []  # Data to be returned

        data.pop()  # Removes total hours worked, at the end of the list
        worker_name = (DataFormatter.get_worker_name(data[:2]))  # Get worker names
        cleaned_data = worker_name  # Add worker names

        worker_times = DataFormatter.get_worker_times(data[2:])
        cleaned_data += worker_times
        return cleaned_data

    @staticmethod
    def get_week(data: list) -> str:
        new_string = " ".join(data)

        new_string = new_string.replace(";", "")
        return new_string

    @staticmethod
    def get_worker_name(data: list[str]) -> list:
        first_name = DataFormatter.remove_semicolon(data[0])
        last_name = DataFormatter.remove_semicolon(data[1])

        name = [first_name, last_name]

        return name

    @staticmethod
    def get_worker_times(data: list) -> list:
        worker_times = []

        temp = []
        for i in range(len(data)):
            if ":" in data[i]:
                temp.append(data[i])
            elif data[i] == ";;;;":  # Means in the CSV file that the worker don´t work that day
                worker_times.append("")  # Add a empty string to say that they don´t work that day

            if len(temp) == 2:
                time = DataFormatter.format_worker_time(temp)
                worker_times.append(time)
                temp = []

        return worker_times

    @staticmethod
    def format_worker_time(data: list) -> str:
        time = "-".join(data)
        time = DataFormatter.remove_semicolon(time)
        return time

    @staticmethod
    def get_care_unit_name(unformatted_care_unit_name: str) -> str:
        care_unit_name = os.path.splitext(os.path.basename(unformatted_care_unit_name))[0]

        return care_unit_name

    @staticmethod
    def get_minimum_worker_formatted(care_unit: str) -> str:
        minimum_workers = MINIMUM_STAFF[care_unit]
        formatted_text = f"Antal: {minimum_workers}"

        return formatted_text

