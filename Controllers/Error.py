from View.GUI import FileTransferView

class Error:
    @staticmethod
    def error_message(message) -> None:
        FileTransferView.show_message(message)
