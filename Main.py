import tkinter as tk
from Controllers import Controller
from View import GUI
from Model.ModelMain import ModelMain

# Start program here
if __name__ == '__main__':
    root = tk.Tk()
    model = ModelMain()  # Initiate the model
    viewmodel = Controller.FileTransferController(model)  # Initiate the Controllers
    app = GUI.FileTransferView(root, viewmodel)  # Initiate the GUI

    root.mainloop()  # Loop the application until the user quits
