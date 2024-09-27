import shutil
import Pathways


class CreateCopy:

    @staticmethod
    def create_copies():
        copy_pathways = Pathways.DICTIONARY_PATHWAYS  # Pathways of all copies, where they´re of to
        template_pathway = Pathways.TEMPLATE_WORKBOOK_PATHWAY

        for path in copy_pathways.keys():
            template_copy_pathway = copy_pathways[path][1]
            CreateCopy.create_copy(template_pathway, template_copy_pathway)

    @staticmethod
    def create_copy(original_path: str, copy_path: str):
        shutil.copy(original_path, copy_path)

