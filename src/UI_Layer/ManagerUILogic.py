from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .ViewUILogic import ViewUILogic
from .Displays import Displays

# Class for Manager UI Logic where we have all of the communication with the manager to the UI

class ManagerUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.ViewingUI = ViewUILogic()
        self.Displays = Displays()

    def run(self):
        self.ViewingUI.clearTerminal()
        while True:
            # List of features the manager can choose to select/do
            print("1: Create new Properties, Employees or Maintenance Tasks")
            print("2: Edit existent Properties, Employees or Maintenance Tasks")
            print("3: View existent Properties, Employess or Maintenance Tasks")
            print("B: Go Back")
            print("Q: Quit\n")
            user_choice = input("Choice: ")

            # The user chooses to quit
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            # The user chooses to go back
            if user_choice.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                break

            if user_choice == "1":
                self.addMenu()
            elif user_choice == "2":
                self.editMenu()
            elif user_choice == "3":
                self.ViewingUI.viewMenu()
            else:
                print("Invalid Input")

    # Definition of the menu that comes when the user chooses to create (option1)
    def addMenu(self):
        self.ViewingUI.clearTerminal()
        while True:
            # Main menu of create employee, contractor, property
            print("1: Create a new General Employee")
            print("2: Create a new Manager")
            print("3: Create a new Contractor")
            print("4: Create a new Property")
            print("5: Create a new Maintenance Task")
            print("6: Create a new Maintenance Schedule")
            print("B: Go Back")
            print("Q: Quit\n")
            user_choice = input("Choice: ")

            #user chooses to quit
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            # user chooses to go back
            if user_choice.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                break

            if user_choice in ["1", "2", "3"]:
                self.createEmployee(user_choice) # komið
            elif user_choice == "4":
                self.createProperty() # komið
            elif user_choice == "5":
                self.createMaintenanceTask()
            elif user_choice == "6":
                self.createMaintenanceSchedule()
            else:
                print("Invalid Input")

    def editMenu(self):
        # Edit Employee
        # Edit Property
        # Edit Maintenance Task
        # Edit Maintenance Schedule
        self.ViewingUI.clearTerminal()
        while True:
            print("1: Edit an Employee or a Manager")
            print("2: Edit a Contractor")
            print("3: Edit a Property")
            print("4: Edit a Maintenance Task")
            print("5: Edit a Maintenance Schedule")
            print("B: Go Back")
            print("Q: Quit\n")
            user_choice = input("Choice: ")

            #user chooses to quit
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            # user chooses to go back
            if user_choice.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                break

            # the user chooses to edit an employee or manager
            if user_choice == "1":
                ID = input("ID of the Employee you want to edit: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()
                    continue

                self.editEmployee(ID) # komið

            # user chooses to edit contractor
            elif user_choice == "2":
                ID = input("ID of the Contractor you want to edit: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()
                    continue

                self.editContractor(ID) # komið

            # user chooses to edit Property
            elif user_choice == "3":
                ID = input("ID of the Property you want to edit: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()
                    continue

                self.editProperty(ID) # komið

            # user chooses to edit a maintenance task
            elif user_choice == "4":
                ID = input("ID of the Maintenance Task you want to edit: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()
                    continue

                self.editMaintenanceTask(ID)

            # user chooses to edit maintenance schedule
            elif user_choice == "5":
                ID = input("ID of the Maintenance Schedule you to edit: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()

                    continue
                self.editMaintenanceSchedule(ID)
            else:
                print("Invalid Input")

    # Definition of create employee
    def createEmployee(self,type_of_employee):

        # Type of employee should be "1" for Employee, "2" for Contractor 
        count = 1
        temp = self.LogicLayerWrapper.getTempEmployee(type_of_employee)
        error_message = None
        if type_of_employee == "3":
            max_parameters = 12
        else:
            max_parameters = 8
        while count < max_parameters:
            self.Displays.display_temp_employee(temp, error_message)
            userInput = input("Information: ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                break

            try:
                if self.LogicLayerWrapper.validateEmployeeInput(userInput, count, temp):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        if userInput.lower() != "b":
            self.Displays.display_temp_employee(temp, error_message)
            self.LogicLayerWrapper.createEmployee(temp)
            print("You have successfully created the employee")
            
    def createProperty(self):

        count = 1
        tempProperty = self.LogicLayerWrapper.createTempProperty()
        error_message = None
        while count < 7:
            self.Displays.display_temp_property(tempProperty, error_message)
            userInput = input("Information : ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput.lower() == "b":
                self.ViewingUI.clearTerminal()
                break

            try:
                if self.LogicLayerWrapper.validatePropertyInput(userInput, count, tempProperty):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        
        if userInput.lower() != "b":
            self.Displays.display_temp_property(tempProperty, error_message)
            self.LogicLayerWrapper.createProperty(tempProperty)
            print("You have successfully created a new Property")

    def createMaintenanceTask(self):
        
        count = 1
        tempMaintenanceTask = self.LogicLayerWrapper.createTempMaintenance()
        error_message = None
        while count < 7:
            self.Displays.display_temp_maintenanceTask(tempMaintenanceTask, error_message)
            userInput = input("Information: ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput.lower() == "b":
                self.ViewingUI.clearTerminal()
                break

            try:
                if self.LogicLayerWrapper.validateMaintenanceTaskInput(userInput, count, tempMaintenanceTask):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        if userInput.lower() != "b":
            self.Displays.display_temp_maintenanceTask(tempMaintenanceTask, error_message)
            self.LogicLayerWrapper.createMaintenance(tempMaintenanceTask)
            print("You have successfully created a new Maintenance Task")

    def createMaintenanceSchedule(self):
        count = 1
        tempMaintenanceSchedule = self.LogicLayerWrapper.createTempMaintenanceSchedule()
        error_message = None
        while count < 4:
            self.Displays.display_temp_maintenanceSchedule(tempMaintenanceSchedule, error_message)
            userInput = input("Information: ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput.lower() == "b":
                self.ViewingUI.clearTerminal()
                break

            try:
                if self.LogicLayerWrapper.validateMaintenanceScheduleInput(userInput, count, tempMaintenanceSchedule):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        if userInput.lower() != "b":
            self.Displays.display_temp_maintenanceSchedule(tempMaintenanceSchedule, error_message)
            self.LogicLayerWrapper.createMaintenanceSchedule(tempMaintenanceSchedule)
            print("You have successfully created a new Maintenance Task")

    def editEmployee(self, ID):
        while True:
            try:
                employee = self.LogicLayerWrapper.getEmployeebyID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Employee to edit: ")
                continue
        
        error_message = None
        while True:
            self.Displays.editEmployeeMenu(employee, error_message)
            userInput = input("Number of the attribute you want to change: ")
            
            if userInput.lower() == "q":
                exit() ## QUIT...
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                break ## Go back one
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
                error_message = "Not a Valid Choice, Try Again"
        if userInput.lower() != "b":
            self.LogicLayerWrapper.update_employee_data(employee)

    def editContractor(self, ID):
        while True:
            try:
                employee = self.LogicLayerWrapper.getContractorbyID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Employee to edit: ")
                continue

        error_message = None
        while True:
            self.Displays.editContractorMenu(employee, error_message)
            userInput = input("Number of the attribute you want to change: ")

            if userInput.lower() == "q":
                exit() ## QUIT...
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                break ## Go back one
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
        if userInput.lower() != "b":
            self.LogicLayerWrapper.update_employee_data(employee)

    def editProperty(self, ID):
        while True:
            try:
                property = self.LogicLayerWrapper.getPropertyByID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Property to edit: ")
                continue
        error_message = None
        while True:
            self.Displays.editPropertyMenu(property, error_message)
            userInput = input("Number of the attribute you want to change: ")

            if userInput.lower() == "q":
                exit() ## QUIT...
            elif userInput.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                break ## Go back one
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
        if userInput.lower() != "b":
            self.LogicLayerWrapper.updateProperty(property)

    def editMaintenanceTask(self, ID):
        pass

    def editMaintenanceSchedule(self, ID):
        pass

# Manager features
# Add employee
# View all employees
# View a single employee (more detail)
# Create a maintenance task
# Confirm or deny task and give feedback on task
# View Property
# View Location
# Add property
# Edit property

# 1: Add features
    # Add employee
    # Add property
    # Add Maintenance Task
    # Schedule Maintenance
# 2: Editing features
    # Edit Employee
    # Edit Property
    # Edit Maintenance Task
    # Edit Maintenance Schedule
# 3: Viewing features
    # View all employees
        # View specific employee By ID
        # View all tasks that an employee has worked on
    # View all properties
        # View specific property by ID
        # View all tasks that have been done on specific property
    # View all Maintenance Tasks
        # View specific Maintenance Task by ID
    # View all Scheduled Maintenanece Tasks