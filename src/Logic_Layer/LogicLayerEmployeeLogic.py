from Data_Layer.DataLayerAPI import DataLayerAPI
import ErrorCheckers

class LogicLayerEmployeeLogic:
    def __init__(self):
        # This list is to store our employees
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()

    def createEmployee(self, params):
        
        # params should be either
        # [name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType] for employees 
        # [name, address, socialSecurity, atHomePhone, gsm, email, workLocation, employeeType, previousTask, performanceRating, contractorContact, openingHours] for contractors
        currentEmployees = DataLayerAPI.loadEmployeeLog()
        newID = currentEmployees[-1].employeeID + 1 # Assign new employee with a unique ID
        # Check parameters for errors
        parameters = [newID] + params
        if params[8] == "Contractor":
            if self.Errors.checkContractorInput(params):
                self.DataLayerWrapper.createContractor(parameters)
            else:
                raise ValueError("Incorrect input for Contractor")
        else:
            if self.Errors.checkEmployeeInput(params):
                self.DataLayerWrapper.createEmployee(parameters)
            else:
                raise ValueError("Incorrect input for Employee")
    


        # # Check if social security number already exists
        # for empl in self.employees:
        #     if empl["socialSecurity"] == socialSecurity:
        #         return False, "Employee with this social security number already exists."

        # #Check if gsm is alredy used
        # for empl in self.employees:
        #     if empl["gsm"] == gsm:
        #         return False, "Employee with this gsm already exists."

        # # Check if email is already used
        # for emp in self.employees:
        #     if emp["email"] == email:
        #         return False, "Employee with this email address already exists."


        # # Add new employee
        # employeeId = len(self.employees) + 1
        # newEmployee = {
        #     "id": employeeId,
        #     "name": name,
        #     "address": address,
        #     "social_security": socialSecurity,
        #     "at_home_phone": atHomePhone,
        #     "gsm": gsm,
        #     "email": email,
        #     "work_location": workLocation,
        #     "employee_type": employeeType,
        # }
        # self.employees.append(newEmployee)
        # return f"Employee {name} added successfully."


    #filter Employees                   
    def filterEmployees(self, workLocation: str = None, employeeType: str = None) -> list:
        for employee in loadEmployeeLog():
            if workLocation

    
    #get Employees Data
    def getEmployeeData(self):
        pass
    


    # #check errors
    # def check_employee_Errors(self):
    #     pass
    # DOUBLE CHECK ERROR CHECK
    
