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
            print(self.Displays.ViewMenu())
            user_choice = input("Choice: ")

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break

            elif user_choice == "1":
                self.filterEmployees()
            elif user_choice == "2":
                self.filterContractors()
            elif user_choice == "3":
                self.filterProperties()
            elif user_choice == "4":
                self.filterMaintenanceTasks()
            elif user_choice == "5":
                self.filterMaintenanceSchedules()
            elif user_choice == "6":
                self.filterMaintenanceReports()
            elif user_choice == "7":
                self.filterDestinations()
            else:
                print("Invalid Input")
            
    def clearTerminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def displayEmployees(self, destination = None):
        employeespretty = PrettyTable()
        employeespretty.field_names = ["Employee Number", "Employee Name", "Social Security Number", "Address", "Home Phone", "GSM Phone","Email", "Working at destination", "Type of Employee"]
        employees = self.LogicLayerWrapper.getEmployeeData(destination)
        for employee in employees:
            employeespretty.add_row([employee.employeeID, employee.name, employee.socialSecurity, employee.address ,employee.atHomePhone, employee.gsmPhone, employee.email, employee.workLocation , employee.type], divider=True)        
        employeespretty.align = 'l'
        employeespretty.max_table_width = 120
        employeespretty.min_table_width = 100
        employeespretty.max_width = 30 
        print(employeespretty)

    # def displayEmployees(self, destination = None):
    #     employees = self.LogicLayerWrapper.getEmployeeData(destination)
    #     for employee in employees:
    #         self.Displays.printEmployee(employee)

    # def displayContractors(self, destination = None):
    #     contractors = self.LogicLayerWrapper.getContractorData(destination)
    #     for contractor in contractors:
    #         self.Displays.printContractor(contractor)

    def displayContractors(self, destination=None):
        contractors_pretty = PrettyTable()
        contractors_pretty.field_names = ["Contractor Number", "Name", "Social Security", "Address", "Home Phone", "GSM Phone", "Email", "Work Location", "Type", "Previous Task", "Performance Rating", "Contractor Contact", "Opening Hours"]
        contractors = self.LogicLayerWrapper.getContractorData(destination)

        for contractor in contractors:
            contractors_pretty.add_row([contractor.employeeID, contractor.name, contractor.socialSecurity, contractor.address, contractor.atHomePhone, contractor.gsmPhone, contractor.email, contractor.workLocation, contractor.type, 
                                        contractor.previousTask if contractor.previousTask else "N/A", 
                                        contractor.performanceRating if contractor.performanceRating else "N/A", 
                                        contractor.contractorContact, contractor.openingHours])
        contractors_pretty.align = 'l'  
        contractors_pretty.max_table_width = 120  
        contractors_pretty.min_table_width = 100  
        contractors_pretty.max_width = 30  
        contractors_pretty.hrules = True 
        contractors_pretty.vrules = True  

        print(contractors_pretty)

    def displayProperties(self, destination = None):
        propertiespretty = PrettyTable()
        propertiespretty.field_names = ["Property Number", "Property Name", "Available for rental", "Pool Available", "Tub Available", "Ovens Available"]
        properties = self.LogicLayerWrapper.getPropertyData(destination)
        for property in properties:
            propertiespretty.add_row([property.propertyID,property.nameOfProperty,property.availability,property.hasAPool,property.hasATub,property.hasOvens])
        propertiespretty.align = 'l'
        propertiespretty.max_width = 30
        propertiespretty.max_table_width = 120  
        propertiespretty.min_table_width = 100  
        print(propertiespretty)

    def displayMaintenanceTasks(self):
        maintenanceTasks = self.LogicLayerWrapper.getMaintenanceTaskData()

        # Create a PrettyTable instance
        tasks_pretty = PrettyTable()
        tasks_pretty.field_names = ["Task ID", "Property ID", "Description", "Start Date", "End Date", "Status", "Priority", "Recurring"]

        # Add rows to the table
        for task in maintenanceTasks:
            tasks_pretty.add_row([task.maintenanceID,task.propertyID,task.description,task.startDate,task.endDate,task.statusMaintenance,task.priority,task.recurring])

        # Table formatting options
        tasks_pretty.align = "l"  
        tasks_pretty.max_width = 30  
        tasks_pretty.min_table_width = 100 
        tasks_pretty.max_table_width = 120  
        tasks_pretty.hrules = 1  

        # Display the table
        print(tasks_pretty)

    def displayMaintenanceSchedules(self):
        maintenanceSchedules = self.LogicLayerWrapper.getMaintenanceScheduleData()

        schedules_pretty = PrettyTable()
        schedules_pretty.field_names = ["Schedule ID", "Maintenance ID", "Task Type", "Frequency", "Start Date"]

        # Add rows to the table
        for schedule in maintenanceSchedules:
            schedules_pretty.add_row([ schedule.maintenanceScheduleID, schedule.maintenanceID, schedule.taskType, schedule.frequency, schedule.startDate])

        # Table formatting options
        schedules_pretty.align = "l"  
        schedules_pretty.max_width = 30  
        schedules_pretty.min_table_width = 100  
        schedules_pretty.max_table_width = 120 
        schedules_pretty.hrules = 1  

        # Display the table
        print(schedules_pretty)


    def displayMaintenanceReports(self):
        # Fetch maintenance report data
        maintenanceReports = self.LogicLayerWrapper.getMaintenanceReportData()

        # Create a PrettyTable instance
        maintenance_reports_pretty = PrettyTable()
        maintenance_reports_pretty.field_names = ["Report ID", "Maintenance ID", "Employee ID", "Material Cost", "Contractor ID", "Contractor Cost", "Ready to Close", "Supervisor Closed", "Supervisor Feedback"]

        # We need to change what the user sees based on whats inside the attribute
        for report in maintenanceReports:
            maintenance_reports_pretty.add_row([
            report.maintenanceReportID,
            report.maintenanceID,
            report.employeeID if report.employeeID else "N/A",
            report.materialCost,
            report.contractorID if report.contractorID else "N/A",
            report.contractorCost if report.contractorCost else "N/A",
            "Yes" if report.readyToClose else "No",
            "Yes" if report.supervisorClosed.lower() == "true" else "No",
            report.supervisorFeedback if report.supervisorFeedback else "No Feedback Yet"
            ])

        # Table formatting 
        maintenance_reports_pretty.align = "l"  
        maintenance_reports_pretty.max_width = 30 
        maintenance_reports_pretty.min_table_width = 100 
        maintenance_reports_pretty.max_table_width = 120 
        maintenance_reports_pretty.hrules = 1 

        print(maintenance_reports_pretty)

    def displayDestinations(self):
        destinations = self.LogicLayerWrapper.getDestinationData()

        destinations_pretty = PrettyTable()
        destinations_pretty.field_names = ["Destination ID", "Name", "Country", "Timezone", "Airport Name", "Phone Number", "Opening Hours", "Manager ID"]

        for destination in destinations:
            destinations_pretty.add_row([destination.destinationID, destination.name, destination.country, destination.timezone, destination.airportName, destination.phoneNumber, destination.openingHours, destination.managerOfDestination])

        destinations_pretty.align = "l" 
        destinations_pretty.max_width = 30 
        destinations_pretty.min_table_width = 100 
        destinations_pretty.max_table_width = 120 
        destinations_pretty.hrules = 1 

        print(destinations_pretty)

    def filterEmployees(self, destination = None):
        self.displayEmployees(destination) # Show them the complete list and then ask if they want any more filtering....
        # Function can receive a destination if user is asking for specific employees at a specific destination
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
                    employee = self.LogicLayerWrapper.getEmployeebyID(ID, destination)
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
                    tasks = self.LogicLayerWrapper.getTasksForEmployeeID(ID, destination) # Gets all the tasks for a specified employee
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")

    def filterContractors(self, destination = None):
        self.displayContractors(destination) # Show them the complete list and then ask if they want any more fliltering...
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
                    contractor = self.LogicLayerWrapper.getContractorbyID(ID, destination)
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
                    tasks = self.LogicLayerWrapper.getTasksForContractorID(ID, destination) # Takes in x amount of Maintenance Tasks a contractor has worked 
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")

    def filterProperties(self, destination = None):
        self.displayProperties(destination) # Show them the complete list and then ask if they want any more filtering....
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
                    property = self.LogicLayerWrapper.getPropertyByID(ID, destination)
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
                    tasks = self.LogicLayerWrapper.getTasksForPropertyID(ID, destination) # Takes in x amount of Maintenance Tasks done on specific property
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")
    
    def filterMaintenanceTasks(self):
        self.displayMaintenanceTasks() #Show them the complete list and then ask if they want any more filtering....
        while True:
            print("\n-------------------------------------------------------")
            print("1: To view additional information of a specific Maintenance Task")
            print("2: To view all Maintenance Tasks that are ready to be closed (Through closing the Maintenance Report)")
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
            elif user_choice == "2":
                try:
                    reports = self.LogicLayerWrapper.getReadyToBeClosedMaintenanceTasks()
                    for report in reports:
                        self.Displays.printMaintenanceTask(report)
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")
    
    def filterMaintenanceSchedules(self):
        self.displayMaintenanceSchedules() # Show them the complete list and then ask if they want any more filtering....
        while True:
            print("\n-------------------------------------------------------")
            print("1: To view additional information of a specific Maintenance Schedule")
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
        self.displayMaintenanceReports()
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
        self.displayDestinations()
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
            
            elif user_choice == "1":  # Employees at Destination
                ID = input("ID of the Destination you want to show Employee information for ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    # In order to reuse the fiter functions for Employees, Contractors and Properties we need to give it a destination so that the GetTasksFor (Property, Contractors, Employees) can filter on the destination
                    # This reduces duplicate code
                    destination = self.LogicLayerWrapper.getDestinationByID(ID)
                    #self.displayDestinationEmployees(destination)
                    self.filterEmployees(destination) # Call the filterEmployees with the specific destination user wanted to look at
                    
                except ValueError as error:
                    print(error)
            elif user_choice == "2": # Contractors At Destination
                ID = input("ID of the Destination you want to show Contractor information for ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID)
                    self.filterContractors(destination)
                    # Try giving Display Contractor a list of contractors on that location ? then call the filter contractors ?
                except ValueError as error:
                    print(error)
            elif user_choice == "3": # Properties at Destination
                ID = input("ID of the Destination you want to show Property information for ")

                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID)
                    self.filterProperties(destination)
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