from Model.CheckPaths.CheckFile import CheckFiles


class CheckSavePath:

    @classmethod
    def check_save_path(cls, file_path: str) -> bool:
        return CheckFiles.check_pathway(file_path)
