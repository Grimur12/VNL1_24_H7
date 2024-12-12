from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Maintenance import Maintenance
from Models.MaintenanceSchedule import MaintenanceSchedule
from Models.MaintenanceReport import MaintenanceReport
from .ErrorCheckers import ErrorCheckers
from datetime import datetime

class LogicLayerMaintenanceLogic:
    def __init__(self):
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()

    def createUniqueMaintenanceID(self) -> int:
        """ Function loads all Maintenances from DB, finds the last assigned ID and adds one to it, creating a new ID, returns unique id int"""
        currentMaintenance = self.DataLayerWrapper.loadMaintenanceLog()
        if len(currentMaintenance) != 0:
            newID = currentMaintenance[-1].maintenanceID + 1 # Since we never delete from the DB we can go to the last maintenance in the list and find the ID of it and +1 to get a new unique ID
        else:
            newID = 1 # If there are no maintenance already in the DB (list is empty) we simply start off with ID = 1
        return newID
    
    def createUniqueMaintenanceScheduleID(self) -> int:
        """ Function loads all Maintenance Schedules from DB, finds the last assigned ID and adds one to it, creating a new ID, returns unique id int"""
        currentMaintenanceSchedules = self.DataLayerWrapper.loadMaintenanceScheduleLog()
        if len(currentMaintenanceSchedules) != 0:
            newID = currentMaintenanceSchedules[-1].maintenanceScheduleID + 1 # Since we never delete from the DB we can go to the last maintenance schedule in the list and find the ID of it and +1 to get a new unique ID
        else:
            newID = 1 # If there are no maintenance Schedules already in the DB (list is empty) we simply start off with ID = 1
        return newID   
            
    def createUniqueMaintenanceReportID(self) -> int:
        """ Function loads all Maintenance Report from DB, finds the last assigned ID and adds one to it, creating a new ID, returns unique id int"""
        currentMaintenanceReport = self.DataLayerWrapper.loadMaintenanceReportLog()
        if len(currentMaintenanceReport) != 0:
            newID = currentMaintenanceReport[-1].maintenanceReportID + 1 # Since we never delete from the DB we can go to the last maintenance report in the list and find the ID of it and +1 to get a new unique ID
        else:
            newID = 1 # If there are no maintenance Reports already in the DB (list is empty) we simply start off with ID = 1
        return newID

    def createTempMaintenance(self) -> Maintenance:
        """ Function creates a temporary Maintenance Task based on user input for the user to fill out, it is assigned a unique INT ID, returns a temporary Maintenance Task """
        # Create a new maintenance
        tempMaintenanceID = self.createUniqueMaintenanceID() # Fetch a unique id for the maintenance
        temp_maintenance = Maintenance(ID=tempMaintenanceID) # Create a Maintenance with that unique ID, user inputs the rest
        return temp_maintenance

    def createTempMaintenanceSchedule(self) -> MaintenanceSchedule:
        """ Function creates a temporary Maintenance Schedule based on user input for the user to fill out, it is assigned a unique INT ID, returns a temporary Maintenance Schedule """
        # Create a temporary maintenance schedule
        tempMaintenanceScheduleID = self.createUniqueMaintenanceScheduleID() # Fetch a unique id for maintenance schedule
        temp_maintenanceSchedule = MaintenanceSchedule(ID=tempMaintenanceScheduleID) # Create a maintenance schedule with the unique id, user fills in the rest
        return temp_maintenanceSchedule
    
    def createTempMaintenanceReport(self) -> MaintenanceReport:
        """ Function creates a temporary Maintenance Report based on user input for the user to fill out, it is assigned a unique INT ID, returns a temporary Maintenance Report """
        # Crate a temporary maintenance Report
        tempMaintenanceReportID = self.createUniqueMaintenanceReportID() # Fetches unique id for maintenance report
        temp_maintenanceReport = MaintenanceReport(ID=tempMaintenanceReportID) # Create a maintenance report with the unique id, user inputs the rest
        return temp_maintenanceReport

    def validateMaintenanceTaskInput(self, input, count, temp_maintenanceTask) -> True:
        """ Function checks for each attribute in the Maintenance Task the user changes if it is of the desired format, returns True or raises ValuError"""
        # Validate the Maintenance Input
        datetime_format = "%d.%m.%Y.%H:%M" # We want the user to input something like 02.10.2024.12:30 which we then convert into datetime format.
        if self.Errors.checkNumber(count):
            count = int(count)
        if count == 1: # Prop ID
            self.Errors.checkNumber(input) # Check if the property ID is an input
            self.checkIfPropertyIDinDB(int(input)) # Check if we have the property ID in our DB, otherwise give error.. cant have maintenance on a property that does not exist
            temp_maintenanceTask.propertyID = int(input)
        elif count == 2: # Description
            self.Errors.checkEmpty(input)
            temp_maintenanceTask.description = input
        elif count == 3: # startDate
            conversion = self.Errors.checkErrorStartDate(input, datetime_format) ## must be a valid date
            temp_maintenanceTask.startDate = conversion
        elif count == 4: # endDate
            conversion = self.Errors.checkErrorEndDate(input, datetime_format, temp_maintenanceTask.startDate) # make sure end is not before start
            temp_maintenanceTask.endDate = conversion
        elif count == 5: # statusMaintenance
            self.Errors.checkErrorStatusMaintenance(input)
            temp_maintenanceTask.statusMaintenance = input
        elif count == 6: # Priority
            self.Errors.checkErrorPriority(input)
            temp_maintenanceTask.priority = input
        elif count == 7: # recurring
            self.Errors.errorCheckBoolean(input)
            temp_maintenanceTask.recurring = input
        
        return True
    
    def canEditMaintenanceTask(self, maintenanceTask) -> True:
        """ Checks if maintenance is closed so you can edit it, returns True or raises ValueError"""
        if maintenanceTask.statusMaintenance.lower() == "closed":
            raise ValueError("Can not edit a closed Maintenance Task")
        return True

    def getMaintenanceTaskByID(self, ID, destination = None) -> Maintenance:
        """ Function loads all Maintenances and tries to find the specified employee by ID in the DB, returns Employee or raises ValueError"""
        # Check for maintenance Task by maintenance Task ID or name
        if self.Errors.checkNumber(ID): # Checks if id is a number
            maintenanceLog = self.getMaintenanceData(destination) # Load all maintenances and mabye depending on destination aswell
            index_to_update = -1
            for index, maintenance in enumerate(maintenanceLog):
                if maintenance.maintenanceID == int(ID): # Find the index of the maintenance specified in the list of maintenances
                    index_to_update = index
            if index_to_update != -1:
                maintenance_found = maintenanceLog[index_to_update] # Extract the maintenance from the list
                return maintenance_found
            else:
                raise ValueError("No Maintenance Task By that ID")
            
    def getMaintenanceScheduleByID(self, ID) -> MaintenanceSchedule:
        """ Function loads all Maintenance Schedules and tries to find the specified employee by ID in the DB, returns Employee or raises ValueError"""
        if self.Errors.checkNumber(ID): # Checks if id is a number
            maintenanceScheduleLog = self.DataLayerWrapper.loadMaintenanceScheduleLog() # Loads all the maintenance schedules
            index_to_update = -1
            for index, maintenanceSchedule in enumerate(maintenanceScheduleLog):
                if maintenanceSchedule.maintenanceScheduleID == int(ID): # Find the index of the maintenance schedules that is specified in the list of maintenance schedules
                    index_to_update = index
            if index_to_update != -1:
                maintenanceSchedule_found = maintenanceScheduleLog[index_to_update] # Extract the maintenance schedule
                return maintenanceSchedule_found
            else:
                raise ValueError("No Maintenance Schedule By that ID")
            
    def getMaintenanceReportByID(self, ID) -> MaintenanceReport:
        """ Function loads all Maintenance Reports and tries to find the specified employee by ID in the DB, returns Employee or raises ValueError"""
        if self.Errors.checkNumber(ID): # Checks if id is a number
            maintenanceReportLog = self.DataLayerWrapper.loadMaintenanceReportLog() # Loads all the Maintenance Reports
            index_to_update = -1
            for index, report in enumerate(maintenanceReportLog):
                if report.maintenanceReportID == int(ID): # Find the index of the maintenance reports that is specified in the list of maintenance reports
                    index_to_update = index
            if index_to_update != -1:
                maintenanceReport_found = maintenanceReportLog[index_to_update] # Extract the maintenance report
                return maintenanceReport_found
            else:
                raise ValueError("No Maintenance Report By that ID")

    def checkIfPropertyIDinDB(self, ID) -> True:
        """ Function checks if the specified property is in the properties DB, returns True or raises ValueError"""
        properties = self.DataLayerWrapper.loadPropertiesLog() # Load all properties
        for property in properties:
            if property.propertyID == ID: # Find the specified property in properties DB
                return True
        raise ValueError("That Property does not exist")

    def validateMaintenanceScheduleInput(self, input, count, temp_maintenanceSchedule) -> True:
        """ Function checks for each attribute in the Maintenance Schedule the user changes if it is of the desired format, returns True or raises ValuError"""
        # This function doubles as a validation for creating maintenance schedules and updating them, when editing maintenance schedules instead of count we get the number of the attribute the user wants to change, thats why we need to change it into an integer even though count would usually be an integer
        if self.Errors.checkNumber(count):
            count = int(count)
        datetime_format = "%d.%m.%Y.%H:%M" # We want the user to input something like 02.10.2024.12:30 which we then convert into datetime format.
        if count == 1:
            self.Errors.checkNumber(input) # Check if the maintenance ID is an int
            self.checkIfMaintenanceIDinDB(int(input)) # Check if we have that maintenance in our DB, cant schedule a maintenance that does not exist..
            self.checkIfMaintenanceIsClosed(int(input)) # Check if the Maintenance we are trying to schedule is closed, we cant create a schedule on a closed maintenance
            self.checkIfMaintenanceIsRecurring(int(input), True) # Check if its recurring using the schedule Flag to get the correct Error
            temp_maintenanceSchedule.maintenanceID = int(input)
        elif count == 2:
            self.Errors.checkErrorTaskType(input)
            temp_maintenanceSchedule.taskType = input
        elif count == 3:
            self.Errors.checkErrorFrequency(input)
            temp_maintenanceSchedule.frequency = input
        elif count == 4: # Start Date
            conversion = self.Errors.checkErrorStartDate(input, datetime_format) ## must be a valid date
            maintenance_start_date = self.getStartDateMaintenanceTask(temp_maintenanceSchedule.maintenanceID) # And we need the start date of the referenced maintenance
            if maintenance_start_date > conversion: # The schedule start date should not be before the maintenance that is reference starts
                raise ValueError(f"Start Date of Scheduled Maintenance can not be before the Maintenance Task Start Date {maintenance_start_date}")
            temp_maintenanceSchedule.startDate = conversion
        return True

    def canEditMaintenanceSchedule(self, maintenanceSchedule) -> True:
        """ Function finds the maintenance associated with the schedule and sees if it is closed, if so raise ValueError else return True"""
        maintenancelog = self.DataLayerWrapper.loadMaintenanceLog() # Loads all mmaintenances
        for maintenance in maintenancelog:
            # We reference the maintenanceID in the maintenance schedule so we find that maintenance via the reference and then check if its closed or not
            if maintenance.maintenanceID == maintenanceSchedule.maintenanceID and maintenance.statusMaintenance.lower() == "closed":
                raise ValueError("Can not edit a Schedule for a maintenance Task that has been closed")
        return True

    def getStartDateMaintenanceTask(self, maintenanceID) -> datetime:
        """ Function loads all maintenances, finds the specified maintenance and returns the start date or raises ValueError if no maintenance is found"""
        maintenances = self.DataLayerWrapper.loadMaintenanceLog() # Load all the maintenances
        for maint in maintenances: 
            if maint.maintenanceID == maintenanceID: # Find the maintenance specified in the DB
                return maint.startDate # Return the start date of that maintenance
        raise ValueError("No maintenance by that ID")

    def checkIfMaintenanceIDinDB(self, ID) -> Maintenance:
        """ Function checks if the specified Maintenance is in the Maintenance DB, returns Maintenance or raises ValueError"""
        maintenances = self.DataLayerWrapper.loadMaintenanceLog() # Load the maintenance log
        for maint in maintenances:
            if maint.maintenanceID == ID: # find the maintenance specified in the DB
                return maint # and return it
        raise ValueError("There is no Maintenance Task by that ID")
    
    def checkIfMaintenanceIsClosed(self, ID, schedule = None) -> True:
        """ This function checks if a Maintenance Task that we know we have in our DB is closed or still ongoing, returns true if maintenance is not closed otherwise raises KeyError """
        # Should not be called in isolation, needs prerequisite functionality (called in validation functions)
        task = self.getMaintenanceTaskByID(ID) # We know that if we call this function that the ID is already in the DB no need to check
        if task.statusMaintenance.lower() == "closed": # Checks if the status we got from id is closed or not
            if schedule:
                raise KeyError("You can not create a Maintenance Schedule for a closed Maintenance Task")
            else:
                raise KeyError("You can not create a Maintenance Report on a closed Maintenance Task")
        return True
    
    def checkIfEmployeeIDinDB(self, ID) -> True:
        """ Function checks if the specified employee is in the employees DB, returns True or raises ValueError"""
        employeeLog = self.DataLayerWrapper.loadEmployeeLog() # Loads all the employees from the DB
        for employee in employeeLog:
            if employee.type == "General" and employee.employeeID == ID: # Check the employees list for a General employee not a manager on a specific id
                return True
        raise ValueError("No General Employee by that ID")
    
    def checkIfContractorIDinDB(self, ID) -> True:
        """ Function checks if the specified contractor is in the employeess DB, returns True or raises ValueError"""
        employeeLog = self.DataLayerWrapper.loadEmployeeLog() # Loads all the employees from the DB
        for employee in employeeLog:
            if employee.type == "Contractor" and employee.employeeID == ID: # check the employees for a contractor type and a specific id that was passed in as an argument
                return True
        raise ValueError("No Contractor by that ID")

    def validateMaintenanceReportEmployeeInput(self, input, count, temp_maintenanceReport) -> True:
        """ Function checks for each attribute in the Maintenance Report the user changes as an employee if it is of the desired format, returns True or raises ValuError"""
        # Validate the MaintenanceReport inputs in creating the temp maintenance report
        # For employees creating the maintenance report we need them to input the maintenance Task ID, their ID, material costs and if its ready to close or not
        if self.Errors.checkNumber(count):
            count = int(count)
        # This function doubles as a validation for creating maintenance report and updating them, when editing maintenance report instead of count we get the number of the attribute the user wants to change, thats why we need to change it into an integer even though count would usually be an integer
        if count == 1: # Maintenance ID
            self.Errors.checkNumber(input)
            maintenanceID = int(input)
            if self.checkIfMaintenanceIDinDB(maintenanceID): # Check if the Maintenance Task exists
                if self.checkIfMaintenanceIsClosed(maintenanceID): # Can only create a report on an active maintenance
                    # We also need to check if a report already exists for that maintenance, if it exists and its not recurring we can not create another maintenance report on that task, if its recurring we can
                    if self.checkIfMaintenanceReportExists(maintenanceID):
                        self.checkIfMaintenanceIsRecurring(maintenanceID) # If it passes we continue if not we abort the creating the maintenance report
                    temp_maintenanceReport.maintenanceID = maintenanceID
        elif count == 2: # Adding the employee ID
            self.checkIfEmployeeIDinDB(int(input))
            temp_maintenanceReport.employeeID = int(input)
        elif count == 3: # Material Cost
            self.Errors.checkNumber(input)
            temp_maintenanceReport.materialCost = input
        return True
    
    def checkIfMaintenanceReportExists(self, maintenanceID) -> True:
        """ Function takes in a Maintenance ID, checks if a maintenance Report has been made on that specific Maintenance Task, returns True if it has, else False"""
        maintenanceReportLog = self.DataLayerWrapper.loadMaintenanceReportLog()
        # Maintenances are referenced on reports so we need to get the data from the maintenance reports not the maintenanace class since the reference is not the other way around
        for report in maintenanceReportLog: # Go through the maintenance reports to check if there is a report on that maintenance 
            if report.maintenanceID == maintenanceID:
                # Report found
                return True
        return False

    def checkIfMaintenanceIsRecurring(self, maintenanceID, schedule = None) -> True:
        """ Function takes in maintenance ID, checks if that maintenance is recurring, if it is return True else raise KeyError """
        maintenanceLog = self.DataLayerWrapper.loadMaintenanceLog()
        # Function should only be used in the validate functions, needs prerequisite functions to work properly
        # At this point we know the maintenance exists and we know its not closed and we know a maintenace report exists for this maintenance so we just need to check if its recurring or not
        for maint in maintenanceLog:
            if maint.maintenanceID == maintenanceID: # Find the maintenance specified in the DB
                if maint.recurring.lower() == "true": # Check if that maintenance is recurring or not
                    return True
        if schedule: # For duplicate use of the function one for maintenance schedule validation
            raise KeyError("You can not Schedule a Maintenance Task that is not recurring")
        else: # one for maintenance report validation
            raise KeyError("You can not create duplicate Maintenance Reports on Maintenance Tasks that are not recurring")

    def validateMaintenanceReportContractorInput(self, input, count, temp_maintenanceReport) -> True:
        """ Function checks for each attribute in the Maintenance Report the user changes as a contractor if it is of the desired format, returns True or raises ValuError"""
        # Validate the MaintenanceReport inputs in creating the temp maintenance report
        # User inputs maintenance ID, material Cost, contractor ID, contractor Cost and ready to close
        if self.Errors.checkNumber(count):
            count = int(count)
        # This function doubles as a validation for creating reports and updating them, when editing reports instead of count we get the number of the attribute the user wants to change, thats why we need to change it into an integer even though count would usually be an integer
        if count == 1: # Adding the maintenanceID
            self.Errors.checkNumber(input)
            maintenanceID = int(input)
            if self.checkIfMaintenanceIDinDB(maintenanceID): # Check if the Maintenance Task exists
                if self.checkIfMaintenanceIsClosed(maintenanceID): # Can only create a report on an active maintenance
                    # We also need to check if a report already exists for that maintenance, if it exists and its not recurring we can not create another maintenance report on that task, if its recurring we can
                    if self.checkIfMaintenanceReportExists(maintenanceID):
                        self.checkIfMaintenanceIsRecurring(maintenanceID) # If it passes we continue if not we abort the creating the maintenance report
                    temp_maintenanceReport.maintenanceID = maintenanceID
        elif count == 2: # Material Cost
            self.Errors.checkNumber(input)
            temp_maintenanceReport.materialCost = input
        elif count == 3: # Adding the Contractor ID
            self.checkIfContractorIDinDB(int(input))
            temp_maintenanceReport.contractorID = int(input)
        elif count == 4: # Adding the Contractor Cost
            self.Errors.checkErrorContractorCost(input)
            temp_maintenanceReport.contractorCost = input
        return True

    def filterMaintenanceTasksDates(self, tasks, startDate, endDate) -> list[Maintenance]:
        """ Takes in a list of maintenance tasks and filteres them based on a specified start and end date"""
        # First check if end and start date are correctly formatted
        # Then filter after converting to datetime
        datetime_format = "%d.%m.%Y.%H:%M" # We want the user to input something like 02.10.2024.12:30 which we then convert into datetime format.
        startDate_converted = self.Errors.checkErrorStartDate(startDate, datetime_format) ## must be a valid date
        endDate_converted =  self.Errors.checkErrorEndDate(endDate, datetime_format, startDate_converted) ## must be a valid date
        # when error checking is done we know that both dates are valid and the end date is not before the start date
        filtered_tasks = []
        for task in tasks:
            if task.startDate >= startDate_converted and task.endDate <= endDate_converted: # We add the task to the list we will return if its in the specified time period
                filtered_tasks.append(task)

        if len(filtered_tasks) == 0: # If we dont find any maintenance tasks over the the specified time period the list will be empty so we raise an error
            raise ValueError("No Maintenance Tasks over that time period")

        return filtered_tasks

    def closeMaintenanceTask(self, maintenanceID, manager_feedback) -> True:
        """ Function takes in a maintenance ID, checks if it can be closed and closes it, returns True if possible, otherwise returns KeyError if you can not close it or ValueError if inputs are invalid"""
        # Close a finished maintenance task
        if self.Errors.checkNumber(maintenanceID): # If the ID is a valid number, ValueError if wrong
            maintenanceID = int(maintenanceID)
            self.Errors.checkEmpty(manager_feedback) # Check if the feedback is empty, we need some feedback, ValueError if wrong
            maintenance = self.checkIfMaintenanceIDinDB(maintenanceID) # If we have a maintenance by that ID, ValueError if wrong

            if maintenance.statusMaintenance.lower() == "closed": # Check if its already closed
                raise KeyError("You can not close an already closed Maintenance Task")
            
            maintenanceReportLog = self.DataLayerWrapper.loadMaintenanceReportLog() # Load all maintenance reports
            report_found = False # Flag to see if we found report, for raising KeyError
            # Now a Recurring maintenance Task can have multiple maintenance reports, if we want to close a recurring maintenance task we need to update all of the maintenance reports that were done on that maintenance task
            # So we create a list of the reports, there can be either one or multiple maintenance reports in this list
            maintenanceReports = [] 

            for maintReport in maintenanceReportLog: # we need to check if there already exists a maintenance report for this task, if so we know it can be closed
                if maintReport.maintenanceID == maintenanceID:
                    maintenanceReports.append(maintReport)
            
            if len(maintenanceReports) != 0:
                report_found = True # We found the report so we execute the rest of the logic and dont raise the KeyError
                maintenance.statusMaintenance = "Closed" # Mark maintenance Task status as closed
                self.DataLayerWrapper.updateMaintenance(maintenance) # Save new updated maintenance Task
                for report in maintenanceReports:
                    report.supervisorClosed = "True" # Mark Maintenance Report as closed by supervisor
                    report.supervisorFeedback = manager_feedback 
                    self.DataLayerWrapper.updateMaintenanceReport(report) # Save new updated maintenance Report

            # If report was not found that means we can not close it so raise KeyError
            if not report_found:
                raise KeyError("You can not close a Maintenance Task that an employee or a contractor has not created a Maintenance Report on")
                
        return True

    def updateMaintenance(self, maintenance) -> None:
        """ Function takes in a maintenance instance that already exists in our DB and we overwrite the old one"""
        self.DataLayerWrapper.updateMaintenance(maintenance)
        
    def updateMaintenanceSchedule(self, schedule) -> None:
        """ Function takes in a maintenance schedule instance that already exists in our DB and we overwrite the old one"""
        self.DataLayerWrapper.updateMaintenanceSchedule(schedule)

    def getMaintenanceData(self, destination = None) -> list[Maintenance]:
        """ Function Loads all the Maintenance Tasks from the maintenance DB and returns a list of those Maintenance Tasks"""
        maintenanceLog = self.DataLayerWrapper.loadMaintenanceLog()
        if destination:
            properties = self.DataLayerWrapper.loadPropertiesLog()
            dest_maintenances = []
            propIDs = []
            for prop in properties:
                if prop.location == destination.destinationID:
                    propIDs.append(prop.propertyID)
            for maint in maintenanceLog:
                if maint.maintenanceID in propIDs:
                    dest_maintenances.append(maint)
                return dest_maintenances
        return maintenanceLog
    
    def getMaintenanceScheduleData(self) -> list[MaintenanceSchedule]:
        """ Function Loads all the Maintenance Schedules from the maintenance DB and returns a list of those Maintenance Schedules"""
        maintenanceSchedules = self.DataLayerWrapper.loadMaintenanceScheduleLog()
        return maintenanceSchedules

    def getMaintenanceReportData(self) -> list[MaintenanceReport]:
        """ Function Loads all the Maintenance Reports from the maintenance DB and returns a list of those Maintenance Report"""
        maintenanceReports = self.DataLayerWrapper.loadMaintenanceReportLog()
        return maintenanceReports

    def createMaintenance(self, maintenance) -> None:
        """ Function takes in a Maintenance object and stores it in the Maintenance DB"""
        self.DataLayerWrapper.createMaintenance(maintenance)

    def createMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ Function takes in a Maintenance Schedule and stores it in the Maintenane Schedule DB"""
        self.DataLayerWrapper.createMaintenanceSchedule(maintenanceSchedule)

    def createMaintenanceReport(self, maintenanceReport) -> None:
        """ Function takes in a Maintenance Report and stores it in the Maintenance Report DB"""
        self.DataLayerWrapper.createMaintenanceReport(maintenanceReport)

    def getReadyToBeClosedMaintenanceTasks(self, destination = None) -> list[Maintenance]:
        """ Function loads all maintenance reports finds all the maintenance ID's from them and returns the maintenance tasks that are ready to be closed via closing the maintenance report"""
        # Load the data from the DB's
        reportslog = self.DataLayerWrapper.loadMaintenanceReportLog()
        maintenances = self.getMaintenanceData(destination)

        maintenancesInReportsID = []
        readyToBeClosedTasks = []
        # First find all the maintenance ID's that are referenced in the reports
        for report in reportslog:
            maintenancesInReportsID.append(report.maintenanceID)
        # Then add all the maintenance's that have reports on them to the list of maintenances ready to be closed
        for maintenance in maintenances: # Check if maintenance has a report on it and that its not already closed
            if maintenance.maintenanceID in maintenancesInReportsID:
                if maintenance.statusMaintenance.lower() == "ongoing":
                    readyToBeClosedTasks.append(maintenance)
        # If there no maintenance reports have been made on the open maintenance tasks then there is nothing to close
        if len(readyToBeClosedTasks) == 0:
            raise ValueError("No Maintenance Reports have been made on open Maintenances. Nothing to close")

        # Return all the maintenances that have reports on them, (meaning they are ready to be closed via closing the report)
        return readyToBeClosedTasks

        
