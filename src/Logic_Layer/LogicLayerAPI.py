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

    def getTempEmployee(self):
        return self.LogicLayerEmployeelogic.createTempEmployee()

    def validateEmployeeInput(self, user_input, count, temp_employee):
        return self.LogicLayerEmployeelogic.validateEmployeeInput(user_input, count, temp_employee)
    
    def getEmployeeData(self):
        employeeLog = self.LogicLayerEmployeelogic.getEmployeeData()
        return employeeLog

    def getEmployeebyID(self, ID):
        employee = self.LogicLayerEmployeelogic.getEmployeebyID(ID)
        return employee

    def assign_task_to_employee(self):
        pass

    def get_employee_tasks(self):
        pass

    def update_employee_data(self, employee):
        self.LogicLayerEmployeelogic.updateEmployeeData(employee)

# here are functions with maintenence operations

    def create_maintenance(self):
        self.LogicLayerMaintenanceLogic.createMaintenance()

    def close_maintenenca_report(self):
        pass

    def update_maintenance_status(self):
        pass

    def create_a_report(self):
        pass

    def changeStatusOfReportAsReady(self):
        pass

    def edit_maintenance_schedule(self):
        pass

    # functions that are about properties,

    def updateStatusOfProperty(self):
        pass

    def createProperty(self):
        self.LogicLayerPropertyLogic.createProperty()

