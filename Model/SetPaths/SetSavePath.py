import Model.Data.Pathways as Pathways


class SetSavePath:

    @classmethod
    def set_save_path(cls, file_path: str) -> None:
        Pathways.SAVE_PATH = file_path
