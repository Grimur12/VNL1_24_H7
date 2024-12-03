from EmployeesDBLogic import EmployeesDBLogic
from MaintenanceDBLogic import MaintenanceDBLogic
from PropertiesDBLogic import PropertiesDBLogic

class DataLayerAPI:
    def __init__(self):
        pass

    def addEmployee(self, params):
        EmployeesDBLogic.createEmployee(params)
    

