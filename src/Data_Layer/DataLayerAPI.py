from EmployeesDBLogic import EmployeesDBLogic
from MaintenanceDBLogic import MaintenanceDBLogic
from PropertiesDBLogic import PropertiesDBLogic

class DataLayerAPI:
    def __init__(self):
        pass

    def addEmployee(self, params) -> None:
        EmployeesDBLogic.createEmployee(params)

    def loadEmployeeLog(self) -> None:
        EmployeesDBLogic.loadEmployeeLog()

    def updateEmployee(self, params) -> None:
        EmployeesDBLogic.updateEmployee(params)

    def removeEmployee(self, ID) -> None:
        EmployeesDBLogic.removeEmployee(ID)

    def propagateData(self) -> None:
        return EmployeesDBLogic.propagateData()
    
    def loadPropertiesLog(self) -> None:
        PropertiesDBLogic.loadPropertiesLog()

    def createProperty(self, params) -> None:
        PropertiesDBLogic.createProperty(params)

    def removeProperty(self, ID) -> None:
        PropertiesDBLogic.removeProperty(ID)

    def updateProperty(self, params) -> None:
        PropertiesDBLogic.updateProperty(params)
    
    def propagateData(self) -> list:
        return PropertiesDBLogic.propagateData()


