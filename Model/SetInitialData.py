import Pathways


class SetInitialData:
    """ Method for setting all the initial data """
    @classmethod
    def set_initial_data(cls, application_pathway: str, template_pathway: str) -> None:
        cls.set_initial_pathways(application_pathway, template_pathway)

    @classmethod
    def set_initial_pathways(cls, application_pathway: str, template_pathway: str) -> None:
        """ Sets initial data, in the form of the pathway and check if the template exist """
        cls.set_application_pathway(application_pathway)  # Set the pathway to where the application is.
        cls.set_template_pathway(template_pathway)

    @classmethod
    def set_application_pathway(cls, application_pathway: str) -> None:
        """ Sets the application pathway to where it currently is """
        Pathways.APPLICATION_PATHWAY = r"{}".format(application_pathway)


    @classmethod
    def set_template_pathway(cls, template_pathway: str) -> None:
        Pathways.TEMPLATE_WORKBOOK_PATHWAY = r"{}".format(template_pathway)


