from .LogicLayerEmployeeLogic import LogicLayerEmployeeLogic
from .LogicLayerMaintenanceLogic import LogicLayerMaintenanceLogic
from .LogicLayerPropertyLogic import LogicLayerPropertyLogic

class LogicLayerAPI:
    def __init__(self):
        self.LogicLayerEmployeelogic = LogicLayerEmployeeLogic()
        self.LogicLayerMaintenancelogic = LogicLayerMaintenanceLogic()
        self.LogicLayerPropertyLogic = LogicLayerPropertyLogic()

# here are functions of the Employee

    def createEmployee(self, employee):
        self.LogicLayerEmployeelogic.createEmployee(employee)

    def getTempEmployee(self, type_of_employee):
        return self.LogicLayerEmployeelogic.createTempEmployee(type_of_employee)

    def validateEmployeeInput(self, user_input, count, temp_employee):
        return self.LogicLayerEmployeelogic.validateEmployeeInput(user_input, count, temp_employee)
    
    def getEmployeeData(self):
        employeeLog = self.LogicLayerEmployeelogic.getEmployeeData()
        return employeeLog
    
    def getContractorData(self):
        contractorLog = self.LogicLayerEmployeelogic.getContractorData()
        return contractorLog

    def getEmployeebyID(self, ID):
        employee = self.LogicLayerEmployeelogic.getEmployeebyID(ID)
        return employee

    def getContractorbyID(self, ID):
        contractor = self.LogicLayerEmployeelogic.getContractorbyID(ID)
        return contractor
    
    def getTasksForContractorID(self, ID):

        # Takes in contractor ID
        tasks = self.LogicLayerEmployeelogic.getTasksForContractorID(ID)
        return tasks
    
    def getTasksForEmployeeID(self, ID):

        # Takes in employee ID
        tasks = self.LogicLayerEmployeelogic.getTasksForEmployeeID(ID)
        return tasks

    # def assign_task_to_employee(self):
    #     pass

    # def get_employee_tasks(self):
    #     pass

# A superior must be able to create and/or update tickets for properties they manage
# A superior must be able to accept maintenance reports to close tickets
# An employee must be able to register a maintenance report for an open ticket
# An employee must be able to flag a ticket as ready for closing by a superior


    def update_employee_data(self, employee):
        self.LogicLayerEmployeelogic.updateEmployeeData(employee)

# functions that are about maintenance

    def createMaintenance(self, maintenance):
        self.LogicLayerMaintenancelogic.createMaintenance(maintenance)
        
    def createMaintenanceSchedule(self, maintenanceSchedule):
        self.LogicLayerMaintenancelogic.createMaintenanceSchedule(maintenanceSchedule)

    def validateMaintenanceTaskInput(self, user_input, count, temp_maintenanceTask):
        return self.LogicLayerMaintenancelogic.validateMaintenanceTaskInput(user_input, count, temp_maintenanceTask)
    
    def validateMaintenanceScheduleInput(self, user_input, count, temp_maintenanceSchedule):
        return self.LogicLayerMaintenancelogic.validateMaintenanceScheduleInput(user_input, count, temp_maintenanceSchedule)
    
    def createTempMaintenance(self):
        return self.LogicLayerMaintenancelogic.createTempMaintenance()

    def createTempMaintenanceSchedule(self):
        return self.LogicLayerMaintenancelogic.createTempMaintenanceSchedule()
    
    def getMaintenanceTaskData(self):
        maintenanceTask = self.LogicLayerMaintenancelogic.getMaintenanceData()
        return maintenanceTask
    
    def getMaintenanceScheduleData(self):
        maintenanceSchedules = self.LogicLayerMaintenancelogic.getMaintenanceScheduleData()
        return maintenanceSchedules

    def getMaintenanceTaskByID(self, ID):
        maintenanceTask = self.LogicLayerMaintenancelogic.getMaintenanceTaskByID(ID)
        return maintenanceTask
    
    def getMaintenanceScheduleByID(self, ID):
        maintenanceSchedule = self.LogicLayerMaintenancelogic.getMaintenanceScheduleByID(ID)
        return maintenanceSchedule

    def closeMaintenanceReport(self):
        pass

    def update_maintenance_status(self):
        pass

    def create_a_report(self):
        pass

    def changeStatusOfReportAsReady(self):
        pass

    def edit_maintenance_schedule(self):
        pass

    # functions that are about properties.

    def updateStatusOfProperty(self):
        self.LogicLayerPropertyLogic.updateStatusOfProperty(property)

    def createTempProperty(self):
        return self.LogicLayerPropertyLogic.createTempProperty()
        
    def createProperty(self, tempProperty):
        self.LogicLayerPropertyLogic.createProperty(tempProperty)

    def validatePropertyInput(self, user_input, count, temp_property):
        return self.LogicLayerPropertyLogic.validatePropertyInput(user_input, count, temp_property)
    
    def getPropertyData(self):
        propertyLog = self.LogicLayerPropertyLogic.getPropertiesData()
        return propertyLog
    
    def updateProperty(self, property):
        self.LogicLayerPropertyLogic.updateProperty(property)

    def getPropertyByID(self, ID):
        property = self.LogicLayerPropertyLogic.getPropertyByID(ID)
        return property
    
    def getTasksForPropertyID(self, ID):
        tasks = self.LogicLayerPropertyLogic.getTasksForPropertyID(ID)
        return tasks
    

