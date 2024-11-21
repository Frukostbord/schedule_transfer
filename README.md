This programs purpose is to transfer information from .csv files with certain formats in to a 
formatted Excel file.

The program is coded in Python, using the module tkinter for the GUI.

The coding paradigm is MVC to achieve decoupling:
Model: Where all the business logic happens
View: Where the user interacts with program
Controller: Where the program controls processed information and relays information between the view and model

1. The program initiates and checks if the excel template exists
2. GUI shows up where the user can:<br />
   a. Choose which .csv files to copy over from<br />
   b. Where the new files should be saved<br />
   c. Start the data transfer process<br />
3. After the process, all selected files are cleared from the selection and the newly created and formatted excel files will be shown to the user.
