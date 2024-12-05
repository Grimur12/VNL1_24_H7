from LogicLayerEmployeeLogic import LogicLayerEmployeeLogic
from LogicLayerMaintenanceLogic import LogicLayerMaintenanceLogic
from LogicLayerPropertyLogic import LogicLayerPropertyLogic


class LogicLayerAPI:
    
    def __init__(self, LogicLayerEmployeeLogic, LogicLayerMaintenanceLogic, LogicLayerPropertyLogic):

        self.LogicLayerEmployeelogic = LogicLayerEmployeeLogic(),
        self.LogicLayerMaintenancelogic = LogicLayerMaintenanceLogic(), 
        self.LogicLayerPropertyLogic = LogicLayerPropertyLogic(), 


# here are functions of the Employee

    def createEmployee(self, ):
        self.

    def assign_task_to_employee(self, task):
        pass

    def get_employee_tasks(self, task):
        pass

    def update_employee_data(self, ):
        pass

    
# here are functions with maintenence operations

    def create_maintenance(self):
        self.

    def close_maintenenca_report(self):
        pass

    def update_maintenance_status(self, maintenanceID, statusOfMaintenance, priority,):
        pass

    def create_a_report(self, maintenanceID, contractors, ):
        self.

    def changeStatusOfReportAsReady(self, ):
        pass

    def edit_maintenance_schedule(self, maintenanceID, taskType, frequency):
        pass

# functions that are about properties,

    def updateStatusOfProperty(self, params):
        pass

    def addProperty(self, params):
        pass

