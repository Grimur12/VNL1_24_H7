# Employee DB Logic
import os
import json
from Models.Workers import Employee

 

class EmployeesDBLogic:
    def __init__(self):
        self.employees = []
        self.base_dir = os.path.dirname(os.path.dirname(__file__)) 
        self.file_path = os.path.join(self.base_dir, 'Data_Layer/Databases', 'Employees.json')

    def loadEmployeeLog(self) -> None:
        """ Function loads all saved employees from DB and turns back into class instances of Employee and saves it internally """
        with open(self.file_path, "r") as employeeDBOpen:
            employees_list = json.load(employeeDBOpen)
        
        for employee in employees_list:
            self.employees.append(Employee(*employee.values()))

        # Need to split into contractor logic

    def saveEmployees(self) -> None:
        """ Function saves all instances of the employee class saved in self.employees in dictionary form into json Database """
        Employees = [employee.Employee_dict() for employee in self.employees] 

        with open(self.file_path, 'w') as file:
            json.dump(Employees, file, indent=4)
        
        # Need to split into contractor logic

    def createEmployee(self, params, type) -> None:
        """This function takes in a list of parameters and creates an employee and stores in the json DB"""
        # Params should be a list of all the variables Employee() class needs to initialize in the correct order
        if type != "Contractor":
            self.employees.append(Employee(*params))
            self.saveEmployees()
        else:
            # Contractor logic here
            pass

    def updateEmployee(self, params) -> None:
        """This function takes in a list of parameters, some may be new some may still be the older ones and stores them in the json DB"""
        # Need to split into instances of General Employee/Manger and Contractor as they have different parameters
        for employee in self.employees:
            if employee.employeeID == params[0]:
                employee.employeeID =
        
    def removeEmployee(self, ID) -> None:
        """ We take in the ID of the employee we want to remove, find it, delete it from the internal list and save the internal list to DB"""
        # Start with finding the index of the employee we want to remove in the self.employees internal list
        index_to_remove = -1
        for index, employee in enumerate(self.employees):
            if employee.employeeID == ID:
                index_to_remove = index
                break
        # Remove that employee from the internal list
        if index_to_remove != -1:
            del self.employee[index_to_remove]
        # Save the modified internal list to the DB
        self.saveEmployees()


ui = EmployeesDBLogic()
#ui.saveEmployees()
ui.loadEmployeeLog()
