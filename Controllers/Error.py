from View.GUI import FileTransferView

class Error:
    @staticmethod
    def error_message(message: str) -> None:
        FileTransferView.show_message(message)
