from Model.InitializeData.CheckInitialData import CheckInitialData
from Model.InitializeData.SetInitialData import SetInitialData


class InitializeData:
    """
    Class responsible for initializing the data for the application
    """

    application_pathway: str = ""
    template_pathway: str = ""

    @classmethod
    def initialize_data(cls) -> bool:
        """
        If all data could be found, set all the data in the model
        :return: True if data could be found and sets it, else False
        """
        if cls.check_initial_data():
            cls.set_initial_data()
            return True

        return False

    @classmethod
    def check_initial_data(cls) -> bool:
        """
        Checks to see if the data is correct
        :return: True if data could be found, else False
        """
        check = CheckInitialData()

        if check.check_initialization_data():
            cls.application_pathway = check.get_application_pathway()
            cls.template_pathway = check.get_template_pathway()

            if cls.template_pathway and cls.application_pathway:

                return True

        return False

    @classmethod
    def set_initial_data(cls) -> None:
        """
        Sets all data
        """
        SetInitialData.set_initial_data(cls.application_pathway, cls.template_pathway)