from .EmployeesDBLogic import EmployeesDBLogic
from .MaintenanceDBLogic import MaintenanceDBLogic
from .PropertiesDBLogic import PropertiesDBLogic

class DataLayerAPI:
    def __init__(self):
        self.employeeDB = EmployeesDBLogic()
        self.maintenanceDB = MaintenanceDBLogic()
        self.propertyDB = PropertiesDBLogic()

    def createEmployee(self, employee) -> None:
        self.employeeDB.createEmployee(employee)

    def createContractor(self, contractor) -> None:
        self.employeeDB.createContractor(contractor)

    def loadEmployeeLog(self) -> list:
        employeeLog = self.employeeDB.loadEmployeeLog()
        return employeeLog

    def updateEmployee(self, employee) -> None:
        self.employeeDB.updateEmployee(employee)

    
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