import tkinter as tk

from Controllers import Controller
from Model import ModelMain
from View import ViewFileTransfer

"""
Program for transferring data from a .csv file with a certain format in to a .excel sheet with a certain format.
The program uses a MVC paradigm to structure the code.
M = Model, where the business logic happens
V = View, what the user sees and is displayed for the user
C = Controller, handles communication between the Model and View
"""

# Starts program here
if __name__ == '__main__':
    root = tk.Tk()
    model = ModelMain.ModelMain()  # Initiate the model
    controller = Controller.FileTransferController(model)  # Initiate the Controllers

    if controller.initialize_data():
        view = ViewFileTransfer.FileTransferView(root, controller)  # Initiate the GUI
        root.mainloop()  # Loop the application until the user quits
    else:
        # Create a temporary view to show an error message
        view = ViewFileTransfer.FileTransferView(root, controller)
        view.show_error_message("Grundmallen kunde inte hittats. Programmet avslutas.")