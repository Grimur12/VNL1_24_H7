from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .ViewUILogic import ViewUILogic
from .Displays import Displays
from prettytable import PrettyTable
# Manager UI Logic class handles all inputs for the manager position
class ManagerUILogic:
    def __init__(self) -> None:
        """ Holds the logic layer wrapper, viewlogic and displays, classes we need to fulfill the user requirements"""
        self.LogicLayerWrapper = LogicLayerAPI()
        self.ViewingUI = ViewUILogic()
        self.Displays = Displays()

    def run(self) -> None:
        """ Function is responsible for running the main manager menu, which ties all the other manager available menus together"""
        error_message = None
        while True:
            self.ViewingUI.clearTerminal()
            print(self.Displays.ManagerMainMenu()) # Show the user his inital options as a manager
            if error_message: # Error message logic here enables us to clear the screen to keep the UI clear but still display the error message that the user encountered
                print(f"Error: {error_message}")
                error_message = None
            user_choice = input("Choice: ")

            if user_choice.lower() == "q": # Check if the user wants to quit
                print("Qutting")
                return "q" # Pass Q back into the main screen for it to quit the program

            if user_choice.lower() == "b": # Check if the user wants to go back to the main menu, to then choose another UI
                print("Going back")
                return "b"

            if user_choice == "1": # User wants to create something
                result = self.addMenu()
                if result == "q":
                    return "q"
            elif user_choice == "2":
                result = self.editMenu() # User wants to edit something
                if result == "q":
                    return "q"
            elif user_choice == "3":
                result = self.ViewingUI.viewMenu() # User wants to access the viewing features so we call the ViewingUI() which handles all of that
                if result == "q":
                    return "q"
            else:
                error_message = "Invalid Input"
                self.ViewingUI.clearTerminal()

    def addMenu(self) -> None:
        """ Function is responsible for handling all user input for creating in the system, returns str (q or b) for quit and back logic"""
        self.ViewingUI.clearTerminal()
        error_message = None
        while True:
            print(self.Displays.ManagerAddMenu()) # Display users inital options when creating something
            if error_message: # Error message logic here enables us to clear the screen to keep the UI clear but still display the error message that the user encountered
                print(f"Error: {error_message}")
                error_message = None
            # Handle initial quit and back logic
            user_choice = input("Choice: ")

            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                print("Going back")
                return "b"
            
            if user_choice in ["1", "2", "3"]: # User wants to create an employee calls for that menu
                result = self.createEmployee(user_choice)
                if result == "q":
                    return "q"
            elif user_choice == "4": # User wants to create a property, calls for that menu
                result = self.createProperty()
                if result == "q":
                    return "q" 
            elif user_choice == "5": # User wants to create a maintenance task, calls for that menu
                result = self.createMaintenanceTask()
                if result == "q":
                    return "q"
            elif user_choice == "6": # User wants to create a maintenance schedule, calls for that menu
                result = self.createMaintenanceSchedule()
                if result == "q":
                    return "q"
                # Nothing more to create here since the manager is not responsible for creating maintenance reports
            else:
                error_message = "Invalid Input"
                self.ViewingUI.clearTerminal()

    def editMenu(self) -> None:
        """Function handles all user inputs regarding editing in the system, returns str (q or b) for quit and back logic"""
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
                except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                    error_message = error
                    self.ViewingUI.clearTerminal()
                except KeyError as error: # KeyErrors may arrive from editing or closing so we display that aswell
                    error_message = error
                    self.ViewingUI.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.ViewingUI.clearTerminal()

    
    def createEmployee(self,type_of_employee) -> None:
        """ Function handles the user input for creating an employee, returns str (q or b) for quit and back logic"""
        # Type of employee should be "1" for Employee, "2" for Manager, "3" for Contractor 
        count = 1
        temp = self.LogicLayerWrapper.getTempEmployee(type_of_employee) # We get the temp employee from the logic layer to show the user 
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
            # We are creating so we pass the print function the relevant things it needs to show the user, like hints and error messages
            self.Displays.printEmployee(temp, title_message[int(type_of_employee)-1], error_message, mode="hints") # The type of employee decides what the title message is, we reference it on the type of employee by indexing it through that in the list of possible titles
            userInput = input(f"{input_message[count-1]}") # See the list of input messages, we keep track of what the user is inputing through count, so we reference the relevant enter message through that
            if userInput.lower() == "q":
                print("Quitting")
                return "q"

            elif userInput.lower() == "b":
                print("Going back")
                aborted = True
                self.ViewingUI.clearTerminal()
                return "b"

            try:
                if self.LogicLayerWrapper.validateEmployeeInput(userInput, count, temp): # We need the logic layer to validate the user input, give them the count to know which one he is inputting, the input and the employee he is creating for the logic layer to make changes
                    count +=1
                    error_message = None
            except ValueError as error:  # If the inputs are wrong when we may get ValueErrors so we display them to the user
                error_message = error
                continue
            except KeyError:
                overWritten = self.overWriteManager(temp, userInput) # If the user is creating a manager and it exists he needs to decide whether he wants to abort or demote him, give him those options
                count += 1
                if overWritten == "q":
                    return "q"
                elif not overWritten: # If we aborted creating the new manager then we break
                    aborted = True
                    break
            
        if not aborted:
            self.ViewingUI.clearTerminal()
            self.Displays.printEmployee(temp, title_message[int(type_of_employee)-1], error_message) # Final display of the employee he created
            self.LogicLayerWrapper.createEmployee(temp)
            print("You have successfully created the employee")

    def overWriteManager(self, temp, userInput_previous) -> True:
        """ Returns True if user decides to overwrite manager and False otherwise"""
        error_message = None
        while True:
            self.ViewingUI.clearTerminal()
            self.Displays.overWriteManager(error_message) # Show the user the options he has for demoteding/aborting
            userInput = input("Choice: ")
            if userInput.lower() == "q":
                print("Quitting")
                return "q"
            elif userInput == "1":
                self.LogicLayerWrapper.exchangeManagersAtLocation(userInput_previous, temp) # If he chooses to overwrite we tell the logic layer to change it
                return True # Just so we can tell the createemployee user input handling what the user did
            elif userInput == "2" or userInput == "b": # Aborting here and pressing b would do essentially the same thing, you are going back and aborting it. even if you press b we want to tell the user that he aborted the process
                print("Aborting the creation of a new Manager")
                return False # Just so we can tell the createemployee user input handling what the user did
            else:
                error_message = "Invalid Input"

    def createProperty(self) -> None:
        """ Function handles the user input for creating an properties, returns str (q or b) for quit and back logic """
        count = 1
        tempProperty = self.LogicLayerWrapper.createTempProperty()
        error_message = None
        title_message = "Adding a new Property"
        input_message = ["Enter Name: ", "Enter Location: ", "Enter Availability: ", "Enter Pool: ", "Enter Hot Tub: ", "Enter Ovens: "]
        while count < 7:
            self.ViewingUI.clearTerminal()
            self.Displays.printProperty(tempProperty, title_message, error_message, mode = "hints")
            userInput = input(f"{input_message[count-1]}") # See the list of input messages, we keep track of what the user is inputing through count, so we reference the relevant enter message through that
            if userInput.lower() == "q":
                print("Quitting")
                return "q"

            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"

            try:
                if self.LogicLayerWrapper.validatePropertyInput(userInput, count, tempProperty):  # We need the logic layer to validate the user input, give them the count to know which one he is inputting, the input and the property he is creating for the logic layer to make changes
                    count +=1
                    error_message = None
            except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                error_message = error
                continue
        self.ViewingUI.clearTerminal()
        self.Displays.printProperty(tempProperty,title_message, error_message) # Show the user the property he just created
        self.LogicLayerWrapper.createProperty(tempProperty)
        print("You have successfully created a new Property")

    def createMaintenanceTask(self) -> None:
        """ Function handles the user input for creating a maintenance task, returns str (q or b) for quit and back logic"""
        count = 1
        tempMaintenanceTask = self.LogicLayerWrapper.createTempMaintenance()
        error_message = None
        title_message = "Adding a new Maintenance Task"
        input_message = ["Enter Property Number: ", "Enter Description of Task: ", "Enter Start Date: ", "Enter End Date: ", "Enter Status Of Maintenance: ", "Enter Priority: ", "Enter Recurring: "]
        while count < 8:
            self.ViewingUI.clearTerminal()
            self.Displays.printMaintenanceTask(tempMaintenanceTask, title_message, error_message, mode = "hints")
            userInput = input(f"{input_message[count-1]}") # See the list of input messages, we keep track of what the user is inputing through count, so we reference the relevant enter message through that
            if userInput.lower() == "q":
                print("Quitting")
                return "q"

            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"

            try:
                if self.LogicLayerWrapper.validateMaintenanceTaskInput(userInput, count, tempMaintenanceTask):  # We need the logic layer to validate the user input, give them the count to know which one he is inputting, the input and the maintenance task he is creating for the logic layer to make changes
                    count +=1
                    error_message = None
            except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                error_message = error
                continue
        self.ViewingUI.clearTerminal()
        self.Displays.printMaintenanceTask(tempMaintenanceTask, title_message, error_message) # Show the property the user created to him
        self.LogicLayerWrapper.createMaintenance(tempMaintenanceTask)
        print("You have successfully created a new Maintenance Task")

    def createMaintenanceSchedule(self) -> None:
        """ Function handles the user input for creating a maintenance schedule, returns str (q or b) for quit and back logic"""
        count = 1
        tempMaintenanceSchedule = self.LogicLayerWrapper.createTempMaintenanceSchedule()
        error_message = None
        title_message = "Adding a new Maintenance Schedule"
        input_message = ["Enter Maintenance Task Number: ", "Enter Type Of Maintenance Task: ", "Enter Frequency: ", "Enter Start Date: "]
        while count < 5:
            self.ViewingUI.clearTerminal()
            self.Displays.printMaintenanceSchedule(tempMaintenanceSchedule, title_message, error_message, mode = "hints")
            userInput = input(f"{input_message[count-1]}") # See the list of input messages, we keep track of what the user is inputing through count, so we reference the relevant enter message through that
            if userInput.lower() == "q":
                print("Quitting")
                return "q"

            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"

            try:
                if self.LogicLayerWrapper.validateMaintenanceScheduleInput(userInput, count, tempMaintenanceSchedule):  # We need the logic layer to validate the user input, give them the count to know which one he is inputting, the input and the maintenance schedule he is creating for the logic layer to make changes
                    count +=1
                    error_message = None
            except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                error_message = error
                continue
            except KeyError as error:
                error_message = error
                continue
        self.ViewingUI.clearTerminal()
        self.Displays.printMaintenanceSchedule(tempMaintenanceSchedule, title_message, error_message)
        self.LogicLayerWrapper.createMaintenanceSchedule(tempMaintenanceSchedule)
        print("You have successfully created a new Maintenance Task")

    def editEmployee(self, ID) -> None:
        """ Function handles the user input for editing an employee, returns str (q or b) for quit and back logic"""
        done_message = "D: To Quit Changing and Save Changes\n"
        edit_message = "You can not change Employees ID, Social Security or Type"
        title_message = "Updating Employee Information"
        while True:
            try:
                employee = self.LogicLayerWrapper.getEmployeebyID(ID) # Try to get the Employee the user specified
                break
                
            except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                print(f"Error: {error}")
                ID = input("ID of the Employee you want to edit: ") # We need the ID of the object the user wants to edit so we can ask the logic layer for it to show the user what his options are
                # Need handling for if user wants to quit or go back
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    print("Going back")
                    self.ViewingUI.clearTerminal()
                    return "b"
        # Once we have the specified employee from the logic layer we can start getting the user input to change the things he wants to change
        error_message = None
        while True:
            self.Displays.printEmployee(employee, title_message, error_message, edit_message, done_message) # Initially print the employee so the user can see what he wants to change
            userInput = input("Number of the attribute you want to change: ")
            # Need handling for if user wants to quit or go back
            if userInput.lower() == "q":
                return "q"
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput in ["1", "3", "4", "5", "6", "7"]: # The attribute numbers that the user can choose to change, keep track of them

                newParam = input("New Information: ").strip()
                try:
                    self.LogicLayerWrapper.validateEmployeeInput(newParam, userInput, employee) # And then tell the logic layer to make relevant changes based on the user input
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice"

        if userInput.lower() == "d":
            self.LogicLayerWrapper.update_employee_data(employee)

    def editContractor(self, ID) -> None:
        """ Function handles the user input for editing a contractor, returns str (q or b) for quit and back logic"""
        done_message = "D: To Quit Changing and Save Changes\n"
        edit_message = "You can not change Contractors ID, Social Security or Type"
        title_message = "Updating Contractor Information"
        while True:
            try:
                employee = self.LogicLayerWrapper.getContractorbyID(ID) # Get the contractor specified by the user from the logic layer
                break
                
            except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                print(f"Error: {error}")
                ID = input("ID of the Contractor you want to edit: ") # We need the ID of the object the user wants to edit so we can ask the logic layer for it to show the user what his options are
                # Need handling for if user wants to quit or go back
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    print("Going back")
                    self.ViewingUI.clearTerminal()
                    return "b"
        # once we have the contractor the user specified from the logic layer we can start getting the user input to change the things he wants to change
        error_message = None
        while True:
            self.Displays.printEmployee(employee, title_message, error_message, edit_message, done_message)
            userInput = input("Number of the attribute you want to change: ")
            # Need handling for if user wants to quit or go back
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
                except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"

        if userInput.lower() == "d":
            self.LogicLayerWrapper.update_employee_data(employee)

    def editProperty(self, ID) -> None:
        """ Function handles the user input for editing a property, returns str (q or b) for quit and back logic"""
        done_message = "D: To Quit Changing and Save Changes\n"
        title_message = "Updating Property Information"
        while True:
            try:
                property = self.LogicLayerWrapper.getPropertyByID(ID) # Get the property specified by the user from the logic layer
                break
                
            except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                print(f"Error: {error}")
                ID = input("ID of the Property you want to edit: ") # We need the ID of the object the user wants to edit so we can ask the logic layer for it to show the user what his options are
                # Need handling for if user wants to quit or go back
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    print("Going back")
                    self.ViewingUI.clearTerminal()
                    return "b"
        # once we have the property the user specified from the logic layer we can start getting the user input to change the things he wants to change
        error_message = None
        while True:
            self.Displays.printProperty(property, title_message, error_message, done_message=done_message) # print the property for the user to see what he is changing and the numbers of the attributes
            userInput = input("Number of the attribute you want to change: ")
            # Need handling for if user wants to quit or go back
            if userInput.lower() == "q":
                return "q"
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput in ["1", "3", "4", "5", "6"]: # List of the available attributes the user could potentially edit

                newParam = input("New Information: ").strip()
                try:
                    self.LogicLayerWrapper.validatePropertyInput(newParam, userInput, property) # Ask the logic layer to make the relevant changes if they are valid 
                    error_message = None
                except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"

        if userInput.lower() == "d":
            self.LogicLayerWrapper.updateProperty(property)

    def editMaintenanceTask(self, ID) -> None:
        """ Function handles the user input for editing a maintenance task, returns str (q or b) for quit and back logic"""
        done_message = "D: To Quit Changing and Save Changes\n"
        edit_message = "You can not change the Number, Maintenance done on Property, Start- or EndDate, Status or if its recurring or not"
        title_message = "Updating Maintenance Task Information"
        while True:
            try:
                maintenanceTask = self.LogicLayerWrapper.getMaintenanceTaskByID(ID) # Get the maintenancetask specified by the user from the logic layer
                self.LogicLayerWrapper.canEditMaintenanceTask(maintenanceTask) # Ask the logic layer if he is allowed to edit the maintenance task
                break
                
            except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                print(f"Error: {error}")
                # Need handling for if user wants to quit or go back
                ID = input("ID of the Maintenance Task you want to edit: ") # We need the ID of the object the user wants to edit so we can ask the logic layer for it to show the user what his options are
                if ID.lower() == "q":
                    return "q"
                elif ID.lower() == "b":
                    print("Going back")
                    self.ViewingUI.clearTerminal()
                    return "b"
        # once we have the maintenance task the user specified from the logic layer we can start getting the user input to change the things he wants to change     
        error_message = None
        while True:
            self.Displays.printMaintenanceTask(maintenanceTask, title_message, error_message, edit_message, done_message) # print the maintenance task for the user to see what he is changing and the numbers of the attributes
            userInput = input("Number of the attribute you want to change: ")
            # Need handling for if user wants to quit or go back
            if userInput.lower() == "q":
                return "q"
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput in ["2", "6"]: # List of the available attributes the user could potentially edit

                newParam = input("New Information: ").strip()
                try:
                    self.LogicLayerWrapper.validateMaintenanceTaskInput(newParam, userInput, maintenanceTask) # Ask the logic layer to make the relevant changes if they are valid 
                    error_message = None
                except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"

        if userInput.lower() == "d":
            self.LogicLayerWrapper.updateMaintenance(maintenanceTask)

    def editMaintenanceSchedule(self, ID) -> None:
        """ Function handles the user input for editing a maintenance schedule, returns str (q or b) for quit and back logic"""
        done_message = "D: To Quit Changing and Save Changes\n"
        edit_message = "You can not change Schedule Number, Scheduled Task, Type of Maintenance Task or the Start Date"
        title_message = "Updating Maintenance Schedule Information"
        while True:
            try:
                maintenanceSchedule = self.LogicLayerWrapper.getMaintenanceScheduleByID(ID) # Get the maintenance schedule specified by the user from the logic layer
                self.LogicLayerWrapper.canEditMaintenanceSchedule(maintenanceSchedule) # Ask the logic layer if he is allowed to edit the maintenance schedule
                break
                
            except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                print(f"Error: {error}")
                # Need handling for if user wants to quit or go back
                ID = input("ID of the Maintenance Schedule you want to edit: ") # We need the ID of the object the user wants to edit so we can ask the logic layer for it to show the user what his options are
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    print("Going back")
                    self.ViewingUI.clearTerminal()
                    return "b"
        # once we have the maintenance schedule the user specified from the logic layer we can start getting the user input to change the things he wants to change    
        error_message = None
        while True:
            self.Displays.printMaintenanceSchedule(maintenanceSchedule, title_message, error_message, edit_message, done_message) # print the maintenance schedule for the user to see what he is changing and the numbers of the attributes
            userInput = input("Number of the attribute you want to change: ")
            # Need handling for if user wants to quit or go back
            if userInput.lower() == "q":
                return "q"
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                return "b"
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput == "3": # Possible attribute to change 

                newParam = input("New Information: ").strip()
                try:
                    self.LogicLayerWrapper.validateMaintenanceScheduleInput(newParam, userInput, maintenanceSchedule) # Ask the logic layer to make the relevant changes if they are valid 
                    error_message = None
                except ValueError as error: # If the inputs are wrong when we may get ValueErrors so we display them to the user
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"

        if userInput.lower() == "d":
            self.LogicLayerWrapper.updateMaintenanceSchedule(maintenanceSchedule)