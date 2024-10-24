import os
from pathlib import Path
import sys


class CheckInitialData:
    """
    Checks all initial data for the application
    """

    application_pathway: str = None
    template_pathway: str = None
    template_subdir: str = r"Grundmall.xlsx"

    @classmethod
    def check_initialization_data(cls) -> bool:
        """
        Checks all data needed for the applications initialization
        :return: True if all files could be found, else False
        """

        if cls.check_pathways_exist():
            return True

        return False

    @classmethod
    def get_application_pathway(cls) -> str:
        return cls.application_pathway

    @classmethod
    def get_template_pathway(cls) -> str:
        return cls.template_pathway


    @classmethod
    def check_pathways_exist(cls) -> bool:
        """
        1. Gets the application´s current pathway
        2. Gets the templates pathway
        :return: True if the templates pathway relative to the application is correct, else False
        """
        cls.check_template()
        return cls.check_template_exist(cls.application_pathway)

    @classmethod
    def check_template(cls) -> None:
        cls.application_pathway = os.path.dirname(sys.executable)

    @classmethod
    def check_template_exist(cls, application_directory: str) -> bool:
        """
        Checks to see if the template for the Excel file exists and can be read
        """
        # Search for the file in the directory and its subdirectories
        for root, dirs, files in os.walk(application_directory):
            if cls.template_subdir in files:
                # Construct the full path of the found file
                found_file_path = os.path.join(root, cls.template_subdir)

                # Check if we can write to the file
                if os.access(found_file_path, os.W_OK):
                    # If both conditions are met, set the template_pathway and return True
                    cls.template_pathway = found_file_path
                    return True

        # If the file wasn't found or not writable, return False
        return False
