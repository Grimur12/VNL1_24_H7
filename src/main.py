from UI_Layer.ContractorUILogic import ContractorUILogic
from UI_Layer.EmployeeUILogic import EmployeeUILogic
from UI_Layer.ManagerUILogic import ManagerUILogic
from UI_Layer.ViewUILogic import ViewUILogic
from prettytable import PrettyTable
from UI_Layer.Displays import Displays

class main:
    def __init__(self):
        self.ContractorUI = ContractorUILogic()
        self.EmployeeUI = EmployeeUILogic()
        self.ManagerUI = ManagerUILogic()
        self.ViewUI = ViewUILogic()
        self.Displays = Displays()

    def runProgram(self) -> None:
        """Function takes in inital input for which UI he wishes to use going forward"""
        invalid = False
        while True: 
            self.ViewUI.clearTerminal()
            print(self.Displays.MainMenu())

            if invalid:
                print("Error: Invalid Input. Valid inputs are 1, 2 or 3 with no trailing commas or spaces\n")
                invalid = False

            initial_input = input("Choice: ")

            if initial_input.lower() == "q":
                print("Quitting")
                return
            # You can not back out of the main menu so you either pick a value or you quit, other UI's can pass q back into this function to quit aswell
            elif initial_input == "1":
                if self.ManagerUI.run() == "q": # Check if the user wants to quit
                    return
            elif initial_input == "2":
                if self.EmployeeUI.run() == "q": # Check if the user wants to quit
                    return
            elif initial_input == "3":
                if self.ContractorUI.run() == "q": # Check if the user wants to quit
                    return
            else:
                invalid = True

if __name__ == "__main__":
    main().runProgram()
            