from Model.Enum.TransferStages import TransferStage

# Error messages depending upon TransferStage in the File Transfer process
ERROR_MESSAGES_TRANSFERSTAGE: dict = {
    TransferStage.CREATE_COPY: "Något gick fel när grundmallen skulle kopieras.",
    TransferStage.PROCESS_DATA: "Något gick fel när filen ifrån TimeCare skulle göras om.",
    TransferStage.EXPORT_DATA: "Något gick fel när det nya schemat skulle skapas."
}

ERROR_MESSAGE_CHECK_DATA:  dict = {


}
