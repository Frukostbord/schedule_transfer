from Model.Data.MinimumStaff import MINIMUM_STAFF
from openpyxl import worksheet, workbook
from Model.FileReadingWriting.DataFormatter import DataFormatter


class FormatExcelTemplate:
    """
    This class formats the rows for each care unit, depending on how many employees there are there
    """
    @classmethod
    def format_excel_template(cls, care_unit_unformatted: str, workbook_template: workbook) -> None:
        """
        This method removes the amount of rows in the template corresponding to the amount of employees in the current
        care unit.
        :param care_unit_unformatted: current care unit unformatted string (the whole pathway)
        :param workbook_template: the whole workbook
        :return: True if everything went fine, else False
        """

        care_unit = DataFormatter.get_care_unit_name(care_unit_unformatted)

        minimum_staff = cls.get_minimum_staff(care_unit)
        work_sheet = workbook_template["Mall"]

        cls.remove_replacement(minimum_staff, work_sheet)
        cls.remove_ordinary_employee(minimum_staff, work_sheet)


    @classmethod
    def get_minimum_staff(cls, care_unit: str) -> int:
        """
        Gets minimum workers
        :param care_unit: care_unit to get minimum workers from
        :return: minimum workers as an int
        """
        return MINIMUM_STAFF[care_unit]

    @classmethod
    def remove_replacement(cls, staff: int, work_sheet: worksheet) -> None:
        """
        Removes rows in the template of the replacement personnel
        :param staff: number of staff for the care_unit
        :param work_sheet: worksheet to delete it from
        """
        rows_to_remove = 6 - staff - 1
        starting_row = 21

        if rows_to_remove > 0:
            for row in range(starting_row, starting_row-rows_to_remove, -1):
                work_sheet.delete_rows(row)

    @classmethod
    def remove_ordinary_employee(cls, staff: int, work_sheet: worksheet) -> None:
        """
        Removes rows in the template of the ordinary employees
        :param staff: number of staff for the care_unit
        :param work_sheet: worksheet to delete it from
        """
        rows_to_remove = (6 - staff - 1) * 2
        starting_row = 15

        if rows_to_remove > 0:
            halfway_point = rows_to_remove // 2

            for i, row in enumerate(range(starting_row, starting_row-rows_to_remove, -1)):
                work_sheet.delete_rows(row)

                # Adjust the row height to be uniform. Only for visual effect
                if i >= halfway_point:
                    work_sheet.row_dimensions[row].height = 25

