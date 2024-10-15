import os


class CheckFiles:

    @staticmethod
    def check_pathway(pathway: str, file_format=None) -> bool:
        if not pathway:
            return False

        check = CheckFiles.check_file_permission(pathway) and CheckFiles.check_file_path(pathway)

        if file_format:
            check = check and CheckFiles.check_file_type(pathway, file_format)

        return check

    @staticmethod
    def check_pathways(pathways: list, file_format=None) -> bool:
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
        """ Checks a single file's extension against the expected extension """
        if not file_path:
            return False

        _, file_extension = os.path.splitext(file_path)

        return file_extension.lower() == expected_extension.lower()

    @staticmethod
    def check_file_path(path: str) -> bool:
        if not path:
            return False

        return os.path.exists(path)

    @staticmethod
    def check_file_permission(path: str) -> bool:
        if not path:
            return False

        return os.access(path, os.W_OK)
