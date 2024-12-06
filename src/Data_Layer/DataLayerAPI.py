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
        propertyLog = self.propertyDB.loadPropertiesLog()
        return propertyLog

    def createProperty(self, property) -> None:
        self.propertyDB.createProperty(property)

    def updateProperty(self, property) -> None:
        self.propertyDB.updateProperty(property)

    def loadMaintenanceLog(self) -> list:
        maintenances = self.maintenanceDB.loadMaintenanceLog()
        return maintenances

    def loadMaintenanceScheduleLog(self) -> list:
        maintenanceSchedules = self.maintenanceDB.loadMaintenanceScheduleLog()
        return maintenanceSchedules
        
    def updateMaintenanceStatus(self, maintenance) -> None:
        self.maintenanceDB.updateMaintenanceStatus(maintenance)

    def updateMaintenanceSchedule(self, maintenanceSchedule) -> None:
        self.maintenanceDB.updateMaintenanceSchedule(maintenanceSchedule)

    def createMaintenanceSchedule(self, maintenanceSchedule) -> None:
        self.maintenanceDB.createMaintenanceSchedule(maintenanceSchedule)

    def createMaintenance(self, maintenance) -> None:
        self.maintenanceDB.createMaintenance(maintenance)