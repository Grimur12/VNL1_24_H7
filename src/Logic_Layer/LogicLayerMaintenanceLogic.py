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
        self.tempmaintenance = None

    def createUniqueMaintenanceID(self) -> int:
        """ Function loads all Maintenances from DB, finds the last assigned ID and adds one to it, creating a new ID, returns unique id int"""
        currentMaintenance = self.DataLayerWrapper.loadMaintenanceLog()
        if len(currentMaintenance) != 0:
            newID = currentMaintenance[-1].maintenanceID + 1 # Assign new maintenance to a new ID
        else:
            newID = 1
        return newID
    
    def createUniqueMaintenanceScheduleID(self) -> int:
        """ Function loads all Maintenance Schedules from DB, finds the last assigned ID and adds one to it, creating a new ID, returns unique id int"""
        currentMaintenanceSchedules = self.DataLayerWrapper.loadMaintenanceScheduleLog()
        if len(currentMaintenanceSchedules) != 0:
            newID = currentMaintenanceSchedules[-1].maintenanceScheduleID + 1 # Assign new maintenance to a new ID
        else:
            newID = 1  
        return newID   
            
    def createUniqueMaintenanceReportID(self) -> int:
        """ Function loads all Maintenance Report from DB, finds the last assigned ID and adds one to it, creating a new ID, returns unique id int"""
        currentMaintenanceReport = self.DataLayerWrapper.loadMaintenanceReportLog()
        if len(currentMaintenanceReport) != 0:
            newID = currentMaintenanceReport[-1].maintenanceReportID + 1 # Since we never delete from the DB we can go to the last maintenance report in the list and find the ID of it and +1 to get a new unique ID
        else:
            newID = 1 # If there are no maintenance Reports already in the DB we simply start off with ID = 1
        return newID

    def createTempMaintenance(self) -> Maintenance:
        """ Function creates a temporary Maintenance Task based on user input for the user to fill out, it is assigned a unique INT ID, returns a temporary Maintenance Task """
        # Create a new maintenance
        tempMaintenanceID = self.createUniqueMaintenanceID()
        temp_maintenance = Maintenance(ID=tempMaintenanceID)
        return temp_maintenance

    def createTempMaintenanceSchedule(self) -> MaintenanceSchedule:
        """ Function creates a temporary Maintenance Schedule based on user input for the user to fill out, it is assigned a unique INT ID, returns a temporary Maintenance Schedule """
        # Create a temporary maintenance schedule
        tempMaintenanceScheduleID = self.createUniqueMaintenanceScheduleID()
        temp_maintenanceSchedule = MaintenanceSchedule(ID=tempMaintenanceScheduleID)
        return temp_maintenanceSchedule
    
    def createTempMaintenanceReport(self) -> MaintenanceReport:
        """ Function creates a temporary Maintenance Report based on user input for the user to fill out, it is assigned a unique INT ID, returns a temporary Maintenance Report """
        # Crate a temporary maintenance Report
        tempMaintenanceReportID = self.createUniqueMaintenanceReportID()
        temp_maintenanceReport = MaintenanceReport(ID=tempMaintenanceReportID)
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
    
    def canEditMaintenanceTask(self, maintenanceTask):
        """ Checks if maintenance is closed so you can edit it, returns True or raises ValueError"""
        if maintenanceTask.statusMaintenance.lower() == "closed":
            raise ValueError("Can not edit a closed Maintenance Task")
        return True

    def getMaintenanceTaskByID(self, ID) -> Maintenance:
        """ Function loads all Maintenances and tries to find the specified employee by ID in the DB, returns Employee or raises ValueError"""
        # Check for maintenance Task by maintenance Task ID or name
        if self.Errors.checkNumber(ID):
            maintenanceLog = self.DataLayerWrapper.loadMaintenanceLog()
            index_to_update = -1
            for index, maintenance in enumerate(maintenanceLog):
                if maintenance.maintenanceID == int(ID):
                    index_to_update = index
            if index_to_update != -1:
                maintenance_found = maintenanceLog[index_to_update]
                return maintenance_found
            else:
                raise ValueError("No Maintenance Task By that ID")
            
    def getMaintenanceScheduleByID(self, ID) -> MaintenanceSchedule:
        """ Function loads all Maintenance Schedules and tries to find the specified employee by ID in the DB, returns Employee or raises ValueError"""
        if self.Errors.checkNumber(ID):
            maintenanceScheduleLog = self.DataLayerWrapper.loadMaintenanceScheduleLog()
            index_to_update = -1
            for index, maintenanceSchedule in enumerate(maintenanceScheduleLog):
                if maintenanceSchedule.maintenanceScheduleID == int(ID):
                    index_to_update = index
            if index_to_update != -1:
                maintenanceSchedule_found = maintenanceScheduleLog[index_to_update]
                return maintenanceSchedule_found
            else:
                raise ValueError("No Maintenance Schedule By that ID")
            
    def getMaintenanceReportByID(self, ID) -> MaintenanceReport:
        """ Function loads all Maintenance Reports and tries to find the specified employee by ID in the DB, returns Employee or raises ValueError"""
        if self.Errors.checkNumber(ID):
            maintenanceReportLog = self.DataLayerWrapper.loadMaintenanceReportLog()
            index_to_update = -1
            for index, report in enumerate(maintenanceReportLog):
                if report.maintenanceReportID == int(ID):
                    index_to_update = index
            if index_to_update != -1:
                maintenanceReport_found = maintenanceReportLog[index_to_update]
                return maintenanceReport_found
            else:
                raise ValueError("No Maintenance Report By that ID")

    def checkIfPropertyIDinDB(self, ID) -> True:
        """ Function checks if the specified property is in the properties DB, returns True or raises ValueError"""
        properties = self.DataLayerWrapper.loadPropertiesLog()
        for property in properties:
            if property.propertyID == ID:
                return True
        raise ValueError("That Property does not exist")

    def validateMaintenanceScheduleInput(self, input, count, temp_maintenanceSchedule) -> True:
        """ Function checks for each attribute in the Maintenance Schedule the user changes if it is of the desired format, returns True or raises ValuError"""
    # Validate the Maintenance Schedule Input
        if self.Errors.checkNumber(count):
            count = int(count)
        datetime_format = "%d.%m.%Y.%H:%M" # We want the user to input something like 02.10.2024.12:30 which we then convert into datetime format.
        if count == 1:
            self.Errors.checkNumber(input) # Check if the maintenance ID is an int
            self.checkIfMaintenanceIDinDB(int(input)) # Check if we have that maintenance in our DB, cant schedule a maintenance that does not exist..
            temp_maintenanceSchedule.maintenanceID = int(input)
        elif count == 2:
            self.Errors.checkErrorTaskType(input)
            temp_maintenanceSchedule.taskType = input
        elif count == 3:
            self.Errors.checkErrorFrequency(input)
            temp_maintenanceSchedule.frequency = input
        elif count == 4: # Start Date
            conversion = self.Errors.checkErrorStartDate(input, datetime_format) ## must be a valid date
            maintenance_start_date = self.getStartDateMaintenanceTask(temp_maintenanceSchedule.maintenanceID)
            if maintenance_start_date > conversion:
                raise ValueError(f"Start Date of Scheduled Maintenance can not be before the Maintenance Task Start Date {maintenance_start_date}")
            temp_maintenanceSchedule.startDate = conversion
        return True

    def getStartDateMaintenanceTask(self, maintenanceID):
        """ Function loads all maintenances, finds the specified maintenance and returns the start date or raises ValueError if no maintenance is found"""
        maintenances = self.DataLayerWrapper.loadMaintenanceLog()
        for maint in maintenances:
            if maint.maintenanceID == maintenanceID:
                return maint.startDate
        raise ValueError("No maintenance by that ID")

    def checkIfMaintenanceIDinDB(self, ID) -> Maintenance:
        """ Function checks if the specified Maintenance is in the Maintenance DB, returns Maintenance or raises ValueError"""
        maintenances = self.DataLayerWrapper.loadMaintenanceLog()
        for maint in maintenances:
            if maint.maintenanceID == ID:
                return maint
        raise ValueError("There is no Maintenance Task by that ID")
    
    def checkIfMaintenanceIsClosed(self, ID) -> True:
        """ This function checks if a Maintenance Task that we know we have in our DB is closed or still ongoing, returns true if maintenance is not closed otherwise raises KeyError """
        task = self.getMaintenanceTaskByID(ID) # We know that if we call this function that the ID is already in the DB no need to check
        if task.statusMaintenance.lower() == "closed":
            raise KeyError("You can not create a Maintenance Report on a closed Maintenance Task")
        return True
    
    def checkIfEmployeeIDinDB(self, ID) -> True:
        """ Function checks if the specified employee is in the employees DB, returns True or raises ValueError"""
        employeeLog = self.DataLayerWrapper.loadEmployeeLog()
        for employee in employeeLog:
            if employee.type == "General" and employee.employeeID == ID:
                return True
        raise ValueError("No General Employee by that ID")
    
    def checkIfContractorIDinDB(self, ID) -> True:
        """ Function checks if the specified contractor is in the employeess DB, returns True or raises ValueError"""
        employeeLog = self.DataLayerWrapper.loadEmployeeLog()
        for employee in employeeLog:
            if employee.type == "Contractor" and employee.employeeID == ID:
                return True
        raise ValueError("No Contractor by that ID")

    def validateMaintenanceReportEmployeeInput(self, input, count, temp_maintenanceReport) -> True:
        """ Function checks for each attribute in the Maintenance Report the user changes as an employee if it is of the desired format, returns True or raises ValuError"""
        # Validate the MaintenanceReport inputs in creating the temp maintenance report
        # For employees creating the maintenance report we need them to input the maintenance Task ID, their ID, material costs and if its ready to close or not
        if self.Errors.checkNumber(count):
            count = int(count)

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
        for report in maintenanceReportLog: # Go through the maintenance reports, check if there is a report on that maintenance 
            if report.maintenanceID == maintenanceID:
                # Report found
                return True
        return False

    def checkIfMaintenanceIsRecurring(self, maintenanceID) -> True:
        """ Function takes in maintenance ID, checks if that maintenance is recurring, if it is return True else raise KeyError """
        maintenanceLog = self.DataLayerWrapper.loadMaintenanceLog()
        # At this point we know the maintenance exists and we know its not closed and we know a maintenace report exists for this maintenance so we just need to check if its recurring or not
        for maint in maintenanceLog:
            if maint.maintenanceID == maintenanceID:
                if maint.recurring.lower() == "true":
                    return True
        raise KeyError("You can not create duplicate Maintenance Reports on Maintenance Tasks that are not recurring")

    def validateMaintenanceReportContractorInput(self, input, count, temp_maintenanceReport) -> True:
        """ Function checks for each attribute in the Maintenance Report the user changes as a contractor if it is of the desired format, returns True or raises ValuError"""
        # Validate the MaintenanceReport inputs in creating the temp maintenance report
        # User inputs maintenance ID, material Cost, contractor ID, contractor Cost and ready to close
        if self.Errors.checkNumber(count):
            count = int(count)

        if count == 1: # Adding the maintenanceID
            self.Errors.checkNumber(input)
            maintenanceID = int(input)
            if self.checkIfMaintenanceIDinDB(maintenanceID): # Check if the Maintenance Task exists
                if self.checkIfMaintenanceIsClosed(maintenanceID): # Can only create a report on an active maintenance
                    # We also need to check if a report already exists for that maintenance, if it exists and its not recurring we can not create another maintenance report on that task, if its recurring we can
                    if self.checkIfMaintenanceReportExists:
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
            if task.startDate >= startDate_converted and task.endDate <= endDate_converted:
                filtered_tasks.append(task)

        if len(filtered_tasks) == 0:
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
            
            maintenanceReportLog = self.DataLayerWrapper.loadMaintenanceReportLog()
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

    def updateMaintenance(self, maintenance):
        self.DataLayerWrapper.updateMaintenance(maintenance)
        

    def getMaintenanceData(self) -> list[Maintenance]:
        """ Function Loads all the Maintenance Tasks from the maintenance DB and returns a list of those Maintenance Tasks"""
    # Get maintenance data
        maintenanceLog = self.DataLayerWrapper.loadMaintenanceLog()
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