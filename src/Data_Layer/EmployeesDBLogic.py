# Employee DB Logic
import os
import json
from Models.Workers import Employee
from Models.Workers import Contractor

class EmployeesDBLogic:
    def __init__(self) -> None:
        """ Holds reference to the Employees DB """
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "Employees.json")

    def loadEmployeeLog(self) -> list:
        """ Function loads all saved employees from DB and turns back into class instances of Employee and returns a list of them """
        employees_list = []
        try:
            with open(self.file_path, "r") as employeeDBOpen:
                employees_list = json.load(employeeDBOpen)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
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
        """ Function saves all instances of the employee class received in the employees (parameter) list, in dictionary form into json Database """
        Employees = []
        for employee in employees:
            if employee.type == "Contractor":
                Employees.append(employee.Contractor_dict())
            else:
                Employees.append(employee.Employee_dict())

        with open(self.file_path, "w") as file:
            json.dump(Employees, file, indent=4)

    def createEmployee(self, employee) -> None:
        """ Function takes in an employee instance, loads all employees from DB, adds the employee to that list and saves it again into the DB  """
        employees = self.loadEmployeeLog()
        employees.append(employee)
        self.saveEmployees(employees)
    
    def createContractor(self, contractor) -> None:
        """ Function takes in a contractor instance, loads all employees from DB, adds the employee to that list and saves it again into the DB  """
        employees = self.loadEmployeeLog()
        employees.append(contractor)
        self.saveEmployees(employees)

    def updateEmployee(self, employee) -> None:
        """ This function takes in an employee instance, finds old version of it by checking the ID, overwrites it and saves the employees again in the json DB"""
        # Need to split into instances of General Employee/Manger and Contractor as they have different parameters
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