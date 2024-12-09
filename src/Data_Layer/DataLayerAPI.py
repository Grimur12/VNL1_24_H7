from .EmployeesDBLogic import EmployeesDBLogic
from .MaintenanceDBLogic import MaintenanceDBLogic
from .PropertiesDBLogic import PropertiesDBLogic

class DataLayerAPI:
    def __init__(self):
        """ Holds a reference to our Database Logic"""
        self.employeeDB = EmployeesDBLogic()
        self.maintenanceDB = MaintenanceDBLogic()
        self.propertyDB = PropertiesDBLogic()

    # Employee DB Logic
    def createEmployee(self, employee) -> None:
        """ Takes in object employee and stores it in our Employees json DB"""
        self.employeeDB.createEmployee(employee)

    def createContractor(self, contractor) -> None:
        """ Takes in object contractor and stores it in our Employees json DB"""
        self.employeeDB.createContractor(contractor)

    def loadEmployeeLog(self) -> list:
        """ Loads all employees from json database, create the classes again, store in a list to return"""
        employeeLog = self.employeeDB.loadEmployeeLog()
        return employeeLog

    def updateEmployee(self, employee) -> None:
        """ Takes in an object of employee and stores it in our Employee DB"""
        self.employeeDB.updateEmployee(employee)

    # Property DB Logic   
    def loadPropertiesLog(self) -> list:
        """ Loads all properties from json database, create the classes again, store in a list to return"""
        propertyLog = self.propertyDB.loadPropertiesLog()
        return propertyLog

    def createProperty(self, property) -> None:
        """ Takes in object Property and stores it in our Property json DB"""
        self.propertyDB.createProperty(property)

    def updateProperty(self, property) -> None:
        """ Takes in object Property and stores it in our Property json DB"""
        self.propertyDB.updateProperty(property)
        
    # Maintenance Report, Maintenance Schedule and Maintenance Task DB Logic
    def loadMaintenanceLog(self) -> list:
        """ Loads all Maintenances from json database, create the classes again, store in a list to return"""
        maintenances = self.maintenanceDB.loadMaintenanceLog()
        return maintenances

    def loadMaintenanceScheduleLog(self) -> list:
        """ Loads all Maintenance Schedules from json database, create the classes again, store in a list to return"""
        maintenanceSchedules = self.maintenanceDB.loadMaintenanceScheduleLog()
        return maintenanceSchedules
    
    def loadMaintenanceReportLog(self) -> list:
        """ Loads all Maintenance Reports from json database, create the classes again, store in a list to return"""
        maintenanceReports = self.maintenanceDB.loadMaintenanceReportLog()
        return maintenanceReports
        
    def updateMaintenanceStatus(self, maintenance) -> None:
        """ ... IS this needed ?"""
        self.maintenanceDB.updateMaintenanceStatus(maintenance)

    def updateMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ ... IS this needed ?"""
        self.maintenanceDB.updateMaintenanceSchedule(maintenanceSchedule)

    def updateMaintenanceReport(self, maintenanceReport) -> None:
        """ ... IS this needed ?"""
        self.maintenanceDB.updateMaintenanceReport(maintenanceReport)

    def createMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ Takes in object maintenanceSchedule and stores it in our maintenance Schedule json DB"""
        self.maintenanceDB.createMaintenanceSchedule(maintenanceSchedule)

    def createMaintenance(self, maintenance) -> None:
        """ Takes in object Maintenance and stores it in our Maintenance json DB"""
        self.maintenanceDB.createMaintenance(maintenance)

    def createMaintenanceReport(self, maintenanceReport) -> None:
        """ Takes in object Maintenance Report and stores it in our Maintenance Report json DB"""
        self.maintenanceDB.createMaintenanceReport(maintenanceReport)