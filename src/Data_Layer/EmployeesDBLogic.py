# Employee DB Logic
import os
import json
from Models.Workers import Employee
from Models.Workers import Contractor

class EmployeesDBLogic:
    def __init__(self) -> None:
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "Employees.json")

    def loadEmployeeLog(self) -> list:
        """ Function loads all saved employees from DB and turns back into class instances of Employee and saves it internally """
        employees_list = []
        try:
            with open(self.file_path, "r") as employeeDBOpen:
                employees_list = json.load(employeeDBOpen)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        # Params 8 is a reference to "type" variable in the classes
        employees = []
        for employee in employees_list:
            inCommonParameters = list(employee.values())[:9] # First 9 are both in contractor and employee
            independantParameters = list(employee.values())[9:] # Last 4 are contractor specific
            if inCommonParameters[8] == "Contractor":
                employees.append(Contractor(*independantParameters, *inCommonParameters))
            else:
                employees.append(Employee(*inCommonParameters))
        return employees

    def saveEmployees(self, employees) -> None:
        """ Function saves all instances of the employee class saved in self.employees in dictionary form into json Database """
        Employees = []
        for employee in employees:
            if employee.type == "Contractor":
                Employees.append(employee.Contractor_dict())
            else:
                Employees.append(employee.Employee_dict())

        with open(self.file_path, 'w') as file:
            json.dump(Employees, file, indent=4)

    def createEmployee(self, employee) -> None:
        """  """
        # Params should be a list of all the variables Employee() or Contractor() class needs to initialize in the correct order
        employees = self.loadEmployeeLog()
        employees.append(employee)
        self.saveEmployees(employees)
    
    def createContractor(self, contractor) -> None:
        employees = self.loadEmployeeLog()
        employees.append(contractor)
        self.saveEmployees(employees)

    def updateEmployee(self, employee) -> None:
        """ This function takes in a list of parameters, some may be new some may still be the older ones and stores them in the json DB """
        # Need to split into instances of General Employee/Manger and Contractor as they have different parameters
        # Params 8 is a reference to "type" variable in the classes
        employees = self.loadEmployeeLog()
        for index, empl in enumerate(employees):
            if empl.employeeID == employee.employeeID: # If employee is the same (check on ID)
                employees[index] = employee
                break
        # Finally update the DB
        self.saveEmployees(employees)

    def printEmployees(self) -> None:
        """ Prints out all employees from the database """
        employees = self.loadEmployeeLog()  # Load current employees
        for employee in employees:
            print("-------------------------------------------------------------------------------------------------------------")
            if employee.type == "Contractor":
                for key, value in employee.__dict__.items():
                    print(f"{key}: {value}")
            else:
                for key, value in employee.__dict__.items():
                    print(f"{key}: {value}")