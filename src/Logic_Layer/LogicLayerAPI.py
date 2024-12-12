from .LogicLayerEmployeeLogic import LogicLayerEmployeeLogic
from .LogicLayerMaintenanceLogic import LogicLayerMaintenanceLogic
from .LogicLayerPropertyLogic import LogicLayerPropertyLogic
from Models.Workers import *
from Models.Maintenance import Maintenance
from Models.MaintenanceReport import MaintenanceReport
from Models.MaintenanceSchedule import MaintenanceSchedule
from Models.Property import Property
from Models.Destination import Destination

class LogicLayerAPI:
    def __init__(self):
        self.LogicLayerEmployeelogic = LogicLayerEmployeeLogic()
        self.LogicLayerMaintenancelogic = LogicLayerMaintenanceLogic()
        self.LogicLayerPropertyLogic = LogicLayerPropertyLogic()

    # here are functions of the Employee

    def createEmployee(self, employee) -> None:
        """ Function takes in an object Employee and saves it in the DB """
        self.LogicLayerEmployeelogic.createEmployee(employee)

    def getTempEmployee(self, type_of_employee) -> Employee:
        """ Function creates a unique ID for employees, creates an empty one, and returns it to be filled out by user"""
        return self.LogicLayerEmployeelogic.createTempEmployee(type_of_employee)

    def validateEmployeeInput(self, user_input, count, temp_employee) -> True:
        """ Function validates the input of the user when creating and editing employees, returns true or raises ValueError """
        return self.LogicLayerEmployeelogic.validateEmployeeInput(user_input, count, temp_employee)
    
    def getEmployeeData(self, destination = None) -> list[Employee]:
        """ Function gets all of the employees currently stored in the DB if they are of the type Manager or General """
        employeeLog = self.LogicLayerEmployeelogic.getEmployeeData(destination)
        return employeeLog
    
    def getContractorData(self, destination = None) -> list[Contractor]:
        """ Function gets all of the contractors currently stored in the employees DB """
        contractorLog = self.LogicLayerEmployeelogic.getContractorData(destination)
        return contractorLog

    def getEmployeebyID(self, ID, destination = None) -> Employee:
        """ Loads the entire employees DB and tries to find if the employee exists in it, raises ValueError if it does not exist """
        employee = self.LogicLayerEmployeelogic.getEmployeebyID(ID, destination)
        return employee

    def getContractorbyID(self, ID, destination = None) -> Contractor:
        """ Loads the entire employees DB and tries to find if the contractor exists in it, raises ValueError if it does not exist """
        contractor = self.LogicLayerEmployeelogic.getContractorbyID(ID, destination)
        return contractor
    
    def getTasksForContractorID(self, ID, destination = None) -> list[Maintenance]:
        """ Loads maintenance Tasks and maintenance Reports and sees which maintenance Tasks a specific contractor has worked on and returns a list of tasks, otherwise raises ValueError"""
        # Takes in contractor ID
        tasks = self.LogicLayerEmployeelogic.getTasksForContractorID(ID, destination)
        return tasks
    
    def getTasksForEmployeeID(self, ID, destination = None) -> list[Maintenance]:
        """ Loads maintenance Tasks and maintenance Reports and sees which maintenance Tasks a specific contractor has worked on and returns a list of tasks, otherwise raises ValueError"""
        # Takes in employee ID
        tasks = self.LogicLayerEmployeelogic.getTasksForEmployeeID(ID, destination)
        return tasks
    
    def exchangeManagersAtLocation(self, userInput_previous, temp_employee) -> None:
        """ Function takes in a Manager we are trying to create and the destination, and demotes the current one and adds the new manager"""
        self.LogicLayerEmployeelogic.exchangeManagersAtLocation(userInput_previous, temp_employee)

    def update_employee_data(self, employee) -> None:
        """ Function takes in instance of employee that is already in the DB and updates the attributes of it in the DB"""
        self.LogicLayerEmployeelogic.updateEmployeeData(employee)

    def getManagers(self, destination = None) -> list[Employee]:
        managers = self.LogicLayerEmployeelogic.getManagers(destination)
        return managers

