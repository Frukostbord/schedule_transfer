import Model.Data.Pathways as Pathways


class RemoveCSVFiles:

    @staticmethod
    def remove_csv_files(indexes_files_to_remove: tuple[int]) -> None:
        # Create a list of keys to remove from the dictionary
        keys_to_remove = []

        # Enumerate over the dictionary to find matching indices
        for index, (key, value) in enumerate(Pathways.DICTIONARY_PATHWAYS.items()):
            if index in indexes_files_to_remove:
                keys_to_remove.append(key)

        # Remove the corresponding items from the dictionary
        for key in keys_to_remove:
            del Pathways.DICTIONARY_PATHWAYS[key]
