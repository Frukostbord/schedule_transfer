from enum import Enum


class TransferStage(Enum):
    CHECK_FILES = 0
    PROCESS_DATA = 1
    EXPORT_DATA = 2
