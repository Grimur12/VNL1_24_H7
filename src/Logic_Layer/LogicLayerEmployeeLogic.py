from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Workers import Employee, Contractor
from .ErrorCheckers import ErrorCheckers

class LogicLayerEmployeeLogic:
    def __init__(self):
        #
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()

    def createUniqueID(self) -> int:
        #here we create a new unique ID for the employees
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
        if self.Errors.checkNumber(count):
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
                employee_found = employeeLog[index_to_update]
                return employee_found
            else:
                raise ValueError("No Employee by that ID")
    
    def getContractorbyID(self, ID):
        if self.Errors.checkNumber(ID):
            employeeLog = self.DataLayerWrapper.loadEmployeeLog()
            index_to_update = -1
            for index, contractor in enumerate(employeeLog):
                if contractor.employeeID == int(ID) and contractor.type == "Contractor": ## Making sure that the ID provided is a contractor, we can have the ID in the DB but it could be a General Employee or a Manager
                    index_to_update = index
            if index_to_update != -1:
                contractor_found = employeeLog[index_to_update]
                return contractor_found
            else:
                raise ValueError("No Contractor by that ID")

    def getEmployeeData(self):
        """ Load all the employees from the DB and filter out all the General Employess and Managers to return in a list format """
        #get Employees Data
        employeeLog = self.DataLayerWrapper.loadEmployeeLog()
        filtered_employees = []
        for employee in employeeLog:
            if employee.type != "Contractor":
                filtered_employees.append(employee)
        return filtered_employees
    
    def getContractorData(self):
        """ Load all employees from the DB and filter out all the contractors to return in a list format """
        contractorlog = self.DataLayerWrapper.loadEmployeeLog()
        filtered_contractors = []
        for contractor in contractorlog:
            if contractor.type == "Contractor":
                filtered_contractors.append(contractor)
        return filtered_contractors
    
    def getTasksForEmployeeID(self, ID):

        # We take in the employee ID
        # Find the employee
        # Load in all maintenance reports
        # If the employee is in a maintenance report we append the maintenance associated with that maintenance report into a list to return
        employee = self.getEmployeebyID(ID)
        maintenanceTaskLog = self.DataLayerWrapper.loadMaintenanceLog()
        maintenanceReportLog = self.DataLayerWrapper.loadMaintenanceReportLog()
        employeeTasks = []
        maintenanceTaskIDs = []
        for report in maintenanceReportLog:
            if report.employeeID == employee.employeeID:
                maintenanceTaskIDs.append(report.maintenanceID)
        # We have found all the maintenances that a employee has worked on now we need to append the maintenances
        for maintenanceTask in maintenanceTaskLog:
            if maintenanceTask.maintenanceID in maintenanceTaskIDs:
                employeeTasks.append(maintenanceTask)
                
        if len(employeeTasks) == 0:
            raise ValueError("This Employee has not worked on any Maintenance Tasks")
            
        return employeeTasks

    def getTasksForContractorID(self, ID):

        # We take in the contractor ID
        # Find the contractor
        # Load in all maintenance reports
        # If the contractor is in a maintenance report we append the maintenance associated with that maintenance report into a list to return
        contractor = self.getContractorbyID(ID)
        maintenanceTaskLog = self.DataLayerWrapper.loadMaintenanceLog()
        maintenanceReportLog = self.DataLayerWrapper.loadMaintenanceReportLog()
        contractorTasks = []
        maintenanceTaskIDs = []
        for report in maintenanceReportLog:
            if report.contractorID == contractor.employeeID:
                maintenanceTaskIDs.append(report.maintenanceID)
        # We have found all the maintenances that a contractor has worked on now we need to append the maintenances
        for maintenanceTask in maintenanceTaskLog:
            if maintenanceTask.maintenanceID in maintenanceTaskIDs:
                contractorTasks.append(maintenanceTask)

        if len(contractorTasks) == 0:
            raise ValueError("This Contractor has not worked on any Maintenance Tasks")
            
        return contractorTasks

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
        







    
    #check errors
    def check_employee_Errors(self):
        pass
