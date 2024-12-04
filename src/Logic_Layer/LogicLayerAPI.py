from .LogicLayerEmployeeLogic import LogicLayerEmployeeLogic
from .LogicLayerMaintenanceLogic import LogicLayerMaintenanceLogic
from .LogicLayerPropertyLogic import LogicLayerPropertyLogic


class LogicLayerAPI:
    def __init__(self):
        self.LogicLayerEmployeelogic = LogicLayerEmployeeLogic()
        self.LogicLayerMaintenancelogic = LogicLayerMaintenanceLogic()
        self.LogicLayerPropertyLogic = LogicLayerPropertyLogic()

# here are functions of the Employee

    def createEmployee(self):
        self.LogicLayerEmployeelogic.createEmployee()

    def getTempEmployee(self):
        return self.LogicLayerEmployeelogic.createTempEmployee()

    def validateEmployeeInput(self, user_input, count):
        return self.LogicLayerEmployeelogic.validateEmployeeInput(user_input, count)
    
    def getEmployeeData(self):
        employeeLog = self.LogicLayerEmployeelogic.getEmployeeData()
        return employeeLog

    def assign_task_to_employee(self, task):
        pass

    def get_employee_tasks(self, task):
        pass

    def update_employee_data(self):
        pass

# here are functions with maintenence operations

    def create_maintenance(self):
        pass

    def close_maintenenca_report(self):
        pass

    def update_maintenance_status(self, maintenanceID, statusOfMaintenance, priority,):
        pass

    def create_a_report(self, maintenanceID, contractors, ):
        pass

    def changeStatusOfReportAsReady(self, ):
        pass

    def edit_maintenance_schedule(self, maintenanceID, taskType, frequency):
        pass

    # functions that are about properties,

    def updateStatusOfProperty(self, name, availability):
        pass

    def addProperty(self, nameOfProperty, locationOfProperty, availability, hasAPool, hasATub, hasOvens):
        pass

    def deleteProperty(self, propertyID):
        pass
    