from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .ViewUILogic import ViewUILogic
from .Displays import Displays
from prettytable import PrettyTable

class ManagerUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.ViewingUI = ViewUILogic()
        self.Displays = Displays()

    def run(self):
        error_message = None
        while True:
            self.ViewingUI.clearTerminal()
            print(self.Displays.ManagerMainMenu())
            if error_message:
                print(f"Error: {error_message}")
                error_message = None
            user_choice = input("Choice: ")

            if user_choice.lower() == "q": # Check if the user wants to quit
                print("Qutting")
                return "q" # Pass Q back into the main screen for it to quit the program

            if user_choice.lower() == "b": # Check if the user wants to go back to the main menu, to then choose another UI
                print("Going back")
                return "b"

            if user_choice == "1":
                result = self.addMenu()
                if result == "q":
                    return "q"
            elif user_choice == "2":
                result = self.editMenu()
                if result == "q":
                    return "q"
            elif user_choice == "3":
                result = self.ViewingUI.viewMenu()
                if result == "q":
                    return "q"
            else:
                error_message = "Invalid Input"
                self.ViewingUI.clearTerminal()

    def addMenu(self):
        self.ViewingUI.clearTerminal()
        error_message = None
        while True:
            print(self.Displays.ManagerAddMenu())
            if error_message:
                print(f"Error: {error_message}")
            user_choice = input("Choice: ")

            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                print("Going back")
                return "b"
            
            if user_choice in ["1", "2", "3"]:
                result = self.createEmployee(user_choice)
                if result == "q":
                    return "q"
            elif user_choice == "4":
                result = self.createProperty()
                if result == "q":
                    return "q" 
            elif user_choice == "5":
                result = self.createMaintenanceTask()
                if result == "q":
                    return "q"
            elif user_choice == "6":
                result = self.createMaintenanceSchedule()
                if result == "q":
                    return "q"
            else:
                error_message = "Invalid Input"
                self.ViewingUI.clearTerminal()

    def editMenu(self):
        self.ViewingUI.clearTerminal()
        error_message = None
        # Instead of having a very long nested elif statement we will have a dictionary of valid options and we will check on key in that dictionary for the users choice
        # Reduces code and makes it easier to read 
        validOptions = {
            "1": self.editEmployee,
            "2": self.editContractor,
            "3": self.editProperty,
            "4": self.editMaintenanceTask,
            "5": self.editMaintenanceSchedule,
            "6": self.LogicLayerWrapper.closeMaintenanceTask
        }
        # Another dict with the names of the relevant things user may want to edit to make it clear to the user what he is providing the ID for
        names_of_options = {
            "1": "Employee",
            "2": "Contractor",
            "3": "Property",
            "4": "Maintenance Task",
            "5": "Maintenance Schedule",
            "6": "Maintenance Task for Closing"
        }
        while True:
            print(self.Displays.ManagerEditMenu()) # Always display the menu so the user can see what options he has
            if error_message: # If there was an error message display it otherwise dont
                print(f"Error: {error_message}")
                error_message = None # Clear the error message so it dosent persist if the user inputs something wrong and then goes back
                
            user_choice = input("Choice: ") # Choice of what he wants to edit
            # Standard quit or back logic
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                print("Going back")
                return "b"
            
            elif user_choice.lower() in validOptions: # If the user picks any of the 1-6 numbers we call for an ID
                ID = input(f"ID of the {names_of_options[user_choice]} you want to edit: ") # Display the name of the thing he wants to edit from the name dict
                # Standard quit and go back logic for id
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b": # But we want to continue here because we dont want him to go all the way back to the manager menu, just choose another thing in the edit menu
                    self.ViewingUI.clearTerminal()
                    continue
                # We now know the user has either inputted invalid input so the else statement will catch that or a valid ID so we try calling the functions to edit the thing he wanted to edit
                try:
                    if user_choice == "6": # Necessary because to close a maintenance report you need the feedback from the manager,
                        user_feedback = input("Feedback on the Task you want to close: ") 
                        result = validOptions[user_choice](ID, user_feedback) # Call the referenced function for the closing since its of a different format we need more information for it, store the result, incase its a q or b
                    else:
                        result = validOptions[user_choice](ID) # Call the referenced function and store the result, incase its a q or b
                    # standard quit and back logic from the editing menus
                    if result == "q": 
                        print("Quitting")
                        return "q"  # Quit the program if any of those functions return q
                    elif result == "b":
                        self.ViewingUI.clearTerminal()
                        continue  # Go back to the editing screen if he presses b
                except ValueError as error: # If the inputs are wrong when editing we may get valueerrors so we display them to the user
                    error_message = error
                    self.ViewingUI.clearTerminal()
                except KeyError as error: # KeyErrors may arrive from editing or closing so we display that aswell
                    error_message = error
                    self.ViewingUI.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.ViewingUI.clearTerminal()

    
    def createEmployee(self,type_of_employee):

        # Type of employee should be "1" for Employee, "2" for Manager, "3" for Contractor 
        count = 1
        temp = self.LogicLayerWrapper.getTempEmployee(type_of_employee)
        error_message = None
        overWritten = False
        aborted = False # Flag to see if user has pressed b or does not want to overwrite manager
        title_message = ["Adding a new Employee","Adding a new Manager","Adding a new Contractor"] # Creating a list of the possible titles depending on what type of employee the user wants to create
        input_message = ["Enter Name: ", "Enter Social Security Number: ", "Enter Address: ", "Enter Home Phone: ", "Enter GSM Phone: ", "Enter Email: ", "Enter Work Location: ", "Enter Previous Task(s) (If Any): ", "Enter Performance Rating (If Any): ", "Enter Contractor Contact: ", "Enter Opening Hours: "]
        if type_of_employee == "3":
            max_parameters = 12
        else:
            max_parameters = 8
        while count < max_parameters:
            self.ViewingUI.clearTerminal()
            self.Displays.printEmployee(temp, title_message[int(type_of_employee)-1], error_message, mode="hints") # The type of employee decides what the title message is, we reference it on the type of employee by indexing it through that in the list of possible titles
            userInput = input(f"{input_message[count-1]}")
            if userInput.lower() == "q":
                print("Quitting")
                return "q"

            elif userInput.lower() == "b":
                print("Going back")
                aborted = True
                self.ViewingUI.clearTerminal()
                return "b"

            try:
                if self.LogicLayerWrapper.validateEmployeeInput(userInput, count, temp):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
            except KeyError:
                overWritten = self.overWriteManager(temp, userInput)
                count += 1
                if overWritten == "q":
                    return "q"
                elif not overWritten: # If we aborted creating the new manager then we break
                    aborted = True
                    break
            
        if not aborted:
            self.ViewingUI.clearTerminal()
            self.Displays.printEmployee(temp, title_message[int(type_of_employee)-1], error_message)
            self.LogicLayerWrapper.createEmployee(temp)
            print("You have successfully created the employee")

    def overWriteManager(self, temp, userInput_previous) -> True:
        """ Returns True if user decides to overwrite manager and False otherwise"""
        while True:
            self.Displays.overWriteManager()
            userInput = input("Choice: ")
            if userInput.lower() == "q":
                print("Quitting")
                return "q"
            elif userInput == "1":
                self.LogicLayerWrapper.exchangeManagersAtLocation(userInput_previous, temp)
                return True
            elif userInput == "2" or userInput == "b": # Aborting here and pressing b would do essentially the same thing, you are going back and aborting it. even if you press b we want to tell the user that he aborted the process
                print("Aborting the creation of a new Manager")
                return False
            else:
                print("Invalid Input")

    def createProperty(self):

        count = 1
        tempProperty = self.LogicLayerWrapper.createTempProperty()
        error_message = None
        title_message = "Adding a new Property"
        input_message = ["Enter Name: ", "Enter Location: ", "Enter Availability: ", "Enter Pool: ", "Enter Hot Tub: ", "Enter Ovens: "]
        while count < 7:
            self.ViewingUI.clearTerminal()
            self.Displays.printProperty(tempProperty, title_message, error_message, mode = "hints")
            userInput = input(f"{input_message[count-1]}")
            if userInput.lower() == "q":
                print("Quitting")
                return "q"

            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"

            try:
                if self.LogicLayerWrapper.validatePropertyInput(userInput, count, tempProperty):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        self.ViewingUI.clearTerminal()
        self.Displays.printProperty(tempProperty,title_message, error_message, mode = "hints")
        self.LogicLayerWrapper.createProperty(tempProperty)
        print("You have successfully created a new Property")

    def createMaintenanceTask(self):
        count = 1
        tempMaintenanceTask = self.LogicLayerWrapper.createTempMaintenance()
        error_message = None
        title_message = "Adding a new Maintenance Task"
        input_message = ["Enter Property Number: ", "Enter Description of Task: ", "Enter Start Date: ", "Enter End Date: ", "Enter Status Of Maintenance: ", "Enter Priority: ", "Enter Recurring: "]
        while count < 8:
            self.ViewingUI.clearTerminal()
            self.Displays.printMaintenanceTask(tempMaintenanceTask, title_message, error_message, mode = "hints")
            userInput = input(f"{input_message[count-1]}")
            if userInput.lower() == "q":
                print("Quitting")
                return "q"

            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"

            try:
                if self.LogicLayerWrapper.validateMaintenanceTaskInput(userInput, count, tempMaintenanceTask):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        self.ViewingUI.clearTerminal()
        self.Displays.printMaintenanceTask(tempMaintenanceTask, title_message, error_message, mode = "hints")
        self.LogicLayerWrapper.createMaintenance(tempMaintenanceTask)
        print("You have successfully created a new Maintenance Task")

    def createMaintenanceSchedule(self):
        count = 1
        tempMaintenanceSchedule = self.LogicLayerWrapper.createTempMaintenanceSchedule()
        error_message = None
        title_message = "Adding a new Maintenance Schedule"
        input_message = ["Enter Maintenance Task Number: ", "Enter Type Of Maintenance Task: ", "Enter Frequency: ", "Enter Start Date: "]
        while count < 5:
            self.ViewingUI.clearTerminal()
            self.Displays.printMaintenanceSchedule(tempMaintenanceSchedule, title_message, error_message, mode = "hints")
            userInput = input(f"{input_message[count-1]}")
            if userInput.lower() == "q":
                print("Quitting")
                return "q"

            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"

            try:
                if self.LogicLayerWrapper.validateMaintenanceScheduleInput(userInput, count, tempMaintenanceSchedule):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
            except KeyError as error:
                error_message = error
                continue
        self.ViewingUI.clearTerminal()
        self.Displays.printMaintenanceSchedule(tempMaintenanceSchedule, title_message, error_message, mode = "hints")
        self.LogicLayerWrapper.createMaintenanceSchedule(tempMaintenanceSchedule)
        print("You have successfully created a new Maintenance Task")

    def editEmployee(self, ID):
        done_message = "D: To Quit Changing and Save Changes\n"
        edit_message = "You can not change Employees ID, Social Security or Type"
        title_message = "Updating Employee Information"
        while True:
            try:
                employee = self.LogicLayerWrapper.getEmployeebyID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Employee you want to edit: ")
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    print("Going back")
                    self.ViewingUI.clearTerminal()
                    return "b"


        error_message = None
        while True:
            self.Displays.printEmployee(employee, title_message, error_message, edit_message, done_message)
            userInput = input("Number of the attribute you want to change: ")
            
            if userInput.lower() == "q":
                return "q"
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput in ["1", "3", "4", "5", "6", "7"]:

                newParam = input("New Information: ").strip()
                try:
                    self.LogicLayerWrapper.validateEmployeeInput(newParam, userInput, employee)
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice"

        if userInput.lower() == "d":
            self.LogicLayerWrapper.update_employee_data(employee)

    def editContractor(self, ID):
        done_message = "D: To Quit Changing and Save Changes\n"
        edit_message = "You can not change Contractors ID, Social Security or Type"
        title_message = "Updating Contractor Information"
        while True:
            try:
                employee = self.LogicLayerWrapper.getContractorbyID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Contractor you want to edit: ")
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    print("Going back")
                    self.ViewingUI.clearTerminal()
                    return "b"

        error_message = None
        while True:
            self.Displays.printEmployee(employee, title_message, error_message, edit_message, done_message)
            userInput = input("Number of the attribute you want to change: ")

            if userInput.lower() == "q":
                return "q"
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput in ["1", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:

                newParam = input("New Information: ").strip()
                try:
                    self.LogicLayerWrapper.validateEmployeeInput(newParam, userInput, employee)
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"

        if userInput.lower() == "d":
            self.LogicLayerWrapper.update_employee_data(employee)

    def editProperty(self, ID):
        done_message = "D: To Quit Changing and Save Changes\n"
        title_message = "Updating Property Information"
        while True:
            try:
                property = self.LogicLayerWrapper.getPropertyByID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Property you want to edit: ")
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    print("Going back")
                    self.ViewingUI.clearTerminal()
                    return "b"

        error_message = None
        while True:
            self.Displays.printProperty(property, title_message, error_message, done_message=done_message)
            userInput = input("Number of the attribute you want to change: ")

            if userInput.lower() == "q":
                return "q"
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput in ["1", "3", "4", "5", "6"]:

                newParam = input("New Information: ").strip()
                try:
                    self.LogicLayerWrapper.validatePropertyInput(newParam, userInput, property)
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"

        if userInput.lower() == "d":
            self.LogicLayerWrapper.updateProperty(property)

    def editMaintenanceTask(self, ID):
        done_message = "D: To Quit Changing and Save Changes\n"
        edit_message = "You can not change the Number, Maintenance done on Property, Start- or EndDate, Status or if its recurring or not"
        title_message = "Updating Maintenance Task Information"
        while True:
            try:
                maintenanceTask = self.LogicLayerWrapper.getMaintenanceTaskByID(ID)
                self.LogicLayerWrapper.canEditMaintenanceTask(maintenanceTask)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Maintenance Task you want to edit: ")
                if ID.lower() == "q":
                    return "q"
                elif ID.lower() == "b":
                    print("Going back")
                    self.ViewingUI.clearTerminal()
                    return "b"
                
        error_message = None
        while True:
            self.Displays.printMaintenanceTask(maintenanceTask, title_message, error_message, edit_message, done_message)
            userInput = input("Number of the attribute you want to change: ")

            if userInput.lower() == "q":
                return "q"
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput in ["2", "6"]:

                newParam = input("New Information: ").strip()
                try:
                    self.LogicLayerWrapper.validateMaintenanceTaskInput(newParam, userInput, maintenanceTask)
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"

        if userInput.lower() == "d":
            self.LogicLayerWrapper.updateMaintenance(maintenanceTask)

    def editMaintenanceSchedule(self, ID):
        done_message = "D: To Quit Changing and Save Changes\n"
        edit_message = "You can not change Schedule Number, Scheduled Task, Type of Maintenance Task or the Start Date"
        title_message = "Updating Maintenance Schedule Information"
        while True:
            try:
                maintenanceSchedule = self.LogicLayerWrapper.getMaintenanceScheduleByID(ID)
                self.LogicLayerWrapper.canEditMaintenanceSchedule(maintenanceSchedule)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Maintenance Schedule you want to edit: ")
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    print("Going back")
                    self.ViewingUI.clearTerminal()
                    return "b"
                
        error_message = None
        while True:
            self.Displays.printMaintenanceSchedule(maintenanceSchedule, title_message, error_message, edit_message, done_message)
            userInput = input("Number of the attribute you want to change: ")

            if userInput.lower() == "q":
                return "q"
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput == "3":

                newParam = input("New Information: ").strip()
                try:
                    self.LogicLayerWrapper.validateMaintenanceScheduleInput(newParam, userInput, maintenanceSchedule)
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"

        if userInput.lower() == "d":
            self.LogicLayerWrapper.updateMaintenanceSchedule(maintenanceSchedule)