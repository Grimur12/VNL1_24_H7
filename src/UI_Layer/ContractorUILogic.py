from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .ViewUILogic import ViewUILogic
from .Displays import Displays

# Here is our Contractor UI Logic File where we have all of the Contractor's communication with the UI.

class ContractorUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.ViewUI = ViewUILogic()
        self.Displays = Displays()

    def run(self):
        #Here is the menu for the Contractor. In the menu you can view all of the things the contractor can do.
        while True:
            print("--- Contractor ---")
            print("1: Create a Maintenance Report")
            print("2: Mark a Maintenance Report as ready to close")
            print("3: Access viewing features")
            print("B: Go Back")
            print("Q: Quit")
            user_choice = input("Choice: ")

            # The user chooses to quit the program.
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            # The user chooses to go back in the program.
            if user_choice.lower() == "b":
                print("Going back")
                break
            
            # The user chooses to create a maintenance report.
            if user_choice == "1":
                self.createMaintenanceReport()

            # The user chooses to mark a Maintenance report as ready to close.
            elif user_choice == "2":
                ID = input("ID of the Maintenance Report you want to mark as ready to close: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewUI.clearTerminal()
                    continue

                self.markMaintenanceReportAsClosed()

            # If user chooses to access viewing features.
            elif user_choice == "3":
                self.ViewUI.viewMenu()
            else:
                print("Invalid Input")

    # Here is the function to create a maintenance report
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