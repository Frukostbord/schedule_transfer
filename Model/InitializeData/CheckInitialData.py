import os
from Model.InitializeData.SetInitialData import SetInitialData
from pathlib import Path


class CheckInitialData:
    application_pathway: str = None
    template_pathway: str = None
    template_subdir: str = r"\Grundmall\Grundmall.xlsx"

    @classmethod
    def initialize_data(cls) -> bool:
        if cls.check_pathways_exist():
            SetInitialData.set_initial_data(cls.application_pathway, cls.template_pathway)
            return True

        return False

    @classmethod
    def check_pathways_exist(cls) -> bool:
        cls.get_program_pathway()
        return cls.check_template_exist(cls.application_pathway)

    @classmethod
    def get_program_pathway(cls) -> None:
        cls.application_pathway = os.path.dirname(os.path.abspath(__file__))


    @classmethod
    def check_template_exist(cls, application_directory: str) -> bool:
        """ Checks to see if the template for the Excel file exists """
        base_path = Path(application_directory).parents[1]

        template = f"{base_path}{cls.template_subdir}"

        if os.path.exists(template):
            cls.template_pathway = template
            return True

        return False
