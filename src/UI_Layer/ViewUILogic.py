# View UI Logic
from os import system, name
from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .Displays import Displays
from prettytable import PrettyTable

class ViewUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.Displays = Displays()

    def viewMenu(self):
        self.clearTerminal()
        while True:
            print("1: To view all Employees")
            print("2: To view all Contractors")
            print("3: To view all Properties")
            print("4: To view all Maintenance Tasks")
            print("5: To view all Scheduled Maintenance Tasks")
            print("6: To view all Maintenance Reports")
            print("7: To view all Destinations")
            print("B: To Go Back")
            print("Q: To Quit\n")
            user_choice = input("Choice: ")

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break

            elif user_choice == "1":
                self.displayEmployeesPretty() # Show them the complete list and then ask if they want any more filtering....
                self.filterEmployees()
            elif user_choice == "2":
                self.displayContractors() # Show them the complete list and then ask if they want any more fliltering...
                self.filterContractors()
            elif user_choice == "3":
                self.displayProperties() # Show them the complete list and then ask if they want any more filtering....
                self.filterProperties()
            elif user_choice == "4":
                self.displayMaintenanceTasks() #Show them the complete list and then ask if they want any more filtering....
                self.filterMaintenanceTasks()
            elif user_choice == "5":
                self.displayMaintenanceSchedules() # Show them the complete list and then ask if they want any more filtering....
                self.filterMaintenanceSchedules()
            elif user_choice == "6":
                self.displayMaintenanceReports()
                self.filterMaintenanceReports()
            elif user_choice == "7":
                self.displayDestinations()
                self.filterDestinations()
            else:
                print("Invalid Input")
            
    def clearTerminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def displayEmployeesPretty(self):
        employeespretty = PrettyTable()
        employeespretty.field_names = ["Employee Number", "Employee Name", "Social Security Number", "Address", "Home Phone", "GSM Phone","Email", "Working at destination", "Type of Employee"]
        employees = self.LogicLayerWrapper.getEmployeeData()
        for employee in employees:
            self.Displays.printEmployeePretty(employee, employeespretty)
        employeespretty.right_padding_width = 1
        employeespretty.align = 'l'
        print(employeespretty)

    def displayEmployees(self):
        employees = self.LogicLayerWrapper.getEmployeeData()
        for employee in employees:
            self.Displays.printEmployee(employee)

    def displayContractors(self):
        contractors = self.LogicLayerWrapper.getContractorData()
        for contractor in contractors:
            self.Displays.printContractor(contractor)

    def displayProperties(self):
        properties = self.LogicLayerWrapper.getPropertyData()
        for property in properties:
            self.Displays.printProperty(property)

    def displayMaintenanceTasks(self):
        maintenanceTasks = self.LogicLayerWrapper.getMaintenanceTaskData()
        for task in maintenanceTasks:
            self.Displays.printMaintenanceTask(task)

    def displayMaintenanceSchedules(self):
        maintenanceSchedules = self.LogicLayerWrapper.getMaintenanceScheduleData()
        for schedule in maintenanceSchedules:
            self.Displays.printMaintenanceSchedule(schedule)

    def displayMaintenanceReports(self):
        maintenanceReports = self.LogicLayerWrapper.getMaintenanceReportData()
        for report in maintenanceReports:
            self.Displays.printMaintenanceReport(report)

    def displayDestinations(self):
        destinations = self.LogicLayerWrapper.getDestinationData()
        for destination in destinations:
            self.Displays.printDestination(destination)

    def filterEmployees(self):
        while True:
            print("\n-------------------------------------------------------")
            print("1: To view additional information of a specific Employee")
            print("2: To view all tasks an Employee has worked on")
            print("B: To Go Back")
            print("Q: To Quit")
            print("-------------------------------------------------------\n")
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break

            elif user_choice == "1":
                ID = input("ID of the Employee you want to look up: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    employee = self.LogicLayerWrapper.getEmployeebyID(ID)
                    self.Displays.printEmployee(employee)
                except ValueError as error:
                    print(error)

            elif user_choice == "2":
                ID = input("ID of the Employee you want to show tasks for: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    tasks = self.LogicLayerWrapper.getTasksForEmployeeID(ID) # Takes in x amount of Maintenance Tasks an employee has worked
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")

    def filterContractors(self):
        while True:
            print("\n-------------------------------------------------------")
            print("1: To view additional information of a specific Contractor")
            print("2: To view all tasks a Contractor has worked on")
            print("B: To Go Back")
            print("Q: To Quit")
            print("-------------------------------------------------------\n")
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            
            elif user_choice == "1":
                ID = input("ID of the Contractor you want to look up: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    contractor = self.LogicLayerWrapper.getContractorbyID(ID)
                    self.Displays.printContractor(contractor)
                except ValueError as error:
                    print(error)
            elif user_choice == "2":
                ID = input("ID of the Contractor you want to show tasks for: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    tasks = self.LogicLayerWrapper.getTasksForContractorID(ID)# Takes in x amount of Maintenance Tasks a contractor has worked 
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")

    def filterProperties(self):
        while True:
            print("\n-------------------------------------------------------")
            print("1: To view additional information of a specific Property")
            print("2: To view all Maintenance on a specific Property")
            print("B: To Go Back")
            print("Q: To Quit")
            print("-------------------------------------------------------\n")
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            
            elif user_choice == "1":
                ID = input("ID of the Property you want to look up: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    property = self.LogicLayerWrapper.getPropertyByID(ID)
                    self.Displays.printProperty(property)
                except ValueError as error:
                    print(error)
            elif user_choice == "2":
                ID = input("ID of the Property you want to show tasks for: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    tasks = self.LogicLayerWrapper.getTasksForPropertyID(ID) # Takes in x amount of Maintenance Tasks done on specific property
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")
    
    def filterMaintenanceTasks(self):
        while True:
            print("\n-------------------------------------------------------")
            print("B: To Go Back")
            print("Q: To Quit")
            print("-------------------------------------------------------\n")
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            
            elif user_choice == "1":
                ID = input("ID of the Maintenance Task you want to look up: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    task = self.LogicLayerWrapper.getMaintenanceTaskByID(ID)
                    self.Displays.printMaintenanceTask(task)
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")

    def filterMaintenanceSchedules(self):
        while True:
            print("\n-------------------------------------------------------")
            print("1: To view additional information of a specific MaintenanceSchedule") ## IS THIS NEEDED ?
            print("B: To Go Back")
            print("Q: To Quit")
            print("-------------------------------------------------------\n")
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            
            elif user_choice == "1":
                ID = input("ID of the Maintenance Schedule you want to look up: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    task = self.LogicLayerWrapper.getMaintenanceScheduleByID(ID)
                    self.Displays.printMaintenanceSchedule(task)
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")            

    def filterMaintenanceReports(self):
        while True:
            print("\n-------------------------------------------------------")
            print("1: To view additional information of a specific MaintenanceReport")
            print("B: To Go Back")
            print("Q: To Quit")
            print("-------------------------------------------------------\n")
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            
            elif user_choice == "1":
                ID = input("ID of the Maintenance Report you want to look up: ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    report = self.LogicLayerWrapper.getMaintenanceReportByID(ID)
                    self.Displays.printMaintenanceReport(report)
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")

    def filterDestinations(self):
        while True:
            print("\n-------------------------------------------------------")
            print("1: To view information about Employees at a specific Destination")
            print("2: To view information about Contractors at a specific Destination")
            print("3: To view information about Properties at a specific Destination")
            print("B: To Go Back")
            print("Q: To Quit")
            print("-------------------------------------------------------\n")
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            
            elif user_choice == "1": 
                ID = input("ID of the Destination you want to show Employee information for ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID)
                    print("Nothing more implemented here go back")
                    # Try giving Display employees a list of employees on that location ? then call the filter employees ?
                except ValueError as error:
                    print(error)
            elif user_choice == "2":
                ID = input("ID of the Destination you want to show Contractor information for ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID)
                    print("Nothing more implemented here go back")
                    # Try giving Display Contractor a list of contractors on that location ? then call the filter contractors ?
                except ValueError as error:
                    print(error)
            elif user_choice == "3":
                ID = input("ID of the Destination you want to show Property information for ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID)
                    print("Nothing more implemented here go back")
                    # Try giving Display properties a list of properties on that location ? then call the filter properties ?
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")

    
    def dateFilter(self, tasks):
        while True:
            print("\n-------------------------------------------------------")
            print("1: To view tasks over a specific time period")
            print("B: To Go Back")
            print("Q: To Quit")
            print("-------------------------------------------------------\n")
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break

            elif user_choice == "1":
                startDate = input("Start Date: ")
                endDate = input("End Date: ")
                filtered_tasks = self.LogicLayerWrapper.filterMaintenanceTasksDates(tasks, startDate, endDate)
                for filtered_task in filtered_tasks:
                    self.Displays.printMaintenanceTask(filtered_task)
            else:
                print("Invalid Input")