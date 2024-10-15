from Model.Enum.TransferStages import TransferStage

# Error message translator for Swedish
ERROR_MESSAGES_TRANSLATED: dict = {
    "Application_pathway": "Applikationen kunde inte hitta sin egna sökväg.",
    "CSV_files": "Det finns inga filer, eller så är vissa filer av fel format.",
    "Save_path": "Ingen sökväg vald var filer ska sparas",
    "Template_path": "Grundmallen hittades inte"
}

ERROR_MESSAGES_TRANSFERSTAGE: dict = {
    TransferStage.CREATE_COPY: "Något gick fel när grundmallen skulle kopieras.",
    TransferStage.PROCESS_DATA: "Något gick fel när filen ifrån TimeCare skulle göras om.",
    TransferStage.EXPORT_DATA: "Något gick fel när det nya schemat skulle skapas."
}
