from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .ViewUILogic import ViewUILogic
from .Displays import Displays
from prettytable import PrettyTable

class EmployeeUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.ViewUI = ViewUILogic()
        self.Displays = Displays()

    def run(self):
        self.ViewUI.clearTerminal() 
        while True:
            print(self.Displays.EmployeeMenu())
            user_choice = input("Choice ")
            # Exit out of the loop

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            if user_choice.lower() == "b":
                print("Going back")
                break

            if user_choice == "1":
                self.createMaintenanceReport()
            elif user_choice == "2":
                self.ViewUI.viewMenu()
            else:
                print("Invalid Input")

    def createMaintenanceReport(self):
        count = 1
        tempMaintenanceReport = self.LogicLayerWrapper.createTempMaintenanceReport()
        error_message = None
        aborted = False
        while count < 4:
            self.Displays.display_temp_maintenanceReport(tempMaintenanceReport, error_message)
            userInput = input("Information : ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput.lower() == "b":
                self.ViewUI.clearTerminal()
                aborted = True
                break

            try:
                if self.LogicLayerWrapper.validateMaintenanceReportEmployeeInput(userInput, count, tempMaintenanceReport):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
            except KeyError as error:
                print(error)
                aborted = True
                break
        
        if not aborted:
            self.Displays.display_temp_maintenanceReport(tempMaintenanceReport, error_message)
            self.LogicLayerWrapper.createMaintenanceReport(tempMaintenanceReport)
            print("You have successfully created a new Maintenance Report")