from CreateCopy import CreateCopy
from FileTransfer import FileTransfer
import Pathways

# Start program here
if __name__ == '__main__':
    # Create copies for the Excel files to be saved at from the template
    CreateCopy.create_copies()

    # All the pathways where the original document is and where it´s to be copied
    pathways = Pathways.DICTIONARY_PATHWAYS

    # Go through each file and export it to the newly formatted Excel file
    for path in pathways.keys():
        old_file = pathways[path][0]
        new_file = pathways[path][1]

        FileTransfer(old_file, new_file)

    print("File transfer was succesful!")