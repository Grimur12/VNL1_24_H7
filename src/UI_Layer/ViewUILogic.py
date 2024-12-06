# View UI Logic
from os import system, name
from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .Displays import Displays

class ViewUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.Displays = Displays()

    def viewMenu(self):
        self.clearTerminal
        while True:
            print("1: To view all Employees")
            print("2: To view all Properties")
            print("3: To view all Maintenance Tasks")
            print("4: To view all Scheduled Maintenance Tasks")
            user_choice = input("Choice: ")

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                break

            elif user_choice == "1":
                self.displayEmployees() # Show them the complete list and then ask if they want any more filtering....
                self.filterEmployees() 
            elif user_choice == "2":
                self.displayProperties() # Show them the complete list and then ask if they want any more filtering....
                self.filterProperties()
            elif user_choice == "3":
                self.displayMaintenanceTasks() #Show them the complete list and then ask if they want any more filtering....
                self.filterMaintenanceTasks()
            elif user_choice == "4":
                self.displayMaintenanceSchedules() # Show them the complete list and then ask if they want any more filtering....
                self.filterMaintenanceSchedules()
            else:
                print("Invalid Input")
            
    def clearTerminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def displayEmployees(self):
        employees = self.LogicLayerWrapper.getEmployeeData()
        for employee in employees:
            print(employee)

    def displayProperties(self):
        properties = self.LogicLayerWrapper.getPropertyData()
        for property in properties:
            self.Displays.printProperty(property)

    def displayMaintenanceTasks(self):
        pass # Same as displayProperties

    def displayMaintenanceSchedules(self):
        pass # Same as displayProperties

    def filterEmployees(self):
        print("1: To view additional information of a specific Employee")
        print("2: To view all tasks an employee has worked on") # ongoing and closed
        # SOME USER INPUT AND EXTRA LOGIC FOR THAT....

    def filterProperties(self):
        print("1: To view additional information of a specific Property")
        print("2: To view all Maintenance on a specific Property") # ongoing and closed
        
    def filterMaintenanceTasks(self):
        print("1: To view additional information of a specific MaintenanceTask") ## IS THIS NEEDED ?
        pass

    def filterMaintenanceSchedules(self):
        print("1: To view additional information of a specific MaintenanceSchedule") ## IS THIS NEEDED ?
        pass