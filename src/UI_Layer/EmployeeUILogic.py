from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .ViewUILogic import ViewUILogic
from .Displays import Displays
from prettytable import PrettyTable 

# Here is our class of Employee UI Logic where we have all of the employee communication with the UI.

class EmployeeUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.ViewUI = ViewUILogic()
        self.Displays = Displays()

    def run(self):
        while True:



            # All of his functions are here
            # print("1: Create a Maintenance Report")
            # print("2: Mark a Maintenance Report as ready to close")
            # print("3: Viewing features")
            # print("B: Go Back")
            # print("Q: Quit")



            # Here is the menu for the employee, you can view here all of the things the employee can do
            employee_m_menu = PrettyTable()
            employee_m_menu.title = " Employee Menu"
            employee_m_menu.header = False
            employee_m_menu.add_row(["1: Create a Maintenance Report"])
            employee_m_menu.add_row(["2: Mark a Maintenance Report as ready to close"])
            employee_m_menu.add_row(["3: Viewing features"])
            employee_m_menu.add_row(["B: Go Back"])
            employee_m_menu.add_row(["Q: Quit"])

            employee_m_menu.align = "l"
            print(employee_m_menu)
            # Exit out of the loop

            print("What would you like to do today?")
            user_choice = input("Choice: ")

            # The user decides to quit
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            # The user decides to go back in the program
            if user_choice.lower() == "b":
                print("Going back")
                break

            # The user chooses to create a Maintenance Report
            if user_choice == "1":
                self.createMaintenanceReport()
            
            # The user chooses to mark the Maintenance report as ready to close
            elif user_choice == "2":
                ID = input("ID of the Maintenance Report you want to mark as ready to close: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewUI.clearTerminal()
                    continue

                self.markMaintenanceReportAsClosed()

            # The user chooses to access viewing features
            elif user_choice == "3":
                self.ViewUI.viewMenu()
            else:
                print("Invalid Input")

    
    def createMaintenanceReport(self):
        count = 1
        tempMaintenanceReport = self.LogicLayerWrapper.createTempMaintenanceReport()
        error_message = None
        while count < 3:
            self.Displays.display_temp_maintenanceReport(tempMaintenanceReport, error_message)
            userInput = input("Information : ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput.lower() == "b":
                self.ViewUI.clearTerminal()
                break

            try:
                if self.LogicLayerWrapper.validateMaintenanceReportEmployeeInput(userInput, count, tempMaintenanceReport):
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