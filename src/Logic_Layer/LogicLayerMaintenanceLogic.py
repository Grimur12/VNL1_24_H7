from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Workers import *
from .ErrorCheckers import ErrorCheckers


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
        currentMaintenance = self.DataLayerWrapper.loadMaintenanceScheduleLog()
        if len(currentMaintenance) != 0:
            newID = currentMaintenance[-1].maintenanceID + 1 # Assign new maintenance to a new ID
        else:
            newID = 1
        return newID

    def createTempMaintenance(self):
    # Create a new maintenance
        pass

    def createTempMaintenanceSchedule(self):
    # Create a temporary maintenance schedule
        pass

    def validateMaintenanceInput(self):
    # Validate the Maintenance Input
        pass

    def validateMaintenanceScheduleInput(self):
    # Validate the Maintenance Schedule Input
        pass

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
        maintenanceSchedules = self.DataLayerWrapper.loadMaintenanceLog()
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
