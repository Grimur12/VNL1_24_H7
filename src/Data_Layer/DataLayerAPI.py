from EmployeesDBLogic import EmployeesDBLogic
from MaintenanceDBLogic import MaintenanceDBLogic
from PropertiesDBLogic import PropertiesDBLogic

class DataLayerAPI:
    def __init__(self):
        pass

    def addEmployee(self, params) -> None:
        EmployeesDBLogic.createEmployee(params)

    def loadEmployeeLog(self) -> None:
        EmployeesDBLogic.loadEmployeeLog()

    def updateEmployee(self, params) -> None:
        EmployeesDBLogic.updateEmployee(params)

    def removeEmployee(self, ID) -> None:
        EmployeesDBLogic.removeEmployee(ID)

    def propagateEmployeeData(self) -> None:
        return EmployeesDBLogic.propagateData()
    
    def loadPropertiesLog(self) -> None:
        PropertiesDBLogic.loadPropertiesLog()

    def createProperty(self, params) -> None:
        PropertiesDBLogic.createProperty(params)

    def removeProperty(self, ID) -> None:
        PropertiesDBLogic.removeProperty(ID)

    def updateProperty(self, params) -> None:
        PropertiesDBLogic.updateProperty(params)
    
    def propagatePropertyData(self) -> list:
        return PropertiesDBLogic.propagateData()

    def loadMaintenanceLog(self) -> None:
        MaintenanceDBLogic.loadMaintenanceLog()

    def loadMaintenanceSchedule(self) -> None:
        MaintenanceDBLogic.loadMaintenanceSchedule()
        
    def updateMaintenanceStatus(self, params) -> None:
        MaintenanceDBLogic.updateMaintenanceStatus(params)

    def updateMaintenanceSchedule(self, params) -> None:
        MaintenanceDBLogic.updateMaintenanceSchedule(params)

    def createMaintenanceSchedule(self, params) -> None:
        MaintenanceDBLogic.createMaintenanceSchedule(params)

    def createMaintenance(self, params) -> None:
        MaintenanceDBLogic.createMaintenance(params)

    def removeMaintenance(self, ID) -> None:
        MaintenanceDBLogic.removeMaintenance(ID)

    def removeMaintenanceSchedule(self, ID) -> None:
        MaintenanceDBLogic.removeMaintenanceSchedule(ID)

    def propagateMaintenanceData(self) -> list:
        return MaintenanceDBLogic.propagateMaintenanceData()

    def propagateMaintenanceScheduleData(self) -> list:
        return MaintenanceDBLogic.propagateMaintenanceScheduleData()


