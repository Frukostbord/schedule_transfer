from enum import Enum


class TransferStage(Enum):
    """
    Contains transfer stages and method to jump to the next transfer stage,
    during the data transfer from the .csv file(s) to the Excel file(s).
    """

    CREATE_COPY = 0
    PROCESS_DATA = 1
    EXPORT_DATA = 2
    TRANSFER_COMPLETE = 3

    @staticmethod
    def get_next_stage(stage: 'TransferStage') -> 'TransferStage':
        """
        Jumps to the next step in the transfer stage process.

        :param stage: Current stage of type TransferStage.
        :return: Next transfer stage of type TransferStage.
        :raises IndexError: If there is no next stage available.
        """

        # Convert the Enum to a list of stages
        stages = list(TransferStage)

        # Find the current stage's index
        index = stages.index(stage)

        # Check if it's not the last stage, then return the next one
        if index + 1 < len(stages):
            return stages[index + 1]
        else:
            raise IndexError("No next stage available; this is the last stage.")
