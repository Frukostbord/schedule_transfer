import os


class CheckFiles:

    @staticmethod
    def check_single_file_type(file_path: str, expected_extension: str) -> bool:
        """ Checks a single file's extension against the expected extension """
        _, file_extension = os.path.splitext(file_path)

        return file_extension.lower() == expected_extension.lower()

    @staticmethod
    def check_file_path(path: str) -> bool:
        return os.path.exists(path)