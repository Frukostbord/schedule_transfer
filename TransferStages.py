from enum import Enum


class TransferStage(Enum):
    CHECK_FILES = 0
    PROCESS_DATA = 1
    EXPORT_DATA = 2

    @staticmethod
    def get_next_stage(stage):
        # Convert the Enum to a list of stages
        stages = list(TransferStage)

        # Find the current stage's index
        index = stages.index(stage)

        # Check if it's not the last stage, then return the next one
        if index + 1 < len(stages):
            return stages[index + 1]
        else:
            raise IndexError
