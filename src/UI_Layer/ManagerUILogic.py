from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .ViewUILogic import ViewUILogic
from .Displays import Displays

class ManagerUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.ViewingUI = ViewUILogic()
        self.Displays = Displays()

    def run(self):
        self.ViewingUI.clearTerminal()
        while True:
            print("-------------------------Manager----------------------------")
            print("1: To create new Properties, Employees or Maintenance Tasks")
            print("2: To edit existent Properties, Employees or Maintenance Tasks")
            print("3: To view existent Properties, Employess or Maintenance Tasks")
            print("B: To Go Back")
            print("Q: To Quit")
            print("------------------------------------------------------------")
            user_choice = input("Choice: ")

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

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

    def addMenu(self):
        self.ViewingUI.clearTerminal()
        while True:
            print("1: To create a new General Employee")
            print("2: To create a new Manager")
            print("3: To create a new Contractor")
            print("4: To create a new Property")
            print("5: To create a new Maintenance Task")
            print("6: To create a new Maintenance Schedule")
            print("B: To Go Back")
            print("Q: To Quit\n")
            user_choice = input("Choice: ")

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

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
            print("1: To edit an Employee or a Manager")
            print("2: To edit a Contractor")
            print("3: To edit a Property")
            print("4: To edit a Maintenance Task")
            print("5: To edit a Maintenance Schedule")
            print("6: To close a Maintenance Task")
            print("B: To Go Back")
            print("Q: To Quit\n")
            user_choice = input("Choice: ")

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            if user_choice.lower() == "b":
                print("Going back")
                self.ViewingUI.clearTerminal()
                break

            if user_choice == "1":
                ID = input("ID of the Employee you want to edit: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()
                    continue

                self.editEmployee(ID) # komið
            elif user_choice == "2":
                ID = input("ID of the Contractor you want to edit: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()
                    continue

                self.editContractor(ID) # komið
            elif user_choice == "3":
                ID = input("ID of the Property you want to edit: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()
                    continue

                self.editProperty(ID) # komið
            elif user_choice == "4":
                ID = input("ID of the Maintenance Task you want to edit: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()
                    continue

                self.editMaintenanceTask(ID)
            elif user_choice == "5":
                ID = input("ID of the Maintenance Schedule you to edit: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()

                    continue
                self.editMaintenanceSchedule(ID)
            elif user_choice == "6":
                ID = input("ID of the Maintenance Task you to close: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.ViewingUI.clearTerminal()
                    continue

                try:
                    user_feedback = input("Feedback on the Task you want to close: ") 
                    self.LogicLayerWrapper.closeMaintenanceTask(ID, user_feedback)
                except ValueError as error:
                    print(error)

                except KeyError as error:
                    print(error)
                    continue
            else:
                print("Invalid Input")

    
    def createEmployee(self,type_of_employee):

        # Type of employee should be "1" for Employee, "2" for Manager, "3" for Contractor 
        count = 1
        temp = self.LogicLayerWrapper.getTempEmployee(type_of_employee)
        error_message = None
        overWritten = False
        aborted = False # Flag to see if user has pressed b or does not want to overwrite manager
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
                aborted = True
                self.ViewingUI.clearTerminal()
                break

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
                if not overWritten: # If we aborted creating the new manager then we break
                    aborted = True
                    break
            

        if not aborted:
            self.Displays.display_temp_employee(temp, error_message)
            self.LogicLayerWrapper.createEmployee(temp)
            print("You have successfully created the employee")

    def overWriteManager(self, temp, userInput_previous) -> True:
        """ Returns True if user decides to overwrite manager and False otherwise"""
        while True:
            self.Displays.overWriteManager()
            userInput = input("Choice: ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput == "1":
                self.LogicLayerWrapper.exchangeManagersAtLocation(userInput_previous, temp)
                return True
            elif userInput == "2":
                print("Aborting the creation of a new Manager")
                return False
            else:
                print("Invalid Input")

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
        while count < 8:
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
        while count < 5:
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
        while True:
            try:
                maintenanceTask = self.LogicLayerWrapper.getMaintenanceTaskByID(ID)
                self.LogicLayerWrapper.canEditMaintenanceTask(maintenanceTask)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Maintenance Task to edit: ")
                continue
                
        error_message = None
        while True:
            self.Displays.editMaintenanceTaskMenu(maintenanceTask, error_message)
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
        if userInput.lower() != "b":
            self.LogicLayerWrapper.updateMaintenance(maintenanceTask)

    def editMaintenanceSchedule(self, ID):
        while True:
            try:
                maintenanceSchedule = self.LogicLayerWrapper.getMaintenanceScheduleByID(ID)
                self.LogicLayerWrapper.canEditMaintenanceSchedule(maintenanceSchedule)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Maintenance Schedule to edit: ")
                continue
                
        error_message = None
        while True:
            self.Displays.editMaintenanceScheduleMenu(maintenanceSchedule, error_message)
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
        if userInput.lower() != "b":
            self.LogicLayerWrapper.updateMaintenanceSchedule(maintenanceSchedule)

        

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