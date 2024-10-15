from Model.InitializeData.CheckInitialData import CheckInitialData


class InitializeData:

    @staticmethod
    def initialize_data() -> bool:
        return CheckInitialData.initialize_data()
