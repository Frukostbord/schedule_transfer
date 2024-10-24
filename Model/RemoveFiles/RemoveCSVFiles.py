import Model.Data.Pathways as Pathways


class RemoveCSVFiles:
    """
    Removing CSV file pathways
    """
    @staticmethod
    def remove_csv_files(indexes_files_to_remove: tuple[int]) -> None:
        """
        1. Takes a tuple, converts it to a list and reverses it
        2. Enumerate through all keys, where if a index fits a key, put it in keys to be removed
        3. Remove all keys from highest index to lowest
        :param indexes_files_to_remove:
        """

        # Make tuple a list and reverse it
        list_keys_reversed = list(indexes_files_to_remove)[::-1]

        # Create a list of keys to remove from the dictionary
        keys_to_remove = []

        # Enumerate over the dictionary to find matching indices
        for index, (key, value) in enumerate(Pathways.DICTIONARY_PATHWAYS.items()):
            if index in list_keys_reversed:
                keys_to_remove.append(key)

        # Remove the corresponding items from the dictionary
        for key in keys_to_remove:
            del Pathways.DICTIONARY_PATHWAYS[key]