# functions that are about maintenance

    def createMaintenance(self, maintenance) -> None:
        """ Function takes in instance of class Maintenance and saves it in the DB """
        self.LogicLayerMaintenancelogic.createMaintenance(maintenance)
        
    def createMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ Function takes in instance of MaintenanceSchedule and saves it in the DB """
        self.LogicLayerMaintenancelogic.createMaintenanceSchedule(maintenanceSchedule)

    def createMaintenanceReport(self, maintenanceReport) -> None:
        """ Function takes in instance of MaintenanceReport and saves it in the DB """
        self.LogicLayerMaintenancelogic.createMaintenanceReport(maintenanceReport)

    def validateMaintenanceTaskInput(self, user_input, count, temp_maintenanceTask) -> True:
        """ Function validates the input of the user when creating and editing Maintenance Tasks, returns true or raises ValueError """
        return self.LogicLayerMaintenancelogic.validateMaintenanceTaskInput(user_input, count, temp_maintenanceTask)
    
    def validateMaintenanceScheduleInput(self, user_input, count, temp_maintenanceSchedule) -> True:
        """ Function validates the input of the user when creating and editing MaintenanceSchedule, returns true or raises ValueError """
        return self.LogicLayerMaintenancelogic.validateMaintenanceScheduleInput(user_input, count, temp_maintenanceSchedule)
    
    def validateMaintenanceReportEmployeeInput(self, user_input, count, temp_maintenanceReport) -> True:
        """ Function validates the input of the user when creating and editing MaintenanceReport as an Employee, returns true or raises ValueError """
        return self.LogicLayerMaintenancelogic.validateMaintenanceReportEmployeeInput(user_input, count, temp_maintenanceReport)
        
    def validateMaintenanceReportContractorInput(self, user_input, count, temp_maintenanceReport) -> True:
        """ Function validates the input of the user when creating and editing MaintenanceReport as a Contractor, returns true or raises ValueError """
        return self.LogicLayerMaintenancelogic.validateMaintenanceReportContractorInput(user_input, count, temp_maintenanceReport)
    
    def createTempMaintenance(self) -> Maintenance:
        """ Function creates a unique ID for Maintenance, creates an empty one, and returns it to be filled out by user"""
        return self.LogicLayerMaintenancelogic.createTempMaintenance()

    def createTempMaintenanceSchedule(self) -> MaintenanceSchedule:
        """ Function creates a unique ID for MaintenanceSchedule, creates an empty one, and returns it to be filled out by user"""
        return self.LogicLayerMaintenancelogic.createTempMaintenanceSchedule()
    
    def createTempMaintenanceReport(self) -> MaintenanceReport:
        """ Function creates a unique ID for MaintenanceReport, creates an empty one, and returns it to be filled out by user"""
        return self.LogicLayerMaintenancelogic.createTempMaintenanceReport()
    
    def getMaintenanceTaskData(self, destination = None) -> list[Maintenance]:
        """ Function loads all Maintenance's that are in the DB and returns a list of maintenances"""
        maintenanceTask = self.LogicLayerMaintenancelogic.getMaintenanceData(destination)
        return maintenanceTask
    
    def getMaintenanceScheduleData(self) -> list[MaintenanceSchedule]:
        """ Function loads all MaintenanceSchedules that are in the DB and returns a list of maintenanceSchedules"""
        maintenanceSchedules = self.LogicLayerMaintenancelogic.getMaintenanceScheduleData()
        return maintenanceSchedules
    
    def getMaintenanceReportData(self) -> list[MaintenanceReport]:
        """ Functioon loads all MaintenanceReports that are in the DB and returns a list of MaintenanceReports"""
        maintenanceReports = self.LogicLayerMaintenancelogic.getMaintenanceReportData()
        return maintenanceReports

    def getMaintenanceTaskByID(self, ID, destination = None) -> Maintenance:
        """ Function takes in ID of a Maintenance Task, loads up the maintenances in the DB and tries to find it, returns maintenance Task or raises ValueError"""
        maintenanceTask = self.LogicLayerMaintenancelogic.getMaintenanceTaskByID(ID, destination)
        return maintenanceTask
    
    def getMaintenanceScheduleByID(self, ID) -> MaintenanceSchedule:
        """ Function takes in ID of a Maintenance Schedule, loads up the maintenance Schedules in the DB and tries to find it, returns maintenance Schedule or raises ValueError"""
        maintenanceSchedule = self.LogicLayerMaintenancelogic.getMaintenanceScheduleByID(ID)
        return maintenanceSchedule
    
    def getMaintenanceReportByID(self, ID) -> MaintenanceReport:
        """ Function takes in ID of a Maintenance Report, loads up the maintenance Reports in the DB and tries to find it, returns maintenance Report or raises ValueError"""
        maintenanceReport = self.LogicLayerMaintenancelogic.getMaintenanceReportByID(ID)
        return maintenanceReport
    
    def filterMaintenanceTasksDates(self, tasks, startDate, endDate) -> list[Maintenance]:
        """ Function takes in a start and end date and a a list of tasks, filters the tasks based on the dates and returns a list of the filtered maintenance tasks or raises ValueError """
        filtered_tasks = self.LogicLayerMaintenancelogic.filterMaintenanceTasksDates(tasks, startDate, endDate)
        return filtered_tasks

    def closeMaintenanceTask(self, maintenanceID, user_feedback) -> None:
        """ Function takes in a maintenance ID, and marks it as closed if it can be closed"""
        self.LogicLayerMaintenancelogic.closeMaintenanceTask(maintenanceID, user_feedback)

    def updateMaintenance(self, maintenanceTask) -> None:
        self.LogicLayerMaintenancelogic.updateMaintenance(maintenanceTask)

    def canEditMaintenanceTask(self, maintenanceTask) -> True:
        return self.LogicLayerMaintenancelogic.canEditMaintenanceTask(maintenanceTask)
    
    def canEditMaintenanceSchedule(self, maintenanceSchedule) -> True:
        return self.LogicLayerMaintenancelogic.canEditMaintenanceSchedule(maintenanceSchedule)

    def updateMaintenanceSchedule(self, schedule) -> None:
        """ Function takes in a schedule with updated values, and saves it in the maintenanceSchedule DB"""
        self.LogicLayerMaintenancelogic.updateMaintenanceSchedule(schedule)

    def getReadyToBeClosedMaintenanceTasks(self, destination = None) -> list[Maintenance]:
        tasks = self.LogicLayerMaintenancelogic.getReadyToBeClosedMaintenanceTasks(destination)
        return tasks
    # functions that are about properties.

    def createTempProperty(self) -> Property:
        """ Function creates a unique ID for Property, creates an empty one, and returns it to be filled out by user"""
        return self.LogicLayerPropertyLogic.createTempProperty()
        
    def createProperty(self, tempProperty) -> None:
        """ Function gets a filled out Property object and saves it in the Property DB"""
        self.LogicLayerPropertyLogic.createProperty(tempProperty)

    def validatePropertyInput(self, user_input, count, temp_property) -> True:
        """ Function validates the input of the user when creating and editing Property, returns true or raises ValueError """
        return self.LogicLayerPropertyLogic.validatePropertyInput(user_input, count, temp_property)
    
    def getPropertyData(self, destination = None) -> list[Property]:
        """ Function loads all properties from DB and returns a list of Property objects"""
        propertyLog = self.LogicLayerPropertyLogic.getPropertiesData(destination)
        return propertyLog
    
    def updateProperty(self, property) -> None:
        """ Function takes in instance of Property that is already in the DB and updates the attributes of it in the DB"""
        self.LogicLayerPropertyLogic.updateProperty(property)

    def getPropertyByID(self, ID, destination = None) -> Property:
        """ Function takes in ID of a Property, loads up the properties in the DB and tries to find it, returns Property or raises ValueError"""
        property = self.LogicLayerPropertyLogic.getPropertyByID(ID, destination)
        return property
    
    def getTasksForPropertyID(self, ID, destination = None) -> list[Property]:
        """ Function takes in ID of a Property, loads up the maintenances in the DB and tries to find the ones being done on that property, returns maintenance Tasks or raises ValueError"""
        tasks = self.LogicLayerPropertyLogic.getTasksForPropertyID(ID, destination)
        return tasks
    
    def getDestinationData(self) -> list[Destination]:
        """ Function loads all destinations from DB """
        destinations = self.LogicLayerEmployeelogic.getDestinationData()
        return destinations

    def getDestinationByID(self, ID) -> Destination:
        """ Function gets a certain destination by ID """
        destination = self.LogicLayerEmployeelogic.getDestinationByID(ID)
        return destination
    