import os
from Model.InitializeData.SetInitialData import SetInitialData
from pathlib import Path


class CheckInitialData:
    """
    Checks all initial data for the application
    """

    application_pathway: str = None
    template_pathway: str = None
    template_subdir: str = r"\Grundmall\Grundmall.xlsx"

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
    def check_pathways_exist(cls) -> bool:
        """
        1. Gets the application´s current pathway
        2. Gets the templates pathway
        :return: True if the templates pathway relative to the application is correct, else False
        """
        cls.get_and_set_application_pathway()
        return cls.check_template_exist(cls.application_pathway)

    @classmethod
    def get_and_set_application_pathway(cls) -> None:
        cls.application_pathway = os.path.dirname(os.path.abspath(__file__))

    @classmethod
    def check_template_exist(cls, application_directory: str) -> bool:
        """
        Checks to see if the template for the Excel file exists and can be read
        """
        base_path = Path(application_directory).parents[1]

        template = f"{base_path}{cls.template_subdir}"

        # Does the template exist with the correct name, and can we read it
        if os.path.exists(template) and os.access(template, os.R_OK):
            cls.template_pathway = template
            return True

        return False
