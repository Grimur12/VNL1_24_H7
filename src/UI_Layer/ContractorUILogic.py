from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .ViewUILogic import ViewUILogic
from .Displays import Displays

class ContractorUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.ViewUI = ViewUILogic()
        self.Displays = Displays()

    def run(self):
        while True:
            print("------------------ Contractor ------------------")
            print("What do you want to do?")
            print("1: To create a Maintenance Report")
            print("2: To mark a Maintenance Report as ready to close")
            print("3: To access viewing features")
            print("B: to go Back")
            print("Q: to quit")
            print("-------------------------------------------------")
            user_choice = input("Choice ")

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            if user_choice.lower() == "b":
                print("Going back")
                break

            if user_choice == "1":
                self.createMaintenanceReport()
            elif user_choice == "2":
                ID = input("ID of the Maintenance Report you want to mark as ready to close: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewUI.clearTerminal()
                    continue

                self.markMaintenanceReportAsClosed()
            elif user_choice == "3":
                self.ViewUI.viewMenu()
            else:
                print("Invalid Input")

    def createMaintenanceReport(self):
        count = 1
        tempMaintenanceReport = self.LogicLayerWrapper.createTempMaintenanceReport()
        error_message = None
        while count < 4:
            self.Displays.display_temp_maintenanceReport(tempMaintenanceReport, error_message)
            userInput = input("Information : ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput.lower() == "b":
                self.ViewUI.clearTerminal()
                break

            try:
                if self.LogicLayerWrapper.validateMaintenanceReportContractorInput(userInput, count, tempMaintenanceReport):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        
        if userInput.lower() != "b":
            self.Displays.display_temp_maintenanceReport(tempMaintenanceReport, error_message)
            self.LogicLayerWrapper.createMaintenanceReport(tempMaintenanceReport)
            print("You have successfully created a new Maintenance Report")

    def markMaintenanceReportAsClosed(self):
        print("Not implemented ")
        # Mark maintenance report as ready to be closed,
        # The manager can look at the report see it as ready to be closed and then close the maintenance task assoicated with the maintenance report ??