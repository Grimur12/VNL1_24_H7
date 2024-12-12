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

    def viewMenu(self) -> str:
        """ Main viewing menu to view all the things we have in our DB, returns str (q and b for quitting and back features)"""
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
        error_message = None # Error message for clarity
        while True:
            print(self.Displays.ViewMenu()) # Display the menu for the user, so he has options on what to pick
            if error_message: # Error message handling to make the error persistant even through clearing screens. Allows us to keep the UI clear but still show the user what he did wrong
                print(f"Error: {error_message}")
                error_message = None # Reset the error message after displaying, necessary because if he were to for example input something invalid and then go to another menu and go back this message would persist if not reset
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

    def displayEmployees(self, destination = None) -> None:
        """ Function creates a table to display all of the employees in a specified format, it is also used when the user is filtering on a destination, the logic layer only provides us with a list of employees related to that destination"""
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

    def displayManagers(self, destination = None) -> None:
        """ Function creates a table to display all of the managers in a specified format, it is also used when the user is filtering on a destination, the logic layer only provides us with a list of managers related to that destination"""
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
        
    def displayContractors(self, destination=None) -> None:
        """ Function creates a table to display all of the contractors in a specified format, it is also used when the user is filtering on a destination, the logic layer only provides us with a list of contractors related to that destination"""
        # For displaying contractors in the pretty table we omit, Address, Home Phone, Previous Task and Performance Rating
        # User can easily find that information through choosing to view additional information on that specific contractor
        contractors_pretty = PrettyTable()
        contractors_pretty.field_names = ["Contractor Number", "Name", "Social Security", "GSM Phone", "Email", "Work Location", "Type", "Contractor Contact", "Opening Hours"]
        contractors = self.LogicLayerWrapper.getContractorData(destination)

        for contractor in contractors:
            contractors_pretty.add_row([contractor.employeeID, contractor.name, contractor.socialSecurity, contractor.gsmPhone, contractor.email, contractor.workLocation, contractor.type,  contractor.contractorContact, contractor.openingHours])
        contractors_pretty.align = 'l'  
        contractors_pretty.max_table_width = 160 
        contractors_pretty.min_table_width = 100  
        contractors_pretty.max_width = 30  
        contractors_pretty.hrules = True 
        contractors_pretty.vrules = True

        print(contractors_pretty)

    def displayProperties(self, destination = None) -> None:
        """ Function creates a table to display all of the properties in a specified format, it is also used when the user is filtering on a destination, the logic layer only provides us with a list of properties related to that destination"""
        propertiespretty = PrettyTable()
        propertiespretty.field_names = ["Property Number", "Property Name", "Available for rental", "Pool Available", "Tub Available", "Ovens Available"]
        properties = self.LogicLayerWrapper.getPropertyData(destination)
        for property in properties:
            propertiespretty.add_row([property.propertyID,property.nameOfProperty,property.availability,property.hasAPool,property.hasATub,property.hasOvens])
        propertiespretty.align = 'l'
        propertiespretty.max_width = 30
        propertiespretty.max_table_width = 140
        propertiespretty.min_table_width = 100
        propertiespretty.hrules = True 
        propertiespretty.vrules = True  
  
        print(propertiespretty)

    def displayMaintenanceTasks(self, destination = None) -> None:
        """ Function creates a table to display all of the maintenance tasks in a specified format, it is also used when the user is filtering on a destination, the logic layer only provides us with a list of maintenance tasks related to that destination"""
        maintenanceTasks = self.LogicLayerWrapper.getMaintenanceTaskData(destination)
        tasks_pretty = PrettyTable()
        tasks_pretty.field_names = ["Task ID", "Property ID", "Description", "Start Date", "End Date", "Status", "Priority", "Recurring"]
        for task in maintenanceTasks:
            tasks_pretty.add_row([task.maintenanceID,task.propertyID,task.description,task.startDate,task.endDate,task.statusMaintenance,task.priority,task.recurring])
        tasks_pretty.align = "l"  
        tasks_pretty.max_width = 30  
        tasks_pretty.min_table_width = 100 
        tasks_pretty.max_table_width = 150  
        tasks_pretty.hrules = True 
        tasks_pretty.vrules = True 

        # Display the table
        print(tasks_pretty)

    def displayMaintenanceSchedules(self) -> None:
        """ Function creates a table to display all of the maintenanceschedules in a specified format"""
        maintenanceSchedules = self.LogicLayerWrapper.getMaintenanceScheduleData()
        schedules_pretty = PrettyTable()
        schedules_pretty.field_names = ["Schedule ID", "Maintenance ID", "Task Type", "Frequency", "Start Date"]
        for schedule in maintenanceSchedules:
            schedules_pretty.add_row([ schedule.maintenanceScheduleID, schedule.maintenanceID, schedule.taskType, schedule.frequency, schedule.startDate])
        schedules_pretty.align = "l"  
        schedules_pretty.max_width = 30  
        schedules_pretty.min_table_width = 100  
        schedules_pretty.max_table_width = 140
        schedules_pretty.hrules = 1 
        schedules_pretty.hrules = True 
        schedules_pretty.vrules = True 

        # Display the table
        print(schedules_pretty)


    def displayMaintenanceReports(self) -> None:
        """ Function creates a table to display all of the maintenance reports in a specified format"""
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
        maintenance_reports_pretty.max_table_width = 150
        maintenance_reports_pretty.hrules = True 
        maintenance_reports_pretty.vrules = True 

        print(maintenance_reports_pretty)

    def displayDestinations(self) -> None:
        """ Function creates a table to display all of the destinations in a specified format"""
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

    def filterEmployees(self, destination = None) -> str:
        """Function is responsible for handling all user inputs realted to viewing employees, returns str (q or b) for quit and back features"""
        self.clearTerminal()
        # Function can receive a destination, passed from filterDestination which would get that from the logic layer, if user is asking for specific employees at a specific destination
        error_message = None
        while True:
            self.displayEmployees(destination) # Show them the complete list and then ask if they want any more filtering....
            print(self.Displays.filterEmployeesMenu()) # Always show the menu, even if an error was found
            if error_message: # Error message handling to make the error persistant even through clearing screens. Allows us to keep the UI clear but still show the user what he did wrong
                print(f"Error: {error_message}")
                error_message = None # Reset the error message after displaying, necessary because if he were to for example input something invalid and then go to another menu and go back this message would persist if not reset
            user_choice = input("Choice: ")
            # Handle initial Quit and go back user inputs
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"
            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"

            elif user_choice == "1": # User wants to Look up a specific Employee
                ID = input("ID of the Employee you want to look up: ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 
                # If user changes his mind and wants to quit or go back from this point, if he goes back when picking ID he should go back to the main filter employees screen because he may have wanted to choose to show tasks instead of specific employee f.x
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    employee = self.LogicLayerWrapper.getEmployeebyID(ID, destination) # Try to get the employee the user specified from the logic layer
                    self.Displays.printEmployee(employee) # display it for the user to see
                    done_looking = input("Press any button if you are done: ") # Done looking feature is implemented so that the user has time to view what he called after, he presses any button when he is done viewing to back to choose other options
                    if done_looking == "q":
                        return "q"
                    self.clearTerminal()
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "2": # User wants to view all tasks an employee has worked on
                ID = input("ID of the Employee you want to show tasks for: ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 
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
                    result = self.dateFilter(tasks) # Open the dateFiter menu, see if user wants to do that aswell
                    if result == "q":
                        return "q"
                except ValueError as error:# Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "3": # User wants to view the Manager(s)
                self.displayManagers(destination)
                done_looking = input("Press any button if you are done: ")# Done looking feature is implemented so that the user has time to view what he called after, he presses any button when he is done viewing to back to choose other options
                if done_looking == "q":
                    return "q"
                self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()
            

    def filterContractors(self, destination = None) -> str:
        """ Function is responsible for handling all user inputs related to viewing contractors, returns str (q or b) for quit and back features"""
        self.clearTerminal()
        # Function can receive a destination, passed from filterDestination which would get that from the logic layer, if user is asking for specific contractors at a specific destination
        error_message = None
        title_message = "Contractor Information"
        while True:
            self.displayContractors(destination) # Show them the complete list and then ask if they want any more fliltering...
            print(self.Displays.filterContractorsMenu()) # Always show the menu, even if an error was found
            if error_message: # Error message handling to make the error persistant even through clearing screens. Allows us to keep the UI clear but still show the user what he did wrong
                print(f"Error: {error_message}")
                error_message = None # Reset the error message after displaying, necessary because if he were to for example input something invalid and then go to another menu and go back this message would persist if not reset
            # Handle initial Quit and go back user inputs
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1": # User wants to view all additional information of a specific contractor
                ID = input("ID of the Contractor you want to look up: ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 
                # If user changes his mind and wants to quit he quits, if he wants to go back he goes back to the displayContractors screen so he can choose another option from it
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    contractor = self.LogicLayerWrapper.getContractorbyID(ID, destination) # Try to get the Contractor from the logic layer
                    self.Displays.printEmployee(contractor, title_message) # And print it out for the user to view
                    done_looking = input("Press any button if you are done: ")# Done looking feature is implemented so that the user has time to view what he called after, he presses any button when he is done viewing to back to choose other options
                    if done_looking == "q":
                        return "q"
                    self.clearTerminal()
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "2": # User wants to view all tasks a contractor has worked on
                ID = input("ID of the Contractor you want to show tasks for: ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 
                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    tasks = self.LogicLayerWrapper.getTasksForContractorID(ID, destination) # Try to get the tasks for the contractor ID the user inputted from the logic layer
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task) # And print them out for the user to view, could be none, many or one, we dont know so we have a loop 
                    result = self.dateFilter(tasks) # get the datefilter
                    if result == "q":
                        return "q"
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()

    def filterProperties(self, destination = None) -> str:
        """Function is responsible for handling all user inputs related to viewing properties, returns str (q or b) for quit and back features"""
        self.clearTerminal()
        # Function can receive a destination, passed from filterDestination which would get that from the logic layer, if user is asking for specific Properties at a specific destination
        error_message = None
        while True:
            self.displayProperties(destination) # Show them the complete list and then ask if they want any more filtering....
            print(self.Displays.filterPropertiesMenu()) # Inital showing the user the options for viewing properties, always show the menu even when an error occurs
            if error_message: # Error message handling to make the error persistant even through clearing screens. Allows us to keep the UI clear but still show the user what he did wrong
                print(f"Error: {error_message}")
                error_message = None # Reset the error message after displaying, necessary because if he were to for example input something invalid and then go to another menu and go back this message would persist if not reset
            # Handle initial Quit and go back user inputs
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1": # User wants to view additional information of a specific property
                ID = input("ID of the Property you want to look up: ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    property = self.LogicLayerWrapper.getPropertyByID(ID, destination) # Try to get the property the user specified from the logic layer
                    self.Displays.printProperty(property) # print it out for the user to see
                    done_looking = input("Press any button if you are done: ") # Done looking feature is implemented so that the user has time to view what he called after, he presses any button when he is done viewing to back to choose other options
                    if done_looking == "q":
                        print("Quitting")
                        return "q"
                    self.clearTerminal()
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "2": # User wants to view all maintenances done on a specific property
                ID = input("ID of the Property you want to show tasks for: ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    tasks = self.LogicLayerWrapper.getTasksForPropertyID(ID, destination) # Try to get the tasks for the property ID the user inputted from the logic layer
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task) # Print them out, could be many, one or none so we have the loop
                    result = self.dateFilter(tasks) # Show the user the options on if he wants to be more specific with the time of the tasks
                    if result == "q":
                        return "q"
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()
    
    def filterMaintenanceTasks(self, destination = None) -> str:
        """ Function is responsible for handling all user inputs for viewing maintenance tasks, returns str (q or b) for quit and back features"""
        self.clearTerminal()
        # Function can receive a destination, passed from filterDestination which would get that from the logic layer, if user is asking for specific maintenance tasks at a specific destination
        error_message = None
        while True:
            self.displayMaintenanceTasks(destination) #Show them the complete list and then ask if they want any more filtering....
            print(self.Displays.filterMaintenanceMenu()) # Show the user the options to view maintenance tasks, keep showing even with errors until he chooses something
            if error_message: # Error message handling to make the error persistant even through clearing screens. Allows us to keep the UI clear but still show the user what he did wrong
                print(f"Error: {error_message}")
                error_message = None # Reset the error message after displaying, necessary because if he were to for example input something invalid and then go to another menu and go back this message would persist if not reset
            # Handle initial Quit and go back user inputs
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1": # User wants to view additional information on a specific maintenance task
                ID = input("ID of the Maintenance Task you want to look up: ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    task = self.LogicLayerWrapper.getMaintenanceTaskByID(ID, destination) # Try to get the maintenace the user specified from the logic layer
                    self.Displays.printMaintenanceTask(task) # Print it out for him to see
                    done_looking = input("Press any button if you are done: ")# Done looking feature is implemented so that the user has time to view what he called after, he presses any button when he is done viewing to back to choose other options
                    if done_looking == "q":
                        return "q"
                    self.clearTerminal()
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "2": # User wants to view all maintenance tasks that are ready to be closed 
                try:
                    tasks_ = self.LogicLayerWrapper.getReadyToBeClosedMaintenanceTasks(destination) # Try to get the closed maintenance tasks from the logic layer
                    for task_ in tasks_:
                        self.Displays.printMaintenanceTask(task_) # could be many or one or none so we have the loop to show the user all of them, 
                    done_looking = input("Press any button if you are done: ")# Done looking feature is implemented so that the user has time to view what he called after, he presses any button when he is done viewing to back to choose other options
                    if done_looking == "q":
                        return "q"
                    self.clearTerminal()
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()
    
    def filterMaintenanceSchedules(self) -> str:
        """Function is responsible for handling all viewing realted user inputs for maintenance schedules, returns str (q or b) for quit and back features"""
        self.clearTerminal()
        error_message = None
        while True:
            self.displayMaintenanceSchedules() # Show them the complete list and then ask if they want any more filtering....
            print(self.Displays.filterMaintenanceScheduleMenu()) # Show the user the options he has for maintenance schedules
            if error_message: # Error message handling to make the error persistant even through clearing screens. Allows us to keep the UI clear but still show the user what he did wrong
                print(f"Error: {error_message}")
                error_message = None # Reset the error message after displaying, necessary because if he were to for example input something invalid and then go to another menu and go back this message would persist if not reset
            # Handle initial Quit and go back user inputs
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1": # To view additional information on a specfici maintenacne schedule
                ID = input("ID of the Maintenance Schedule you want to look up: ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    task = self.LogicLayerWrapper.getMaintenanceScheduleByID(ID) # Try to get the maintenance schedule the user specified from the logic layer
                    self.Displays.printMaintenanceSchedule(task) # Print it out for them to see
                    done_looking = input("Press any button if you are done: ")# Done looking feature is implemented so that the user has time to view what he called after, he presses any button when he is done viewing to back to choose other options
                    if done_looking == "q":
                        return "q"
                    self.clearTerminal()
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()          

    def filterMaintenanceReports(self) -> str:
        """Function is responisble for handling all user inputs related to viewing maintenance reports, returns str (q or b) for quit and back features"""
        self.clearTerminal()
        error_message = None
        while True:
            self.displayMaintenanceReports() # Show them a complete list of maintenance reports before asking them what they want to do
            print(self.Displays.filterMaintenanceReportMenu()) # Show them the options they have on viewing the maintenance reports
            if error_message: # Error message handling to make the error persistant even through clearing screens. Allows us to keep the UI clear but still show the user what he did wrong
                print(f"Error: {error_message}")
                error_message = None # Reset the error message after displaying, necessary because if he were to for example input something invalid and then go to another menu and go back this message would persist if not reset
            # Handle initial Quit and go back user inputs
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1": # To view additional information of a specific Maintenance Report
                ID = input("ID of the Maintenance Report you want to look up: ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    report = self.LogicLayerWrapper.getMaintenanceReportByID(ID) # Try to get the maintenance report specified by the user from the logic layer
                    self.Displays.printMaintenanceReport(report) # print it out for the user to see
                    done_looking = input("Enter any button if you are done: ")# Done looking feature is implemented so that the user has time to view what he called after, he presses any button when he is done viewing to back to choose other options
                    if done_looking == "q":
                        print("Quitting")
                        return "q"
                    self.clearTerminal()
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()      

    def filterDestinations(self) -> str:
        """Function is responsible for all user inputs for handling viewing a specific destination, inside of that it may use the filter employees and other related filter user input functions, returns str (q or b) for quit and back features"""
        self.clearTerminal()
        error_message = None
        while True:
            self.displayDestinations() # Show them all the destinations 
            print(self.Displays.filterDestinationMenu()) # Show the user the options he has for viewing specific things at destinations
            if error_message: # Error message handling to make the error persistant even through clearing screens. Allows us to keep the UI clear but still show the user what he did wrong
                print(f"Error: {error_message}")
                error_message = None # Reset the error message after displaying, necessary because if he were to for example input something invalid and then go to another menu and go back this message would persist if not reset
            # Handle initial Quit and go back user inputs
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            
            elif user_choice == "1": # To view information about Employees at a specific Destination
                ID = input("ID of the Destination you want to show Employee information for ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    # In order to reuse the fiter functions for Employees, Contractors and Properties we need to give it a destination so that the GetTasksFor (Property, Contractors, Employees) can filter on the destination
                    # This reduces duplicate code
                    destination = self.LogicLayerWrapper.getDestinationByID(ID) # Try to get the destination that the user specified from the logic layer
                    result = self.filterEmployees(destination) # Call the filterEmployees with the specific destination user wanted to look at to handle the rest of the emploee view user input handling
                    if result.lower() == "q":
                        return "q"
                    elif result.lower() == "b":
                        self.clearTerminal()
                        continue
                    
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "2": # To view information about Contractors at a specific Destination
                ID = input("ID of the Destination you want to show Contractor information for ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID) # Try to get the destination that the user specified from the logic layer
                    result = self.filterContractors(destination) # Call the filterContractors with the specific destination user wanted to look at to handle the rest of the contractor view user input handling
                    if result.lower() == "q":
                        return "q"
                    elif result.lower() == "b":
                        self.clearTerminal()
                        continue

                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "3": # To view information about Properties at a specific Destination
                ID = input("ID of the Destination you want to show Property information for ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID) # Try to get the destination that the user specified from the logic layer
                    result = self.filterProperties(destination) # Call the filterProperties with the specific destination user wanted to look at to handle the rest of the properties view user input handling
                    if result.lower() == "q":
                        return "q"
                    elif result.lower() == "b":
                        self.clearTerminal()
                        continue
                    # Try giving Display properties a list of properties on that location ? then call the filter properties ?
                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            elif user_choice == "4": # To view information about Maintenance Tasks at a specific Destination
                ID = input("ID of the Destination you want to show Maintenance Task information for ") # We always need the user to specify the ID of the object he wants to view so we can pass that along to the logic layer 

                if ID.lower() == "q":
                    print("Quitting")
                    return "q"
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue

                try:
                    destination = self.LogicLayerWrapper.getDestinationByID(ID) # Try to get the destination that the user specified from the logic layer
                    result = self.filterMaintenanceTasks(destination)  # Call the filterMaintenanceTasks with the specific destination user wanted to look at to handle the rest of the Maintenance Tasks view user input handling
                    if result.lower() == "q":
                        return "q"
                    elif result.lower() == "b":
                        self.clearTerminal()
                        continue

                except ValueError as error: # Catch value errors from wrong input and display it to the user
                    error_message = error
                    self.clearTerminal()
            else:
                error_message = "Invalid Input"
                self.clearTerminal()   

    def dateFilter(self, tasks) -> str:
        """ Function is responsible for handling all user inputs related to filtering on the start/end date for maintenance tasks, returns str (q or b) for quit and back features"""
        error_message = None
        while True:
            print(self.Displays.FilterDateMenu())
            if error_message: # Error message handling to make the error persistant even through clearing screens. Allows us to keep the UI clear but still show the user what he did wrong
                print(f"Error: {error_message}")
                error_message = None # Reset the error message after displaying, necessary because if he were to for example input something invalid and then go to another menu and go back this message would persist if not reset
            # Handle initial Quit and go back user inputs
            user_choice = input("Choice: ")
            if user_choice.lower() == "q":
                print("Quitting")
                return "q"

            elif user_choice.lower() == "b":
                self.clearTerminal()
                return "b"
            # We need to get both the start date and end date the user wants to see the tasks for while also looking out for if he wants to quit or back out of the program
            elif user_choice == "1":
                startDate = input("Start Date: ")
                if startDate == "b":
                    return "b"
                elif startDate == "q":
                    return "q"
                endDate = input("End Date: ")
                if endDate == "b":
                    return "b"
                elif endDate == "q":
                    return "q"
                
                filtered_tasks = self.LogicLayerWrapper.filterMaintenanceTasksDates(tasks, startDate, endDate) # Make the logic layer gives us the tasks over the time period the user specified
                self.clearTerminal()
                for filtered_task in filtered_tasks:
                    self.Displays.printMaintenanceTask(filtered_task) # Print them all out, for loop here because we do not know how many we will get
            else:
                error_message = "Invalid Input"