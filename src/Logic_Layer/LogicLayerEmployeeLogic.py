from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Workers import Employee, Contractor
from .ErrorCheckers import ErrorCheckers
from Models.Maintenance import Maintenance
from Models.Destination import Destination

class LogicLayerEmployeeLogic:
    def __init__(self):
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()
    
    def createUniqueID(self) -> int:
        """ Function loads all Employees from DB, finds the last assigned ID and adds one to it, creating a new ID, returns unique id int"""
        #here we create a new unique ID for the employees
        currentEmployees = self.DataLayerWrapper.loadEmployeeLog() # Loads all employees from DB
        if len(currentEmployees) != 0:
            newID = currentEmployees[-1].employeeID + 1 # Assign new employee with a unique ID
        else: # If there are no employees in the DB the unique employee ID starts at 1
            newID = 1
        return newID
    
    def createTempEmployee(self, type_of_employee) -> Employee:
        """ Function creates a temporary employee based on user input for the user to fill out, it is assigned a unique INT ID, returns a temporary employee """
        #  Type of employee should be "1" for General Employee, "2 " for Manager, "3" for Contractor 
        tempEmployeeID = self.createUniqueID() # Gets a unique ID for the employee
        if type_of_employee == "1": # General Employee
            temp_employee = Employee(ID=tempEmployeeID, type="General") # Assigns a type depending on user choice
        elif type_of_employee == "2": # Manager
            temp_employee = Employee(ID=tempEmployeeID, type="Manager") # Assigns a type depending on user choice
        elif type_of_employee == "3": # Contractor
            temp_employee = Contractor()
            temp_employee.employeeID = tempEmployeeID # ID
            temp_employee.type = "Contractor" # Assigns type
        else:
            return None
        return temp_employee
    
    def validateEmployeeInput(self, input, count, temp_employee) -> True:
        """ Function checks for each attribute of the employee the user changes if it is of the desired format, returns True or raises ValuError"""
        # We dont have to check for ID and type since that is automatically assigned based on user choice
        if self.Errors.checkNumber(count):
            count = int(count)
        # This function doubles as a validation for creating employees and updating them, when editing employees instead of count we get the number of the attribute the user wants to change, thats why we need to change it into an integer even though count would usually be an integer
        if count == 1:  # Name
            self.Errors.errorCheckName(input)
            temp_employee.name = input
        elif count == 2:  # Social Security
            self.Errors.errorCheckSocialSecurity(input)
            temp_employee.socialSecurity = input
        elif count == 3:  # Address
            self.Errors.errorCheckAddress(input)
            temp_employee.address = input
        elif count == 4:  # At Home Phone
            self.Errors.errorCheckPhone(input)
            temp_employee.atHomePhone = input
        elif count == 5:  # GSM Phone
            self.Errors.errorCheckPhone(input)
            temp_employee.gsmPhone = input
        elif count == 6:  # Email
            self.Errors.errorCheckEmail(input)
            temp_employee.email = input
        elif count == 7:  # Work Location
            # Check first if there exists a Manager at that Destination beforehand
            self.Errors.checkNumber(input)
            dest_ID = int(input)
            destination = self.checkIfDestinationExists(dest_ID) # See if we have Destination in DB
            if temp_employee.type == "Manager": # Only do the checks if the user is creating a manager, because a general employee can always work at any location
                self.checkIfManagerAtDestination(destination) # See if there exists a Manager, if so we need to ask the user if we wants to overwrite That Manager
                # If no errors were raised until this point, this is a valid destination with no Manager in it, so we need to update the destination manager and then save it
                self.addManagerToDestination(destination, temp_employee)
            temp_employee.workLocation = dest_ID
        # Beyond this point is contractor specific
        elif count == 8:  # Previous tasks of contractor
            if input != "":
                self.Errors.errorCheckEmployeePreviousTask(input)
                tasks = input.split(",") # Will create a list of the maintenance ID's in a string format, we need to check if they exist
                for task in tasks:
                    self.checkIfMaintenanceExists(int(task))
                # at this point we know all the previous tasks are valid and on existant maintenances so we add the string to the attribute
                temp_employee.previousTask = input
        elif count == 9: # Performance rating of those previous tasks
            if temp_employee.previousTask != "":
                can_be_empty = False
            else:
                can_be_empty = True
            self.Errors.errorCheckEmployeePerformanceRating(input, can_be_empty)
            temp_employee.performanceRating = input
        elif count == 10: # We should get a reference to an already existant either General Employee or Manager
            self.Errors.checkNumber(input) # Checks if its indeed a nubmer otherwise we cant integer it
            self.getEmployeebyID(int(input)) # Will raise an error if employee dosent exist because the contact cant be a contact if he dosent exist...
            temp_employee.contractorContact = int(input)
        elif count == 11:
            self.Errors.errorCheckEmployeeOpeningHours(input)
            temp_employee.openingHours = input
        return True
    
    def checkIfMaintenanceExists(self, maintenance_ID) -> True:
        """ Function takes in a maintenance id, loads all maintenances from the DB and checks if there exists a maintenance by that ID in the DB, returns true or raises a ValueError"""
        maintenanceLog = self.DataLayerWrapper.loadMaintenanceLog()
        for maint in maintenanceLog:
            if maint.maintenanceID == maintenance_ID:
                return True
        raise ValueError("Contractor can not have a Maintenance that does not exist as a previous task")

    def addManagerToDestination(self, destination, temp_employee) -> None:
        """ Function takes in a destination and a temp_employee, it sets the temp_employees ID as the manager of that destination and saves the destination in the DB"""
        destination.managerOfDestination = temp_employee.employeeID # Set the destination manager as the manager employeeid we are creating
        self.DataLayerWrapper.updateDestination(destination) # update the destination DB

    def checkIfDestinationExists(self, dest_ID) -> Destination:
        """ Function takes in a Destination ID and checks if we have a Destination by that ID in our Destination DB, raises ValueError if not found else returns Destination"""
        destinations = self.DataLayerWrapper.loadDestinationsLog() # Loads all destinations from DB
        for dest in destinations:
            if dest.destinationID == dest_ID: # Tries to find the destination based on the given destination ID
                return dest # If we find it return the destination
        raise ValueError("No Destination by that ID exists")

    def checkIfManagerAtDestination(self, destination) -> True:
        """ Functions takes in a Destination and checks if that Destination already has a Manager, raises KeyError if it has , returns True if not"""
        if destination.managerOfDestination != "": # Checks if destination has a manger
            raise KeyError("This Destination already has a Manager") # This keyError can be used to trigger an overwrite feature for the manager
        else:
            return True

    def exchangeManagersAtLocation(self, destination_id, temp_employee) -> None:
        """ Function takes in a destination_id as string and temp_employee, demotes the current manager of that destination to General Employee and updates that employee information, 
        and makes the temp_employee the new manager and saves it to the destination DB and puts temp_employees worklocation as the destination """
        destination = self.checkIfDestinationExists(int(destination_id)) # See if the destination exists and get the destination
        current_manager_ID = destination.managerOfDestination # Get manager of that destination
        employeeLog = self.DataLayerWrapper.loadEmployeeLog() # get all employees
        # Make the current manager a General Employee
        for employee in employeeLog:
            if employee.employeeID == current_manager_ID: # Find the current manager of the location in the employees DB
                employee.type = "General" # Change the type
                self.DataLayerWrapper.updateEmployee(employee) # Update that employee in the employee DB
                break
        # Make the temp employee the new manager
        destination.managerOfDestination = temp_employee.employeeID # Put the destination manager as the new manager id
        temp_employee.workLocation = int(destination_id) # put the worklocation of the new manager as the destination
        self.DataLayerWrapper.updateDestination(destination) # Finally update that destination in the destination DB
        
    def getEmployeebyID(self, ID, destination = None) -> Employee:
        """ Function loads all Employees and tries to find the specified employee by ID in the DB, if there is a destination specified it filters by that first, returns Employee if found or raises ValueError"""
        if self.Errors.checkNumber(ID): # Checks if the id is a number
            destination_filter = False # Flag to determine if function should filter based on destination aswell
            employeeLog = self.DataLayerWrapper.loadEmployeeLog() # Loads all the employees
            index_to_update = -1

            if destination is not None: # If destination is not None we filter by destination otherwise we do not
                destination_filter = True

            for index, employee in enumerate(employeeLog):
                if destination_filter: # If we do have a destination we apply the destination filter aswell
                    if employee.employeeID == int(ID) and employee.type != "Contractor" and employee.workLocation == destination.destinationID:
                        index_to_update = index # With this we found the employee at that specific location
                        break
                else: # This means that we had no destination specified
                    if employee.employeeID == int(ID) and employee.type != "Contractor":
                        index_to_update = index # We found the employee
                        break
            if index_to_update != -1:
                employee_found = employeeLog[index_to_update] # Extract that employee we found
                return employee_found # and return it
            else: # If we never found the employee then the index remains -1 so we raise the error
                raise ValueError("No Employee by that ID")
    
    def getContractorbyID(self, ID, destination = None) -> Contractor:
        """ Function loads all Employees and tries to find the specified Contractor by ID in the DB, returns Contractor or raises ValueError"""
        if self.Errors.checkNumber(ID): # Checks if the id is a number
            destination_filter = False # Flag to determine if function should filter based on destination aswell
            employeeLog = self.DataLayerWrapper.loadEmployeeLog() # Loads all the employees
            index_to_update = -1

            if destination is not None: # If destination is not None we filter by destination otherwise we do not
                destination_filter = True

            for index, contractor in enumerate(employeeLog):
                if destination_filter: # If we do have a destination we apply the destination filter aswell
                    if contractor.employeeID == int(ID) and contractor.type == "Contractor" and contractor.workLocation == destination.destinationID: ## Making sure that the ID provided is a contractor, we can have the ID in the DB but it could be a General Employee or a Manager
                        index_to_update = index
                        break
                else:
                    if contractor.employeeID == int(ID) and contractor.type == "Contractor": ## Making sure that the ID provided is a contractor, we can have the ID in the DB but it could be a General Employee or a Manager
                        index_to_update = index
                        break

            if index_to_update != -1:
                contractor_found = employeeLog[index_to_update] # Extract the contractor we found
                return contractor_found
            else: # If we never found the contractor then the index remains -1 so we raise the error
                raise ValueError("No Contractor by that ID")

    def getEmployeeData(self, destination = None) -> list[Employee]:
        """ Load all the employees from the DB and filter out all the General Employess and Managers to return in a list format, can also filter by destination if it is specified """
        employeeLog = self.DataLayerWrapper.loadEmployeeLog() # Load all employees
        destination_filter = False # Flag to see if we will filter on destination aswell
        filtered_employees = []

        if destination is not None:
            destination_filter = True # This means we will filter on destination

        for employee in employeeLog:
            if destination_filter: # If we are filtering on destination
                if employee.type != "Contractor" and employee.workLocation == destination.destinationID:
                    filtered_employees.append(employee) # Only append the employees that are on that destination
            else:
                if employee.type != "Contractor":
                    filtered_employees.append(employee)
        return filtered_employees
    
    def getContractorData(self, destination = None) -> list[Contractor]:
        """ Load all employees from the DB and filter out all the contractors to return in a list format """
        contractorlog = self.DataLayerWrapper.loadEmployeeLog() # Load all employees
        destination_filter = False # Flag to see if we will filter on the destination aswell
        filtered_contractors = []

        if destination is not None:
            destination_filter = True # This means we will filter on destination

        for contractor in contractorlog:
            if destination_filter: # If we are filtering on destination
                if contractor.type == "Contractor" and contractor.workLocation == destination.destinationID:
                    filtered_contractors.append(contractor) # Only append the contractors that are on that destination
            else:
                if contractor.type == "Contractor":
                    filtered_contractors.append(contractor)
        return filtered_contractors
    
    def getTasksForEmployeeID(self, ID, destination = None) -> Maintenance:
        """ Function finds the Employee, loads all maintenance reports and tasks and filters out all the maintenance tasks an employee has worked, returns filtered list of maintenance tasks or raises ValuError"""
        # We take in the employee ID
        # Find the employee
        # Load in all maintenance reports
        # If the employee is in a maintenance report we append the maintenance associated with that maintenance report into a list to return
        # In addition to this if we get passed a destination, the getemployeebyid function will filter on destination which means that this function does that aswell essentially
        employee = self.getEmployeebyID(ID, destination) # We get the employee either with destination specified, if no employee by that ID at that location it will raise a ValueError, otherwise it keeps going, if there was no destination specified it ignores it
        maintenanceTaskLog = self.DataLayerWrapper.loadMaintenanceLog() # Loads all maintenances
        maintenanceReportLog = self.DataLayerWrapper.loadMaintenanceReportLog() # Loads all maintenace reports
        employeeTasks = []
        maintenanceTaskIDs = []
        for report in maintenanceReportLog: 
            if report.employeeID == employee.employeeID: # Find all the reports that have that employee associated with it
                maintenanceTaskIDs.append(report.maintenanceID) # Extract all the maintenance ID's from those reports and put them in a list
        # We have found all the maintenances that a employee has worked on now we need to append the maintenances
        for maintenanceTask in maintenanceTaskLog:
            if maintenanceTask.maintenanceID in maintenanceTaskIDs: # We need to fetch the actual maintenance classes from the maintenance DB, we get that by filtering them on ID
                employeeTasks.append(maintenanceTask)
                
        if len(employeeTasks) == 0: # Just in case we found no tasks we raise an error that an employee has worked on (might be on a specific location)
            raise ValueError("This Employee has not worked on any Maintenance Tasks")
            
        return employeeTasks

    def getTasksForContractorID(self, ID, destination = None) -> list[Maintenance]:
        """ Function finds the Contractor, loads all maintenance reports and tasks and filters out all the maintenance tasks a contractor has worked, returns filtered list of maintenance tasks or raises ValuError"""
        # We take in the contractor ID
        # Find the contractor
        # Load in all maintenance reports
        # If the contractor is in a maintenance report we append the maintenance associated with that maintenance report into a list to return
        # In addition to this if we get passed a destination, the getemployeebyid function will filter on destination which means that this function does that aswell essentially
        contractor = self.getContractorbyID(ID, destination) # We either have destination to filter or not, if the contractor is on that destination we get the tasks if not we raise ValueError that he dosent exist, because hes not at that location, if no destination is specified it does not matter
        maintenanceTaskLog = self.DataLayerWrapper.loadMaintenanceLog() # Loads all maintenances
        maintenanceReportLog = self.DataLayerWrapper.loadMaintenanceReportLog() # Loads all maintenace reports
        contractorTasks = []
        maintenanceTaskIDs = []
        for report in maintenanceReportLog:
            if report.contractorID == contractor.employeeID: # Find all the reports that have that contractor associated with it
                maintenanceTaskIDs.append(report.maintenanceID) # Extract all the maintenance ID's from those reports and put them in a list
        # We have found all the maintenances that a contractor has worked on now we need to append the maintenances
        for maintenanceTask in maintenanceTaskLog:
            if maintenanceTask.maintenanceID in maintenanceTaskIDs: # We need to fetch the actual maintenance classes from the maintenance DB, we get that by filtering them on ID
                contractorTasks.append(maintenanceTask)

        if len(contractorTasks) == 0: # Just in case we found no tasks we raise an error that a contractor has worked on (might be on a specific location)
            raise ValueError("This Contractor has not worked on any Maintenance Tasks")
            
        return contractorTasks

    def createEmployee(self, temp_employee) -> None:
        """ Function takes in a completely filled out temp_employee and saves it in our Employee DB"""
        # [name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType] for employees 
        # [name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType, previousTask, performanceRating, contractorContact, openingHours] for contractors
        if temp_employee == "Contractor": # We seperate them on type because they have different parameters
            self.DataLayerWrapper.createContractor(temp_employee) # Calls to create a contractor
        else:
            self.DataLayerWrapper.createEmployee(temp_employee) # Calls to create an employee
    
    def updateEmployeeData(self, employee) -> None:
        """ Function takes in employee already in DB and overwrites it with the new attributes and saves it in Employee DB """
        # input can be name, address, socialSecurity, atHomePhone, gsm, email, workLocation, for employees 
        self.DataLayerWrapper.updateEmployee(employee)

    def getDestinationData(self) -> list[Destination]:
        """ Function loads all Destinations from the destination DB, returns them in Class Destination format"""
        destinations = self.DataLayerWrapper.loadDestinationsLog()
        return destinations
    
    def getDestinationByID(self, ID) -> Destination:
        """ Function loads all Destinations and tries to find the specified Destination by ID in the DB, returns Destination if found or raises ValueError"""
        if self.Errors.checkNumber(ID): # Check if the ID is a number
            destinationLog = self.DataLayerWrapper.loadDestinationsLog() # Load all the destinations
            index_to_update = -1
            for index, destination in enumerate(destinationLog): # Go through the list of destinations
                if destination.destinationID == int(ID): # If we find the specified destination
                    index_to_update = index # We store the index of that destination in the destination list
            if index_to_update != -1:
                destination_found = destinationLog[index_to_update] # And use that index to extract him from the list
                return destination_found
            else: # If we havent found the employee then the index will remain -1 and we raise the error
                raise ValueError("No Destination by that ID")