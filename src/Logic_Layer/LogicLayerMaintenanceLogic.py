from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Workers import *
from .ErrorCheckers import ErrorCheckers


class LogicLayerMaintenanceLogic:
    def __init__(self):
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()
        self.tempmaintenance = None

    def createUniqueID(self):
        currentMaintenance = self.DataLayerWrapper.loadMaintenanceLog()
        if len(currentMaintenance) != 0:
            newID = currentMaintenance[-1].maintenanceID + 1 # Assign new maintenance to a new ID
        else:
            newID = 1
        return newID

    #create a new maintenance
    def createTemp_Maintenance(self):


    #close a finished maintenance report
    def closeMaintenanceReport(self):
        pass

    #update maintenance status
    def updateMaintenanceStatus(self):
        pass

    #get maintenance data
    def getMaintenanceData(self):
        return self.maintenance
    
    #edit maintenance schedule
    def editMaintenanceSchedule(self):
        pass





    #check errors
    def checkMaintenanceErrors(self):
        pass


    # #filter maintenance by priority
    # def filterMaintenance(self):
    #     pass