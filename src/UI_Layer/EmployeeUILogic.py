from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .ViewUILogic import ViewUILogic
from .Displays import Displays
from prettytable import PrettyTable

class EmployeeUILogic:
    def __init__(self) -> None:
        """ Function holds LogicLayerWrapper so we can get the data we need from the logic layer, viewUI to view all the things we need and Displays for all user displays we need"""
        self.LogicLayerWrapper = LogicLayerAPI()
        self.ViewUI = ViewUILogic()
        self.Displays = Displays()

    def run(self) -> str:
        """ Function handles the UI user interaction for the employees,  returns str, q or b for back and quit purposes"""
        error_message = None
        while True:
            self.ViewUI.clearTerminal()
            print(self.Displays.EmployeeMenu())
            if error_message: # Error message handling to keep the UI clean, display the error message while clearing the screen 
                print(f"Error: {error_message}")
                error_message = None
            user_choice = input("Choice: ")

            if user_choice.lower() == "q": # Check if the user wants to quit
                print("Qutting")
                return "q" # Pass Q back into the main screen for it to quit the program

            if user_choice.lower() == "b": # Check if the user wants to go back to the main menu, to then choose another UI
                print("Going back")
                return "b"

            if user_choice == "1": # If we user wants to create a maintenance report
                result = self.createMaintenanceReport() # Call the maintenance report view menu 
                if result == "q": # Check if he wants to quit
                    return "q"
            elif user_choice == "2": # If the user wants to access the viewing features
                result = self.ViewUI.viewMenu() # Call the viewing functions menu
                if result == "q": # Check if he wants to quit
                    return "q"
            else:
                error_message = "Invalid Input"
                self.ViewUI.clearTerminal()

    def createMaintenanceReport(self) -> str: 
        """ Functon is makes it available to the contractor (user) to create a maintenance report on a task, returns str, q or b for back and quit purposes"""
        count = 1
        tempMaintenanceReport = self.LogicLayerWrapper.createTempMaintenanceReport() # Get a Temporary class Maintenance Report from the logic layer
        error_message = None # An error message for if the user inputs something he shouldn't
        title_message = "Creating a new Maintenance Report"
        input_strings = ["Enter Maintenance Task ID: ", "Enter An Employee ID: ", "Enter Cost Of Materials: "]
        while count < 4: # The count here is to keep track of how many inputs the user should input when creating the Maintenance Report
            self.ViewUI.clearTerminal()
            self.Displays.printMaintenanceReport(tempMaintenanceReport, title_message, error_message, mode = "hints") # Display the MaintenanceReport to the user each time he updates an attribute so he can keep track of what he is changing in real time
            userInput = input(f"{input_strings[count-1]}") # Actual user input here, he needs to input the information needed to create the maintenance report
            if userInput.lower() == "q": # Quit
                print("Quitting")
                return "q"
            elif userInput.lower() == "b": # Go back to the main contractor UI screen
                self.ViewUI.clearTerminal()
                return "b"

            try:
                # For each input the user inserts into the program we need to validate it, we pass the count to keep track of which attribute the user is changing, along with the maintenancereport object he is updating so the logic layer can make some changes
                if self.LogicLayerWrapper.validateMaintenanceReportEmployeeInput(userInput, count, tempMaintenanceReport):
                    count +=1
                    error_message = None  # If there is no error we update the error message since there may have been a previous error, this flushes it out on correct input
            except ValueError as error: # To print out what the user did wrong in input
                error_message = error
                continue
            except KeyError as error:  # This is a more serious error, for things like if the user is trying to create a maintenance report on a closed maintenance or on a maintenance that does not exist... Generally things which he shouldn't be able to do
                error_message = error
                continue
        self.ViewUI.clearTerminal() # All clear terminal commands are for user clarity, to not clutter the interface
        self.Displays.printMaintenanceReport(tempMaintenanceReport, title_message, error_message)# Final displaying of the report the user created
        self.LogicLayerWrapper.createMaintenanceReport(tempMaintenanceReport)# Pass all the user inputted information along to the logic layer 
        print("You have successfully created a new Maintenance Report")# Tell the user that the creation process was successful
        done_looking = input("Press any button if you are done: ")# The press any button if you are done mechanics are just for user clarity, in this case so that the user can easily see what he did without automatically going back to the employee menu
        if done_looking == "q": # Quit option
            print("Quitting")
            return "q"
        self.ViewUI.clearTerminal()  # Finally clear the terminal before going back to the employee menu