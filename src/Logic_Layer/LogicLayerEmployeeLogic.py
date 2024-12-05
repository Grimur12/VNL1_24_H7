from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Workers import *
from .ErrorCheckers import ErrorCheckers

class LogicLayerEmployeeLogic:
    def __init__(self):
        # This list is to store our employees
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()
        self.temp_employee = None

    def createUniqueID(self) -> int:
        currentEmployees = self.DataLayerWrapper.loadEmployeeLog()
        if len(currentEmployees) != 0:
            newID = currentEmployees[-1].employeeID + 1 # Assign new employee with a unique ID
        else:
            newID = 1
        return newID
    
    def createTempEmployee(self):
        tempEmployeeID = self.createUniqueID()
        self.temp_employee = Employee(ID=tempEmployeeID)
        return self.temp_employee
    

    def validateEmployeeInput(self, input, count, temp_employee):
        print(f"Validation : {temp_employee}")
        if input == "":
            raise ValueError("Information field cannot be empty")
        if count == 0:  # Name
            self.Errors.errorCheckName(input)
            temp_employee.name = input
        elif count == 1:  # Social Security
            self.Errors.errorCheckSocialSecurity(input)
            temp_employee.socialSecurity = input
        elif count == 2:  # Address
            self.Errors.errorCheckAddress(input)
            temp_employee.address = input
        elif count == 3:  # At Home Phone
            self.Errors.errorCheckPhone(input)
            temp_employee.atHomePhone = input
        elif count == 4:  # GSM Phone
            self.Errors.errorCheckPhone(input)
            temp_employee.gsmPhone = input
        elif count == 5:  # Email
            self.Errors.errorCheckEmail(input)
            temp_employee.email = input
        elif count == 6:  # Work Location
            self.Errors.errorCheckLocation(input)
            temp_employee.workLocation = input
        elif count == 7:  # Type
            self.Errors.errorCheckEmployeeType(input)
            temp_employee.type = input

        return True
    

    def getEmployeebyID(self, ID):
        employeeLog = self.DataLayerWrapper.loadEmployeeLog()
        index_to_update = -1
        for index, employee in enumerate(employeeLog):
            if employee.employeeID == int (ID):
                index_to_update = index
        if index_to_update != -1:
            employee = employeeLog[index_to_update]
        return employee

    #get Employees Data
    def getEmployeeData(self):
        employeeLog = self.DataLayerWrapper.loadEmployeeLog()
        return employeeLog
        
    def createEmployee(self, temp_employee):
        # params should be either
        # [name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType] for employees 
        # [name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType, previousTask, performanceRating, contractorContact, openingHours] for contractors
        params = list(temp_employee.__dict__.values())
        self.DataLayerWrapper.createEmployee(params)
        return True
    
    def updateEmployeeData(self,employee):
        # input can be name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType for employees 
        params = list(employee.__dict__.values())
        self.DataLayerWrapper.updateEmployee(params)
        
                
    #filter Employees                   
    def filterEmployees(self, workLocation: str = None, employeeType: str = None) -> list:
        pass
        # for employee in loadEmployeeLog():
        #     if workLocation
    
    #check errors
    def check_employee_Errors(self):
        pass