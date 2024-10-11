import os


class SetInitialData:
    """ Method for setting all the initial data """

    model = None  # Model to be received for initialization of data

    @classmethod
    def set_initial_data(cls, model) -> bool:
        cls.model = model
        cls.set_initial_pathways()

        return cls.set_initial_pathways()

    @classmethod
    def set_initial_pathways(cls) -> bool:
        """ Sets initial data, in the form of the pathway and check if the template exist """
        application_directory = cls.model.set_application_pathway()  # Set the pathway to where the application is.
        return cls.check_template_exist(application_directory)  # See if the template exist, so copying can begin.

    @classmethod
    def set_application_pathway(cls) -> str:
        """ Sets the application pathway to where it currently is """
        application_directory = r"{}".format(os.path.dirname(os.path.abspath(__file__)))

        cls.model.set_program_pathway = application_directory
        return application_directory

    @classmethod
    def check_template_exist(cls, application_directory: str) -> bool:
        """ Checks to see if the template for the Excel file exists """
        template = r"{}".format(application_directory + r"\Grundmall\Grundmall.xlsx")

        return os.path.exists(template)
