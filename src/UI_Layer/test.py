## Test to create an employee
from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI

class UItest:
    def __init__(self) -> None:
        self.logicLayerWrapper = LogicLayerAPI()

    def display_temp_employee(self, temp, error = None):

        self.clear_terminal()

        print("\n--- Adding a new Employee ---")
        print(temp)            
        print("--------------------------\n")

        if error:
            print(f"Error: {error}\n")

    def updateEmployeeMenu(self, employee, error = None):
        """ Turns the class into a string to print out with, mainly for UI display """
        self.clear_terminal()
        print(f"""
--- Updating employee {employee.employeeID} ---
You can not change Employee's ID, Social Security or Type
ID: {employee.employeeID}
1.Name: {employee.name}
Social Security: {employee.socialSecurity}
3.Address: {employee.address}
4.Home Phone: {employee.atHomePhone}
5.GSM Phone: {employee.gsmPhone}
6.Email: {employee.email}
7.Work Location: {employee.workLocation}
Type: {employee.type}
B: To Go Back
Q: To Quit\n
------""")
        if error:
            print(f"Error: {error} \n")
    
    def updateContractorMenu(self, employee, error = None):
        """ Turns the class into a string to print out with, mainly for UI display """
        self.clear_terminal()
        print(f"""
--- Updating employee {employee.employeeID} ---
You can not change Employee's ID, Social Security or Type
ID: {employee.employeeID}
1.Name: {employee.name}
Social Security: {employee.socialSecurity}
3.Address: {employee.address}
4.Home Phone: {employee.atHomePhone}
5.GSM Phone: {employee.gsmPhone}
6.Email: {employee.email}
7.Work Location: {employee.workLocation}
Type: {employee.type}
8.Previous Task: {employee.previousTask}
9.Performance Rating: {employee.performanceRating}
10.Contractor Contact: {employee.contractorContact}
11.Opening Hours: {employee.openingHours}
B: To Go Back
Q: To Quit
------""")
        if error:
            print(f"Error: {error} \n")


    def employeeMenu(self):
        self.clear_terminal()
        while True:
            print("Type 1 to create an Employee")
            print("Type 2 to create a Manager")
            print("Type 3 to create a Contractor")
            print("Type 4 to update an Employee")
            print("Type 5 to update a Contractor")
            print("Type 6 to view all Employees")
            print("B to go back")
            print("Q to Quit")
            employee_user_choice = input("Choice: ")
            
            if employee_user_choice.lower() == "q":
                print("Quitting")
                exit()
            elif employee_user_choice.lower() == "b":
                break

            elif employee_user_choice in ["1","2","3"]:
                self.createEmployee(employee_user_choice)
                self.clear_terminal()
            elif employee_user_choice == "4":
                ID = input("ID of the Employee to update: ")
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clear_terminal()
                    continue
                self.updateEmployee(ID)
                self.clear_terminal()
            elif employee_user_choice == "5":
                ID = input("ID of the Contractor to update: ")
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clear_terminal()
                    continue
                self.updateContractor(ID)
                self.clear_terminal()
            elif employee_user_choice == "6":
                self.clear_terminal()
                self.displayEmployees()
            else:
                print("Invalid Input")

    def propertyMenu(self):
        self.clear_terminal()
        while True:
            print("Type 1 to create a Property")
            print("Type 2 to update a Property")
            print("Type 3 to view all Properties")
            print("B to go back")
            print("Q to Quit")
            print("NOT IMPLEMENTED YET, Press B to go back or Q to quit")
            employee_user_choice = input("Choice: ")

            if employee_user_choice.lower() == "q":
                print("Quitting")
                exit()
            elif employee_user_choice.lower() == "b":
                break
        
    def maintenanceMenu(self):
        self.clear_terminal()
        while True:
            print("Type 1 to create a Maintenance Task")
            print("Type 2 to add a Maintenane Task to a Schedule")
            print("Type 3 to update a Maintenance Schedule")
            print("Type 4 to view all Maintenance Tasks")
            print("Type 5 to view all Scheduled Maintainance Tasks")
            print("B to go back")
            print("Q to Quit")
            print("NOT IMPLEMENTED YET, Press B to go back or Q to quit")
            employee_user_choice = input("Choice: ")

            if employee_user_choice.lower() == "q":
                print("Quitting")
                exit()
            elif employee_user_choice.lower() == "b":
                break

    def clear_terminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def createEmployee(self,type_of_employee):

        # Type of employee should be "1" for Employee, "2" for Contractor 
        count = 1
        temp = self.logicLayerWrapper.getTempEmployee(type_of_employee)
        error_message = None
        if type_of_employee == "3":
            max_parameters = 12
        else:
            max_parameters = 8
        while count < max_parameters:
            self.display_temp_employee(temp, error_message)
            userInput = input("Information: ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput.lower() == "b":
                break
            try:
                if self.logicLayerWrapper.validateEmployeeInput(userInput, count, temp):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        if userInput.lower() != "b":
            self.display_temp_employee(temp, error_message)
            self.logicLayerWrapper.createEmployee(temp)
            print("You have successfully created the employee")

    def updateEmployee(self, ID):
        while True:
            try:
                employee = self.logicLayerWrapper.getEmployeebyID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Employee to update: ")
                continue
        
        error_message = None
        while True:
            self.updateEmployeeMenu(employee, error_message)
            userInput = input("Number of the attribute you want to change: ")
            
            if userInput == "Q" or userInput == "q":
                exit() ## QUIT...
            elif userInput == "B":
                print("Going back")
                break ## Go back one

            if userInput in ["1", "3", "4", "5", "6", "7"]:

                newParam = input("New Information: ").strip()
                try:
                    self.logicLayerWrapper.validateEmployeeInput(newParam, userInput, employee)
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"
        if userInput.lower() != "b":
            self.logicLayerWrapper.update_employee_data(employee)

    def updateContractor(self, ID):
        while True:
            try:
                employee = self.logicLayerWrapper.getContractorbyID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Employee to update: ")
                continue

        error_message = None
        while True:
            self.updateContractorMenu(employee, error_message)
            userInput = input("Number of the attribute you want to change: ")

            if userInput == "Q" or userInput == "q":
                exit() ## QUIT...
            elif userInput == "B" or "b":
                print("Going back")
                break ## Go back one

            if userInput in ["1", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:

                newParam = input("New Information: ").strip()
                try:
                    self.logicLayerWrapper.validateEmployeeInput(newParam, userInput, employee)
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"
        if userInput.lower() != "b":
            self.logicLayerWrapper.update_employee_data(employee)

    def displayEmployees(self):
        employees = self.logicLayerWrapper.getEmployeeData()
        for employee in employees:
            print(employee)

    def run(self):
        while True:
            print("Type 1 to access Employee features")
            print("Type 2 to access Maintenance features")
            print("Type 3 to access Property features")
            print("B to go Back")
            print("Q to quit")
            user_choice = input("Type 1, 2, 3 or q: ")
            # Exit out of the loop

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            if user_choice.lower() == "b":
                print("Going back")
                break

            if user_choice == "1":
                self.employeeMenu()
            elif user_choice == "2":
                self.maintenanceMenu()
            elif user_choice == "3":
                self.propertyMenu()
            else:
                print("Invalid Input")


if __name__ == "__main__":
    ui = UItest()
    ui.clear_terminal()
    while True:
        print("1: If you are a Manager")
        print("Type Q to quit the program")

        initial_input = input("Choice: ")
        if initial_input.lower() == "q":
            print("Quitting")
            break
        elif initial_input == "1":
            ui.clear_terminal()
            ui.run()
        else:
            print("Invalid Input.")
            
        

