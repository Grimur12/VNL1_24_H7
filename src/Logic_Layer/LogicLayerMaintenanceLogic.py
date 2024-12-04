#This is our Maintenance Logic 

class LogicLayerMaintenanceLogic:
    def __init__(self):
        self.maintenance = []

    def createMaintenance(self, property_ID, description, priority, deadline):
        task = {
            
        }
        self.maintenance.append(task)
        return f" Task {task['id']} has been created now"

    def closeMaintenanceReport(self):
        pass

    def updateMaintenanceStatus(self):
        pass

    def filterMaintenance(self):
        pass

    def getMaintenanceData(self):
        return self.maintenance
    
    def editMaintenanceSchedule(self):
        pass


    #check errors
    def checkMaintenanceErrors(self):
        pass