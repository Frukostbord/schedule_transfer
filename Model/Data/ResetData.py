import Model.Data.Pathways as Pathways


class ResetData:

    @staticmethod
    def reset_data() -> None:
        ResetData.reset_csv_pathways()
        ResetData.reset_save_pathway()

    @staticmethod
    def reset_save_pathway() -> None:
        Pathways.SAVE_PATH = ""

    @staticmethod
    def reset_csv_pathways() -> None:
        Pathways.DICTIONARY_PATHWAYS = {}

