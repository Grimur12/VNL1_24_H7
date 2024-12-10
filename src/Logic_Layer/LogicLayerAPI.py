from .LogicLayerEmployeeLogic import LogicLayerEmployeeLogic
from .LogicLayerMaintenanceLogic import LogicLayerMaintenanceLogic
from .LogicLayerPropertyLogic import LogicLayerPropertyLogic
from Models.Workers import *
from Models.Maintenance import Maintenance
from Models.MaintenanceReport import MaintenanceReport
from Models.MaintenanceSchedule import MaintenanceSchedule
from Models.Property import Property

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
    
    def getEmployeeData(self) -> list[Employee]:
        """ Function gets all of the employees currently stored in the DB if they are of the type Manager or General """
        employeeLog = self.LogicLayerEmployeelogic.getEmployeeData()
        return employeeLog
    
    def getContractorData(self) -> list[Contractor]:
        """ Function gets all of the contractors currently stored in the employees DB """
        contractorLog = self.LogicLayerEmployeelogic.getContractorData()
        return contractorLog

    def getEmployeebyID(self, ID) -> Employee:
        """ Loads the entire employees DB and tries to find if the employee exists in it, raises ValueError if it does not exist """
        employee = self.LogicLayerEmployeelogic.getEmployeebyID(ID)
        return employee

    def getContractorbyID(self, ID) -> Contractor:
        """ Loads the entire employees DB and tries to find if the contractor exists in it, raises ValueError if it does not exist """
        contractor = self.LogicLayerEmployeelogic.getContractorbyID(ID)
        return contractor
    
    def getTasksForContractorID(self, ID) -> list[Maintenance]:
        """ Loads maintenance Tasks and maintenance Reports and sees which maintenance Tasks a specific contractor has worked on and returns a list of tasks, otherwise raises ValueError"""
        # Takes in contractor ID
        tasks = self.LogicLayerEmployeelogic.getTasksForContractorID(ID)
        return tasks
    
    def getTasksForEmployeeID(self, ID) -> list[Maintenance]:
        """ Loads maintenance Tasks and maintenance Reports and sees which maintenance Tasks a specific contractor has worked on and returns a list of tasks, otherwise raises ValueError"""
        # Takes in employee ID
        tasks = self.LogicLayerEmployeelogic.getTasksForEmployeeID(ID)
        return tasks
    
    def exchangeManagersAtLocation(self, userInput_previous, temp_employee):
        self.LogicLayerEmployeelogic.exchangeManagersAtLocation(userInput_previous, temp_employee)

    # def assign_task_to_employee(self):
    #     pass

    # def get_employee_tasks(self):
    #     pass

# A superior must be able to create and/or update tickets for properties they manage
# A superior must be able to accept maintenance reports to close tickets
# An employee must be able to register a maintenance report for an open ticket
# An employee must be able to flag a ticket as ready for closing by a superior


    def update_employee_data(self, employee) -> None:
        """ Function takes in instance of employee that is already in the DB and updates the attributes of it in the DB"""
        self.LogicLayerEmployeelogic.updateEmployeeData(employee)

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
    
    def getMaintenanceTaskData(self) -> list[Maintenance]:
        """ Function loads all Maintenance's that are in the DB and returns a list of maintenances"""
        maintenanceTask = self.LogicLayerMaintenancelogic.getMaintenanceData()
        return maintenanceTask
    
    def getMaintenanceScheduleData(self) -> list[MaintenanceSchedule]:
        """ Function loads all MaintenanceSchedules that are in the DB and returns a list of maintenanceSchedules"""
        maintenanceSchedules = self.LogicLayerMaintenancelogic.getMaintenanceScheduleData()
        return maintenanceSchedules
    
    def getMaintenanceReportData(self) -> list[MaintenanceReport]:
        """ Functioon loads all MaintenanceReports that are in the DB and returns a list of MaintenanceReports"""
        maintenanceReports = self.LogicLayerMaintenancelogic.getMaintenanceReportData()
        return maintenanceReports

    def getMaintenanceTaskByID(self, ID) -> Maintenance:
        """ Function takes in ID of a Maintenance Task, loads up the maintenances in the DB and tries to find it, returns maintenance Task or raises ValueError"""
        maintenanceTask = self.LogicLayerMaintenancelogic.getMaintenanceTaskByID(ID)
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

    def updateMaintenance(self, maintenanceTask):
        self.LogicLayerMaintenancelogic.updateMaintenance(maintenanceTask)

    def canEditMaintenanceTask(self, maintenanceTask):
        return self.LogicLayerMaintenancelogic.canEditMaintenanceTask(maintenanceTask)
    
    def canEditMaintenanceSchedule(self, maintenanceSchedule):
        return self.LogicLayerMaintenancelogic.canEditMaintenanceSchedule(maintenanceSchedule)

    def updateMaintenanceSchedule(self, schedule) -> None:
        """ Function takes in a schedule with updated values, and saves it in the maintenanceSchedule DB"""
        self.LogicLayerMaintenancelogic.updateMaintenanceSchedule(schedule)

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
    
    def getPropertyData(self) -> list[Property]:
        """ Function loads all properties from DB and returns a list of Property objects"""
        propertyLog = self.LogicLayerPropertyLogic.getPropertiesData()
        return propertyLog
    
    def updateProperty(self, property) -> None:
        """ Function takes in instance of Property that is already in the DB and updates the attributes of it in the DB"""
        self.LogicLayerPropertyLogic.updateProperty(property)

    def getPropertyByID(self, ID) -> None:
        """ Function takes in ID of a Property, loads up the properties in the DB and tries to find it, returns Property or raises ValueError"""
        property = self.LogicLayerPropertyLogic.getPropertyByID(ID)
        return property
    
    def getTasksForPropertyID(self, ID) -> list[Property]:
        """ Function takes in ID of a Property, loads up the maintenances in the DB and tries to find the ones being done on that property, returns maintenance Tasks or raises ValueError"""
        tasks = self.LogicLayerPropertyLogic.getTasksForPropertyID(ID)
        return tasks
    

