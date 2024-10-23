import os


class CheckFiles:
    """
    Checks if a file exists, if it can be written and file type
    """

    @staticmethod
    def check_pathway(pathway: str, file_format=None) -> bool:
        """
        Checks a single pathway
        :param pathway: pathway of file
        :param file_format: file format to check - OPTIONAL
        :return: True if pathway exists and file format is correct, else False
        """
        if not pathway:
            return False

        check = CheckFiles.check_file_permission(pathway) and CheckFiles.check_file_path(pathway)

        if file_format:
            check = check and CheckFiles.check_file_type(pathway, file_format)

        return check

    @staticmethod
    def check_pathways(pathways: list, file_format=None) -> bool:
        """
        Checks several pathways
        :param pathways: pathway of file
        :param file_format: file format to check - OPTIONAL
        :return: True if pathway exists and file format is correct, else False
        """

        if not pathways:
            return False

        for pathway in pathways:
            check = CheckFiles.check_file_permission(pathway) and CheckFiles.check_file_path(pathway)

            if file_format:
                check = check and CheckFiles.check_file_type(pathway, file_format)

            if not check:
                return False

        return True

    @staticmethod
    def check_file_type(file_path: str, expected_extension: str) -> bool:
        """
        Checks a single file's extension against the expected extension
        :param file_path: file´s path
        :param expected_extension: extension of file
        :return: True if file has the correct extension, else False
        """
        if not (file_path and expected_extension):
            return False

        _, file_extension = os.path.splitext(file_path)

        return file_extension.lower() == expected_extension.lower()

    @staticmethod
    def check_file_path(path: str) -> bool:
        """
        Checks to see if the file path exists
        :param path: path of file to check
        :return: True if it exists, else False
        """

        if not path:
            return False

        return os.path.exists(path)

    @staticmethod
    def check_file_permission(path: str) -> bool:
        """
        Check if we can write data on the file
        :param path: path of file
        :return: True if we can write data, else False
        """
        if not path:
            return False

        return os.access(path, os.W_OK)
