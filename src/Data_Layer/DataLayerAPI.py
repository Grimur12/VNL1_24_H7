from .EmployeesDBLogic import EmployeesDBLogic
from .MaintenanceDBLogic import MaintenanceDBLogic
from .PropertiesDBLogic import PropertiesDBLogic

class DataLayerAPI:
    def __init__(self):
        self.employeeDB = EmployeesDBLogic()
        self.maintenanceDB = MaintenanceDBLogic()
        self.propertyDB = PropertiesDBLogic()

    def createEmployee(self, params) -> None:
        self.employeeDB.createEmployee(params)

    def createContractor(self, params) -> None:
        self.employeeDB.createContractor(params)

    def loadEmployeeLog(self) -> list:
        employeeLog = self.employeeDB.loadEmployeeLog()
        return employeeLog

    def updateEmployee(self, params) -> None:
        self.employeeDB.updateEmployee(params)

    
    def loadPropertiesLog(self) -> list:
        return self.propertyDB.loadPropertiesLog()

    def createProperty(self, params) -> None:
        self.propertyDB.createProperty(params)


    def updateProperty(self, params) -> None:
        self.propertyDB.updateProperty(params)

    def loadMaintenanceLog(self) -> list:
        return self.maintenanceDB.loadMaintenanceLog()

    def loadMaintenanceSchedule(self) -> list:
        return self.maintenanceDB.loadMaintenanceSchedule()
        
    def updateMaintenanceStatus(self, params) -> None:
        self.maintenanceDB.updateMaintenanceStatus(params)

    def updateMaintenanceSchedule(self, params) -> None:
        self.maintenanceDB.updateMaintenanceSchedule(params)

    def createMaintenanceSchedule(self, params) -> None:
        self.maintenanceDB.createMaintenanceSchedule(params)

    def createMaintenance(self, params) -> None:
        self.maintenanceDB.createMaintenance(params)

    def removeMaintenance(self, ID) -> None:
        self.maintenanceDB.removeMaintenance(ID)

    def removeMaintenanceSchedule(self, ID) -> None:
        self.maintenanceDB.removeMaintenanceSchedule(ID)