from Model.Enum.TransferStages import TransferStage

# Error messages depending upon TransferStage in the File Transfer process
ERROR_MESSAGES_TRANSFERSTAGE: dict = {
    TransferStage.CREATE_COPY: "Något gick fel när grundmallen skulle kopieras.",
    TransferStage.FORMAT_TEMPLATE: "Det gick inte ändra i grundmallen för antalet medarbetare på enheten, "
                                   "se över grundmallen.",
    TransferStage.PROCESS_DATA: "Något gick fel när filen ifrån TimeCare skulle göras om.",
    TransferStage.EXPORT_DATA: "Något gick fel när det nya schemat skulle skapas."
}

# Error displaying if certain data is missing
ERROR_MESSAGE_CHECK_DATA:  dict = {
    "APPLICATION_PATHWAY": "Systemet kunde inte hitta sin egna sökväg",
    "CSV_FILES": "Inga filer ifrån TimeCare har blivit valda",
    "SAVE_PATH": "Ingen sökväg där nya filerna sparas har blivit vald",
    "TEMPLATE_PATH": "Kunde inte hitta grundmallen"
}
