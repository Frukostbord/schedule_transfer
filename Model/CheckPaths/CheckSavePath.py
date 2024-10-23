from Model.CheckPaths.CheckFile import CheckFiles


class CheckSavePath:
    """
    Checks to see if the directory to save files is correct
    """

    @classmethod
    def check_save_path(cls, file_path: str) -> bool:
        """
        Checks to see if the file´s pathway is correct
        :param file_path: pathway of save path
        :return: True if it´s correct, else False
        """
        if file_path:
            return CheckFiles.check_pathway(file_path)
        return False
