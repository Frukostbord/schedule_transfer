from View.GUI import FileTransferView

class PopupMessage:
    @staticmethod
    def error_message(message: str) -> None:
        FileTransferView.show_error_message(message)

    @staticmethod
    def pop_up_message(title: str, message: str) -> None:
        FileTransferView.show_message(title, message)
