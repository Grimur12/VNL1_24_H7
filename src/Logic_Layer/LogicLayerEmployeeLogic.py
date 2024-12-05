from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Workers import *
from .ErrorCheckers import ErrorCheckers

class LogicLayerEmployeeLogic:
    def __init__(self):
        # This list is to store our employees
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()

    def createUniqueID(self) -> int:
        currentEmployees = self.DataLayerWrapper.loadEmployeeLog()
        if len(currentEmployees) != 0:
            newID = currentEmployees[-1].employeeID + 1 # Assign new employee with a unique ID
        else:
            newID = 1
        return newID
    
    def createTempEmployee(self, type_of_employee):

        #  Type of employee should be "1" for General Employee, "2 " for Manager, "3" for Contractor 
        tempEmployeeID = self.createUniqueID()
        if type_of_employee == "1": # General Employee
            temp_employee = Employee(ID=tempEmployeeID, type="General")
        elif type_of_employee == "2": # Manager
            temp_employee = Employee(ID=tempEmployeeID, type="Manager")
        elif type_of_employee == "3":
            temp_employee = Contractor()
            temp_employee.employeeID = tempEmployeeID
            temp_employee.type = "Contractor"
        else:
            return None
        return temp_employee
    

    def validateEmployeeInput(self, input, count, temp_employee):
        # We dont have to check for ID and type since that is automatically assigned based on user choice
        if self.Errors.checkNumber:
            count = int(count)
        if count == 1:  # Name
            self.Errors.errorCheckName(input)
            temp_employee.name = input
        elif count == 2:  # Social Security
            self.Errors.errorCheckSocialSecurity(input)
            temp_employee.socialSecurity = input
        elif count == 3:  # Address
            self.Errors.errorCheckAddress(input)
            temp_employee.address = input
        elif count == 4:  # At Home Phone
            self.Errors.errorCheckPhone(input)
            temp_employee.atHomePhone = input
        elif count == 5:  # GSM Phone
            self.Errors.errorCheckPhone(input)
            temp_employee.gsmPhone = input
        elif count == 6:  # Email
            self.Errors.errorCheckEmail(input)
            temp_employee.email = input
        elif count == 7:  # Work Location
            self.Errors.errorCheckLocation(input)
            temp_employee.workLocation = input
        # Beyond this point is contractor specific
        elif count == 8:  #
            self.Errors.errorCheckEmployeePreviousTask(input)
            temp_employee.previousTask = input
        elif count == 9:
            self.Errors.errorCheckEmployeePerformanceRating(input)
            temp_employee.performanceRating = input
        elif count == 10:
            self.Errors.errorCheckContractorContact(input)
            temp_employee.contractorContact = input
        elif count == 11:
            self.Errors.errorCheckEmployeeOpeningHours(input)
            temp_employee.openingHours = input
        return True

    def getEmployeebyID(self, ID):
        if self.Errors.checkNumber(ID):
            employeeLog = self.DataLayerWrapper.loadEmployeeLog()
            index_to_update = -1
            for index, employee in enumerate(employeeLog):
                if employee.employeeID == int(ID) and employee.type != "Contractor":
                    index_to_update = index
            if index_to_update != -1:
                employee = employeeLog[index_to_update]
                return employee
            else:
                raise ValueError("No Employee by that ID")
    
    def getContractorbyID(self, ID):
        if self.Errors.checkNumber(ID):
            employeeLog = self.DataLayerWrapper.loadEmployeeLog()
            index_to_update = -1
            for index, employee in enumerate(employeeLog):
                if employee.employeeID == int(ID) and employee.type == "Contractor":
                    index_to_update = index
            if index_to_update != -1:
                employee = employeeLog[index_to_update]
                return employee
            else:
                raise ValueError("No Contractor by that ID")

    #get Employees Data
    def getEmployeeData(self):
        employeeLog = self.DataLayerWrapper.loadEmployeeLog()
        return employeeLog
        
    def createEmployee(self, temp_employee):
        # params should be either
        # [name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType] for employees 
        # [name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType, previousTask, performanceRating, contractorContact, openingHours] for contractors
        if temp_employee == "Contractor":
            self.DataLayerWrapper.createContractor(temp_employee)
        else:
            self.DataLayerWrapper.createEmployee(temp_employee)
        return True
    
    def updateEmployeeData(self,employee):
        # input can be name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType for employees 
        self.DataLayerWrapper.updateEmployee(employee)
        
                
    #filter Employees                   
    def filterEmployees(self, workLocation: str = None, employeeType: str = None) -> list:
        pass
        # for employee in loadEmployeeLog():
        #     if workLocation
    
    #check errors
    def check_employee_Errors(self):
        pass