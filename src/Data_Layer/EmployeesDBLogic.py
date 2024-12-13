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
        employees_list = [] # Start off with an empty list
        try:
            with open(self.file_path, "r") as employeeDBOpen:
                employees_list = json.load(employeeDBOpen) # Load all Employees from the DB
        except FileNotFoundError: # Unless file is not found, we return an empty list anyways (basically assumes that the DB dosent exist so an empty list would make sense here)
            return []
        except json.JSONDecodeError: # And unless no Employees in the DB (or corrupt) so we return an empty list, because the DB is empty
            return []
        # We loaded in all of the Employee but they are dictionaries since we store them as such
        employees = []
        for employee in employees_list:
            inCommonParameters = list(employee.values())[:9] # First 9 are both in contractor and employee
            independantParameters = list(employee.values())[9:] # Last 4 are contractor specific
            if inCommonParameters[8] == "Contractor":
                employees.append(Contractor(*independantParameters, *inCommonParameters)) # If the employee dictionary in question is a Contractor we pass the common parameters and the contractor specific ones to create the contractor class
            else:
                employees.append(Employee(*inCommonParameters)) # Otherwise if a general employee or a manager just create the class normally with the common parameters
        return employees

    def saveEmployees(self, employees) -> None:
        """ Function saves all instances of the employee class received in the employees (parameter) list, in dictionary form into json Database """
        Employees = []
        for employee in employees:
            if employee.type == "Contractor": # We need to change the Employees into dictionaries to save them in the DB
                Employees.append(employee.Contractor_dict()) # If its a contractor we use the contractor dict
            else:
                Employees.append(employee.Employee_dict()) # If manager or employee use the employee dict

        with open(self.file_path, "w") as file: # Save all the dictionaries into the DB
            json.dump(Employees, file, indent=4)

    def createEmployee(self, employee) -> None:
        """ Function takes in an employee instance, loads all employees from DB, adds the employee to that list and saves it again into the DB  """
        employees = self.loadEmployeeLog() # Load all employees (Class Object)
        employees.append(employee) # Add the employee we just created to the list of Employees
        self.saveEmployees(employees) # Save the updated list of employees to the DB
    
    def createContractor(self, contractor) -> None:
        """ Function takes in a contractor instance, loads all employees from DB, adds the employee to that list and saves it again into the DB  """
        employees = self.loadEmployeeLog() # Load all employees (Class Object)
        employees.append(contractor) # Add the Contractor we just created to the list of Employees
        self.saveEmployees(employees) # Save the updated list of employees to the DB

    def updateEmployee(self, employee) -> None:
        """ This function takes in an employee instance, finds old version of it by checking the ID, overwrites it and saves the employees again in the json DB"""
        # Need to split into instances of General Employee/Manger and Contractor as they have different parameters
        employees = self.loadEmployeeLog() # Load all the employees (Class Objects)
        for index, empl in enumerate(employees): # Find the employee we are udpating in the DB
            if empl.employeeID == employee.employeeID: # If employee is the same (check on ID)
                employees[index] = employee # Overwrite it in the list
                break
        # Finally update the DB
        self.saveEmployees(employees) # Save the list of employees to the DB, (including the newly updated one)
