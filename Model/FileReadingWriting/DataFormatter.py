import os
from Model.Data.MinimumStaff import MINIMUM_STAFF


class DataFormatter:
    """
    This class formats strings in different ways, to later be used
    when transferring data to the Excel sheet
    """

    @staticmethod
    def format_date(data: list[str]) -> list[str]:
        """
        Method for getting the date in the correct information
        """
        date_formatted = []

        week = DataFormatter.get_week(data[:2])
        date_formatted.append(week)

        for i in range(3, len(data), 2):
            clean_string = data[i].replace(";", "")  # Removes ";"
            date_formatted.append(clean_string)

        return date_formatted

    @staticmethod
    def remove_semicolon(string: str) -> str:
        """
        Removes semicolon from a string
        :param string: string to remove semicolons from
        """
        new_string = string.replace(";", "")
        return new_string

    @staticmethod
    def format_employee_work_time(data: list) -> list:
        """
        Formats the data from the .csv file, to a uniform list of data to be inserted in to
        the Excel file
        :param data: list of raw data from the .csv file
        :return: list of formatted data
        """

        data.pop()  # Removes total hours worked, at the end of the list
        worker_name = (DataFormatter.get_worker_name(data[:2]))  # Get worker names
        cleaned_data: list = worker_name  # Add worker names

        worker_times = DataFormatter.get_worker_times(data[2:])  # Get all work times for the different workers
        cleaned_data += worker_times

        return cleaned_data

    @staticmethod
    def get_week(data: list) -> str:
        """
        Gets the week from a list of strings
        :param data: List with information of data from .csv file
        :return: Week from list of .csv data
        """
        week = " ".join(data)

        week = week.replace(";", "")
        return week

    @staticmethod
    def get_worker_name(data: list[str]) -> list:
        """
        Formats raw .csv data to get the worker´s name
        :param data: .csv data to be formatted
        :return: Worker´s name
        """

        first_name = DataFormatter.remove_semicolon(data[0])
        last_name = DataFormatter.remove_semicolon(data[1])

        name = [first_name, last_name]

        return name

    @staticmethod
    def get_worker_times(data: list) -> list:
        """
        Gets a list of .csv data, which are workers work time. The method reformat it for easier use.
        :param data:
        :return:
        """
        worker_times = []

        curr_worker_time = []
        # We iterate through the raw data. If
        for i in range(len(data)):
            # A time will have ":" in it, like 07:00
            if ":" in data[i]:
                curr_worker_time.append(data[i])
            elif data[i] == ";;;;":  # Means in the CSV file that the worker don´t work that day
                worker_times.append("")  # Add an empty string to say that they don´t work that day

            # When we have two times e.g [07:00, 15:00], which is the start and finishing time,
            # the data is sent to be formatted, then added to that worker´s work time
            if len(curr_worker_time) == 2:
                time = DataFormatter.format_worker_time(curr_worker_time)
                worker_times.append(time)
                curr_worker_time = []

        return worker_times

    @staticmethod
    def format_worker_time(data: list[str]) -> str:
        """
        Simple string formatted of a workers time
        :param data: List of two strings, e.g ["08:00", "16:30"]
        :return: formatted string of worker time
        """
        not_formatted_worker_time = "-".join(data)
        formatted_worker_time = DataFormatter.remove_semicolon(not_formatted_worker_time)

        return formatted_worker_time

    @staticmethod
    def get_care_unit_name(unformatted_care_unit_name: str) -> str:
        """
        Gets the last part of a string path
        :param unformatted_care_unit_name: string of a path
        :return: last part of the string, which is the care unit
        """
        care_unit_name = os.path.splitext(os.path.basename(unformatted_care_unit_name))[0]

        return care_unit_name

    @staticmethod
    def get_minimum_worker_formatted(care_unit: str) -> str:
        """
        Gets data from an enum of minimum workers for each care unit
        :return: string of minimum workers
        """
        minimum_workers = MINIMUM_STAFF[care_unit]
        formatted_text = f"Antal: {minimum_workers}"

        return formatted_text
