# View UI Logic
from os import system, name
from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .Displays import Displays
from prettytable import PrettyTable

class ViewUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.Displays = Displays()

    def clearTerminal(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")    

    def viewMenu(self):
        self.clearTerminal()
        # Instead of having a very long nested elif statement we will have a dictionary of valid options and we will check on key in that dictionary for the users choice
        # Reduces code and makes it easier to read 
        validOptions = {
            "1": self.filterEmployees,
            "2": self.filterContractors,
            "3": self.filterProperties,
            "4": self.filterMaintenanceTasks,
            "5": self.filterMaintenanceSchedules,
            "6": self.filterMaintenanceReports,
            "7": self.filterDestinations
        }
        error_message = None
        while True:
            print(self.Displays.ViewMenu())
            if error_message:
                print(f"Error: {error_message}")
                error_message = None
            user_choice = input("Choice: ")
            # We check if the user wants to quit or go back to the previous menu
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"
            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            # Then we check if we have the input as a key in our valid options dictionary and if he have it use the function inside of it which calls another menu
            elif user_choice in validOptions:
                result = validOptions[user_choice]() # Can not have the function directly in the dictionary it calls them, so we need to only call them after we have received the valid input by storing the reference
                if result == "q":
                    return "q" # We dont want to return Back even if user presses back because then we would go back to the main menu which we dont want
            else:
                error_message = "Invalid Input"
                self.clearTerminal()

    def displayEmployees(self, destination = None):
        # For displaying employees in the pretty table we omit, Address and Home phone
        # User can easily find that information through choosing to view additional information on a specific employee
        employeespretty = PrettyTable()
        employeespretty.field_names = ["Employee Number", "Employee Name", "Social Security Number", "GSM Phone","Email", "Working at destination", "Type of Employee"]
        employees = self.LogicLayerWrapper.getEmployeeData(destination)
        for employee in employees:
            employeespretty.add_row([employee.employeeID, employee.name, employee.socialSecurity, employee.gsmPhone, employee.email, employee.workLocation , employee.type], divider=True)        
        employeespretty.align = 'l'
        employeespretty.max_table_width = 150
        employeespretty.min_table_width = 100
        employeespretty.max_width = 30
        print(employeespretty)

    def displayManagers(self, destination = None):
        # For displaying managers in the pretty table we omit, Address and Home phone
        # User can easily find that information through choosing to view additional information on a specific employee
        managerspretty = PrettyTable()
        managerspretty.field_names = ["Employee Number", "Employee Name", "Social Security Number", "GSM Phone","Email", "Working at destination", "Type of Employee"]
        managers = self.LogicLayerWrapper.getManagers(destination)
        for manager in managers:
            managerspretty.add_row([manager.employeeID, manager.name, manager.socialSecurity, manager.gsmPhone, manager.email, manager.workLocation , manager.type], divider=True)        
        managerspretty.align = 'l'
        managerspretty.max_table_width = 150
        managerspretty.min_table_width = 100
        managerspretty.max_width = 30
        print(managerspretty)
        
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
        propertiespretty.hrules = True 
        propertiespretty.vrules = True  
  
        print(propertiespretty)

    def displayMaintenanceTasks(self, destination = None):
        maintenanceTasks = self.LogicLayerWrapper.getMaintenanceTaskData(destination)
        tasks_pretty = PrettyTable()
        tasks_pretty.field_names = ["Task ID", "Property ID", "Description", "Start Date", "End Date", "Status", "Priority", "Recurring"]
        for task in maintenanceTasks:
            tasks_pretty.add_row([task.maintenanceID,task.propertyID,task.description,task.startDate,task.endDate,task.statusMaintenance,task.priority,task.recurring])
        tasks_pretty.align = "l"  
        tasks_pretty.max_width = 30  
        tasks_pretty.min_table_width = 100 
        tasks_pretty.max_table_width = 120  
        tasks_pretty.hrules = True 
        tasks_pretty.vrules = True 

        # Display the table
        print(tasks_pretty)

    def displayMaintenanceSchedules(self):
        maintenanceSchedules = self.LogicLayerWrapper.getMaintenanceScheduleData()
        schedules_pretty = PrettyTable()
        schedules_pretty.field_names = ["Schedule ID", "Maintenance ID", "Task Type", "Frequency", "Start Date"]
        for schedule in maintenanceSchedules:
            schedules_pretty.add_row([ schedule.maintenanceScheduleID, schedule.maintenanceID, schedule.taskType, schedule.frequency, schedule.startDate])
        schedules_pretty.align = "l"  
        schedules_pretty.max_width = 30  
        schedules_pretty.min_table_width = 100  
        schedules_pretty.max_table_width = 120 
        schedules_pretty.hrules = 1 
        schedules_pretty.hrules = True 
        schedules_pretty.vrules = True 

        # Display the table
        print(schedules_pretty)


    def displayMaintenanceReports(self):
        maintenanceReports = self.LogicLayerWrapper.getMaintenanceReportData()
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

        maintenance_reports_pretty.align = "l"  
        maintenance_reports_pretty.max_width = 90
        maintenance_reports_pretty.min_table_width = 100 
        maintenance_reports_pretty.max_table_width = 170
        maintenance_reports_pretty.hrules = True 
        maintenance_reports_pretty.vrules = True 

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
        destinations_pretty.hrules = True 

        print(destinations_pretty)

    def filterEmployees(self, destination = None):
        self.clearTerminal()
        # Function can receive a destination if user is asking for specific employees at a specific destination
        error_message = None
        while True:
            self.displayEmployees(destination) # Show them the complete list and then ask if they want any more filtering....
            print(self.Displays.filterEmployeesMenu()) # Always show the menu, even if an error was found
            if error_message:
                print(f"Error: {error_message}")
                error_message = None
            user_choice = input("Choice: ")
            # Handle initial Quit and go back user inputs
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"
            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"

            elif user_choice == "1": # User wants to Look up a specific Employee
                ID = input("ID of the Employee you want to look up: ")
                # If user changes his mind and wants to quit or go back from this point, if he goes back when picking ID he should go back to the main filter employees screen because he may have wanted to choose to show tasks instead of specific employee f.x
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    employee = self.LogicLayerWrapper.getEmployeebyID(ID, destination)
                    self.Displays.printEmployee(employee)
                    done_looking = input("Press any button if you are done: ")
                    if done_looking == "q":
                        return "q"
                    self.clearTerminal()
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "2":
                ID = input("ID of the Employee you want to show tasks for: ")
                # If user changes his mind and wants to quit or go back from this point, if he goes back when picking ID he should go back to the main filter employees screen because he may have wanted to choose to specific employee instead of show tasks f.x
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    tasks = self.LogicLayerWrapper.getTasksForEmployeeID(ID, destination) # Gets all the tasks for a specified employee from logic layer
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # Open the dateFiter menu, see if user wants to do that aswell
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "3":
                self.displayManagers(destination)
                done_looking = input("Press any button if you are done: ")
                if done_looking == "q":
                    return "q"
                self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()
            

    def filterContractors(self, destination = None):
        self.clearTerminal()
        error_message = None
        title_message = "Contractor Information"
        while True:
            self.displayContractors(destination) # Show them the complete list and then ask if they want any more fliltering...
            print(self.Displays.filterContractorsMenu()) # Always show the menu, even if an error was found
            if error_message:
                print(f"Error: {error_message}")
                error_message = None

            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1":
                ID = input("ID of the Contractor you want to look up: ")
                # If user changes his mind and wants to quit he quits, if he wants to go back he goes back to the displayContractors screen so he can choose another option from it
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    contractor = self.LogicLayerWrapper.getContractorbyID(ID, destination)
                    self.Displays.printEmployee(contractor, title_message)
                    done_looking = input("Press any button if you are done: ")
                    if done_looking == "q":
                        return "q"
                    self.clearTerminal()
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "2":
                ID = input("ID of the Contractor you want to show tasks for: ")
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    tasks = self.LogicLayerWrapper.getTasksForContractorID(ID, destination) # Takes in x amount of Maintenance Tasks a contractor has worked 
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()

    def filterProperties(self, destination = None):
        self.clearTerminal()
        error_message = None
        while True:
            self.displayProperties(destination) # Show them the complete list and then ask if they want any more filtering....
            print(self.Displays.filterPropertiesMenu())
            if error_message:
                print(f"Error: {error_message}")
                error_message = None

            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1":
                ID = input("ID of the Property you want to look up: ")

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    property = self.LogicLayerWrapper.getPropertyByID(ID, destination)
                    self.Displays.printProperty(property)
                    done_looking = input("Press any button if you are done: ")
                    if done_looking == "q":
                        print("Quitting")
                        return "q"
                    self.clearTerminal()
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "2":
                ID = input("ID of the Property you want to show tasks for: ")

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    tasks = self.LogicLayerWrapper.getTasksForPropertyID(ID, destination) # Takes in x amount of Maintenance Tasks done on specific property
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter menu
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()
    
    def filterMaintenanceTasks(self, destination = None):
        self.clearTerminal()
        error_message = None
        while True:
            self.displayMaintenanceTasks(destination) #Show them the complete list and then ask if they want any more filtering....
            print(self.Displays.filterMaintenanceMenu())
            if error_message:
                print(f"Error: {error_message}")
                error_message = None

            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1":
                ID = input("ID of the Maintenance Task you want to look up: ")

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    task = self.LogicLayerWrapper.getMaintenanceTaskByID(ID, destination)
                    self.Displays.printMaintenanceTask(task)
                    done_looking = input("Press any button if you are done: ")
                    if done_looking == "q":
                        return "q"
                    self.clearTerminal()
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "2":
                try:
                    reports = self.LogicLayerWrapper.getReadyToBeClosedMaintenanceTasks(destination)
                    for report in reports:
                        self.Displays.printMaintenanceTask(report)
                    done_looking = input("Press any button if you are done: ")
                    if done_looking == "q":
                        return "q"
                    self.clearTerminal()
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()
    
    def filterMaintenanceSchedules(self):
        self.clearTerminal()
        error_message = None
        while True:
            self.displayMaintenanceSchedules() # Show them the complete list and then ask if they want any more filtering....
            print(self.Displays.filterMaintenanceScheduleMenu())
            if error_message:
                print(f"Error: {error_message}")
                error_message = None

            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1":
                ID = input("ID of the Maintenance Schedule you want to look up: ")

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    task = self.LogicLayerWrapper.getMaintenanceScheduleByID(ID)
                    self.Displays.printMaintenanceSchedule(task)
                    done_looking = input("Press any button if you are done: ")
                    if done_looking == "q":
                        return "q"
                    self.clearTerminal()
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()          

    def filterMaintenanceReports(self):
        self.clearTerminal()
        error_message = None
        while True:
            self.displayMaintenanceReports()
            print(self.Displays.filterMaintenanceReportMenu())
            if error_message:
                print(f"Error: {error_message}")
                error_message = None

            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1":
                ID = input("ID of the Maintenance Report you want to look up: ")

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    report = self.LogicLayerWrapper.getMaintenanceReportByID(ID)
                    self.Displays.printMaintenanceReport(report)
                    done_looking = input("Enter any button if you are done: ")
                    if done_looking == "q":
                        print("Quitting")
                        return "q"
                    self.clearTerminal()
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()      

    def filterDestinations(self):
        self.clearTerminal()
        error_message = None
        while True:
            self.displayDestinations()
            print(self.Displays.filterDestinationMenu())
            if error_message:
                print(f"Error: {error_message}")
                error_message = None  

            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1":  # Employees at Destination
                ID = input("ID of the Destination you want to show Employee information for ")

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    # In order to reuse the fiter functions for Employees, Contractors and Properties we need to give it a destination so that the GetTasksFor (Property, Contractors, Employees) can filter on the destination
                    # This reduces duplicate code
                    destination = self.LogicLayerWrapper.getDestinationByID(ID)
                    result = self.filterEmployees(destination) # Call the filterEmployees with the specific destination user wanted to look at
                    if result.lower() == "q":
                        return "q"
                    elif result.lower() == "b":
                        self.clearTerminal()
                        continue
                    
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "2": # Contractors At Destination
                ID = input("ID of the Destination you want to show Contractor information for ")

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID)
                    result = self.filterContractors(destination)
                    if result.lower() == "q":
                        return "q"
                    elif result.lower() == "b":
                        self.clearTerminal()
                        continue
                    # Try giving Display Contractor a list of contractors on that location ? then call the filter contractors ?
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "3": # Properties at Destination
                ID = input("ID of the Destination you want to show Property information for ")

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID)
                    result = self.filterProperties(destination)
                    if result.lower() == "q":
                        return "q"
                    elif result.lower() == "b":
                        self.clearTerminal()
                        continue
                    # Try giving Display properties a list of properties on that location ? then call the filter properties ?
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "4": # Filtering all maintenance tasks on a specific location
                ID = input("ID of the Destination you want to show Maintenance Task information for ")

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID)
                    result = self.filterMaintenanceTasks(destination)
                    if result.lower() == "q":
                        return "q"
                    elif result.lower() == "b":
                        self.clearTerminal()
                        continue
                    # Try giving Display properties a list of properties on that location ? then call the filter properties ?
                except ValueError as error:
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()   

    def dateFilter(self, tasks):
        error_message = None
        while True:
            print(self.Displays.FilterDateMenu())
            if error_message:
                print(f"Error: {error_message}")
                error_message = None

            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"

            elif user_choice == "1":
                startDate = input("Start Date: ")
                endDate = input("End Date: ")
                filtered_tasks = self.LogicLayerWrapper.filterMaintenanceTasksDates(tasks, startDate, endDate)
                for filtered_task in filtered_tasks:
                    self.Displays.printMaintenanceTask(filtered_task)
            else:
                error_message = "Invalid Input"