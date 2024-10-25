import Model.Data.Pathways as Pathways


class ResetData:
    """
    Resets data in the application
    """

    @staticmethod
    def reset_data() -> None:
        """
        Resets all user input data
        """
        ResetData.reset_csv_pathways()
        ResetData.reset_save_pathway()

    @staticmethod
    def reset_save_pathway() -> None:
        """
        Resets save path
        """
        Pathways.SAVE_PATH = ""

    @staticmethod
    def reset_csv_pathways() -> None:
        """
        Resets csv. pathway(s)
        """
        Pathways.DICTIONARY_PATHWAYS = {}
