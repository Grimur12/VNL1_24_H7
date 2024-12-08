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

    def createUniqueMaintenanceID(self):
        currentMaintenance = self.DataLayerWrapper.loadMaintenanceLog()
        if len(currentMaintenance) != 0:
            newID = currentMaintenance[-1].maintenanceID + 1 # Assign new maintenance to a new ID
        else:
            newID = 1
        return newID
    
    def createUniqueMaintenanceScheduleID(self):
        currentMaintenanceSchedules = self.DataLayerWrapper.loadMaintenanceScheduleLog()
        if len(currentMaintenanceSchedules) != 0:
            newID = currentMaintenanceSchedules[-1].maintenanceScheduleID + 1 # Assign new maintenance to a new ID
        else:
            newID = 1
        return newID
    
    def createUniqueMaintenanceReportID(self):
        currentMaintenanceReport = self.DataLayerWrapper.loadMaintenanceReportLog()
        if len(currentMaintenanceReport) != 0:
            newID = currentMaintenanceReport[-1].maintenanceReportID + 1 # Since we never delete from the DB we can go to the last maintenance report in the list and find the ID of it and +1 to get a new unique ID
        else:
            newID = 1 # If there are no maintenance Reports already in the DB we simply start off with ID = 1
        return newID

    def createTempMaintenance(self):
    # Create a new maintenance
        tempMaintenanceID = self.createUniqueMaintenanceID()
        temp_maintenance = Maintenance(ID=tempMaintenanceID)
        return temp_maintenance

    def createTempMaintenanceSchedule(self):
    # Create a temporary maintenance schedule
        tempMaintenanceScheduleID = self.createUniqueMaintenanceScheduleID()
        temp_maintenanceSchedule = MaintenanceSchedule(ID=tempMaintenanceScheduleID)
        return temp_maintenanceSchedule
    
    def createTempMaintenanceReport(self):
        # Crate a temporary maintenance Report
        tempMaintenanceReportID = self.createUniqueMaintenanceReportID()
        temp_maintenanceReport = MaintenanceReport(ID=tempMaintenanceReportID)
        return temp_maintenanceReport

    def validateMaintenanceTaskInput(self, input, count, temp_maintenanceTask):
    # Validate the Maintenance Input
        datetime_format = "%d.%m.%Y.%H:%M" # We want the user to input something like 02.10.2024.12:30 which we then convert into datetime format.
        if self.Errors.checkNumber(count):
            count = int(count)

        if count == 1:
            self.Errors.checkNumber(input) # Check if the property ID is an input
            self.checkIfPropertyIDinDB(int(input)) # Check if we have the property ID in our DB, otherwise give error.. cant have maintenance on a property that does not exist
            temp_maintenanceTask.propertyID = int(input)
        elif count == 2:
            conversion = self.Errors.checkErrorStartDate(input, datetime_format) ## must be a valid date
            temp_maintenanceTask.startDate = conversion
        elif count == 3:
            conversion = self.Errors.checkErrorEndDate(input, datetime_format, temp_maintenanceTask.startDate) # make sure end is not before start
            temp_maintenanceTask.endDate = conversion
        elif count == 4:
            self.Errors.checkErrorStatusMaintenance(input)
            temp_maintenanceTask.statusMaintenance = input
        elif count == 5:
            self.Errors.checkErrorFeedback(input)
            temp_maintenanceTask.feedback = input
        elif count == 6:
            self.Errors.checkErrorPriority(input)
            temp_maintenanceTask.priority = input
        
        return True
    
    def getMaintenanceTaskByID(self, ID):
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
            
    def getMaintenanceScheduleByID(self, ID):
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
            
    def getMaintenanceReportByID(self, ID):
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

    def checkIfPropertyIDinDB(self, ID):
        properties = self.DataLayerWrapper.loadPropertiesLog()
        for property in properties:
            if property.propertyID == ID:
                return True
        raise ValueError("That Property does not exist")

    def validateMaintenanceScheduleInput(self, input, count, temp_maintenanceSchedule):
    # Validate the Maintenance Schedule Input
        if self.Errors.checkNumber(count):
            count = int(count)

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
        
        return True

    def checkIfMaintenanceIDinDB(self, ID):
        maintenances = self.DataLayerWrapper.loadMaintenanceLog()
        for maint in maintenances:
            if maint.maintenanceID == ID:
                return True
        raise ValueError("There is no Maintenance Task by that ID")
    
    def checkIfMaintenanceIsClosed(self, ID) -> bool:
        """ This function checks if a Maintenance Task that we know we have in our DB is closed or still ongoing """
        task = self.getMaintenanceTaskByID(ID) # We know that if we call this function that the ID is already in the DB no need to check
        if task.statusMaintenance.lower() == "closed":
            raise ValueError("You can not create a Maintenance Report on a closed Maintenance Task")
        return True
    
    def checkIfEmployeeIDinDB(self, ID):
        employeeLog = self.DataLayerWrapper.loadEmployeeLog()
        for employee in employeeLog:
            if employee.type == "General" and employee.employeeID == ID:
                return True
        raise ValueError("No General Employee by that ID")
    
    def checkIfContractorIDinDB(self, ID):
        employeeLog = self.DataLayerWrapper.loadEmployeeLog()
        for employee in employeeLog:
            if employee.type == "Contractor" and employee.employeeID == ID:
                return True
        raise ValueError("No Contractor by that ID")

    def validateMaintenanceReportEmployeeInput(self, input, count, temp_maintenanceReport):
        # Validate the MaintenanceReport inputs in creating the temp maintenance report
        if self.Errors.checkNumber(count):
            count = int(count)

        if count == 1:
            self.Errors.checkNumber(input)
            maintenanceID = int(input)
            if self.checkIfMaintenanceIDinDB(maintenanceID): # Check if the Maintenance Task exists
                if self.checkIfMaintenanceIsClosed(maintenanceID): # Can only create a report on an active maintenance
                    temp_maintenanceReport.maintenanceID = maintenanceID
        elif count == 2: # Adding the employee ID
            self.checkIfEmployeeIDinDB(int(input))
            temp_maintenanceReport.employeeID = int(input)
        return True
    
    def validateMaintenanceReportContractorInput(self, input, count, temp_maintenanceReport):
        # Validate the MaintenanceReport inputs in creating the temp maintenance report
        if self.Errors.checkNumber(count):
            count = int(count)

        if count == 1: # Adding the maintenanceID
            maintenanceID = int(input)
            self.checkIfMaintenanceIDinDB(maintenanceID) # Check if the Maintenance Task exists
            self.checkIfMaintenanceIsClosed(maintenanceID) # Can only create a report on an active maintenance
            temp_maintenanceReport.maintenanceID = maintenanceID
        elif count == 2: # Adding the Contractor ID
            self.checkIfContractorIDinDB(int(input))
            temp_maintenanceReport.contractorID = int(input)
        elif count == 3: # Adding the Contractor Cost
            self.Errors.checkErrorContractorCost(input)
            temp_maintenanceReport.contractorCost = input
        
        return True

    def filterMaintenanceTasksDates(self, tasks, startDate, endDate) -> list:
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
        return filtered_tasks


    def closeMaintenanceReport(self):
    # Close a finished maintenance report
        pass

    def updateMaintenanceStatus(self):
    # Update maintenance status
        pass

    def getMaintenanceData(self):
    # Get maintenance data
        maintenanceLog = self.DataLayerWrapper.loadMaintenanceLog()
        return maintenanceLog
    
    def getMaintenanceScheduleData(self):
        maintenanceSchedules = self.DataLayerWrapper.loadMaintenanceScheduleLog()
        return maintenanceSchedules

    def getMaintenanceReportData(self):
        maintenanceReports = self.DataLayerWrapper.loadMaintenanceReportLog()
        return maintenanceReports

    def editMaintenanceData(self):
    # Edit maintenance schedule
        pass

    def editMaintenanceSchedule(self):
        pass
    
    def createMaintenance(self, maintenance):
        self.DataLayerWrapper.createMaintenance(maintenance)

    def createMaintenanceSchedule(self, maintenanceSchedule):
        self.DataLayerWrapper.createMaintenanceSchedule(maintenanceSchedule)

    def createMaintenanceReport(self, maintenanceReport):
        self.DataLayerWrapper.createMaintenanceReport(maintenanceReport)