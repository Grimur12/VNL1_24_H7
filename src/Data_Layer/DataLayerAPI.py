from .EmployeesDBLogic import EmployeesDBLogic
from .MaintenanceDBLogic import MaintenanceDBLogic
from .PropertiesDBLogic import PropertiesDBLogic
from .DestinationDBLogic import DestinationDBLogic
from Models.Maintenance import Maintenance
from Models.MaintenanceReport import MaintenanceReport
from Models.MaintenanceSchedule import MaintenanceSchedule
from Models.Destination import Destination
from Models.Property import Property
from Models.Workers import *

class DataLayerAPI:
    def __init__(self):
        """ Holds a reference to our Database Logic"""
        self.employeeDB = EmployeesDBLogic()
        self.maintenanceDB = MaintenanceDBLogic()
        self.propertyDB = PropertiesDBLogic()
        self.destinationDB = DestinationDBLogic()

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
    def loadPropertiesLog(self) -> list[Property]:
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
    def loadMaintenanceLog(self) -> list[Maintenance]:
        """ Loads all Maintenances from json database, create the classes again, store in a list to return"""
        maintenances = self.maintenanceDB.loadMaintenanceLog()
        return maintenances

    def loadMaintenanceScheduleLog(self) -> list[MaintenanceSchedule]:
        """ Loads all Maintenance Schedules from json database, create the classes again, store in a list to return"""
        maintenanceSchedules = self.maintenanceDB.loadMaintenanceScheduleLog()
        return maintenanceSchedules
    
    def loadMaintenanceReportLog(self) -> list[MaintenanceReport]:
        """ Loads all Maintenance Reports from json database, create the classes again, store in a list to return"""
        maintenanceReports = self.maintenanceDB.loadMaintenanceReportLog()
        return maintenanceReports
        
    def updateMaintenance(self, maintenance) -> None:
        """ Function takes in a maintenance with updated attributes, saves it in the maintenance DB"""
        self.maintenanceDB.updateMaintenance(maintenance)

    def updateMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ ... IS this needed ?"""
        self.maintenanceDB.updateMaintenanceSchedule(maintenanceSchedule)

    def updateMaintenanceReport(self, maintenanceReport) -> None:
        """ Function takes in a maintenance Report with updated attributes, saves it in the maintenance DB?"""
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

    # Destination DB Logic
    def loadDestinationsLog(self) -> list[Destination]:
        """ Loads all properties from json database, creates the classes again, stores in a list to return"""
        destinations = self.destinationDB.loadDestinationsLog()
        return destinations

    def updateDestination(self, updated_destination) -> None:
        """ This function takes in a property instance, finds old version of it by checking the ID, overwrites it and saves the properties again in the json DB"""
        self.destinationDB.updateDestination(updated_destination)