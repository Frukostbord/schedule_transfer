import os
from SetInitialData import SetInitialData


class CheckInitialData:
    application_pathway: str = None
    template_pathway: str = None

    @classmethod
    def check_initial_data(cls) -> bool:
        cls.check_pathways_exist()

        if cls.template_pathway:
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
        template = application_directory + r"\Grundmall\Grundmall.xlsx"

        if os.path.exists(template):
            cls.template_pathway = template
            return True

        return False
