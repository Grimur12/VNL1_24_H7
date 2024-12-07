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
                maintenance = maintenanceLog[index_to_update]
                return maintenance
            else:
                raise ValueError("No Property By that ID")
            
    def getMaintenanceScheduleByID(self, ID):
        if self.Errors.checkNumber(ID):
            maintenanceScheduleLog = self.DataLayerWrapper.loadMaintenanceScheduleLog()
            index_to_update = -1
            for index, maintenanceSchedule in enumerate(maintenanceScheduleLog):
                if maintenanceSchedule.maintenanceScheduleID == int(ID):
                    index_to_update = index
            if index_to_update != -1:
                maintenanceSchedule = maintenanceScheduleLog[index_to_update]
                return maintenanceSchedule
            else:
                raise ValueError("No Property By that ID")

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
        raise ValueError("You can not create a maintenance schedule for a maintenance task that does not exist")

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
    
    def editMaintenanceData(self):
    # Edit maintenance schedule
        pass

    def editMaintenanceSchedule(self):
        pass
    
    def createMaintenance(self, maintenance):
        self.DataLayerWrapper.createMaintenance(maintenance)

    def createMaintenanceSchedule(self, maintenanceSchedule):
        self.DataLayerWrapper.createMaintenanceSchedule(maintenanceSchedule)
