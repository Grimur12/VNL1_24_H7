## Test to create an employee
from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI

class UItest:
    def __init__(self) -> None:
        self.logicLayerWrapper = LogicLayerAPI()

    def display_temp_employee(self, temp, error = None):

        self.clear_terminal()

        print("\n--- Adding a new Employee ---")
        print(f"ID: {temp.employeeID}")
        print(f"Name: {temp.name}")
        print(f"Social Security: {temp.socialSecurity}")
        print(f"Address: {temp.address}")
        print(f"Home Phone: {temp.atHomePhone}")
        print(f"GSM Phone: {temp.gsmPhone}")
        print(f"Email: {temp.email}")
        print(f"Work Location: {temp.workLocation}")
        print(f"Type: {temp.type}")
        print("--------------------------\n")
        
        if error:
            print(f"Error: {error}\n")

    def clear_terminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def createEmployee(self):
        count = 0
        temp = self.logicLayerWrapper.getTempEmployee()
        error_message = None
        while count < 8:
            self.display_temp_employee(temp, error_message)
            user_input = input("Information: ")
            try:
                if self.logicLayerWrapper.validateEmployeeInput(user_input, count, temp):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        self.display_temp_employee(temp, error_message)
        self.logicLayerWrapper.createEmployee(temp)
        print("You have successfully created the employee")
    

    def updateEmployee(self, ID):
        employee = self.logicLayerWrapper.getEmployeebyID(ID)
        print(employee)
        userInput = int(input("Press 0 to change name:"))
        newParam = input("Write new name:")
        self.logicLayerWrapper.validateEmployeeInput(newParam, userInput, employee)
        print(employee)
        self.logicLayerWrapper.update_employee_data(employee)



    def displayEmployees(self):
        employees = self.logicLayerWrapper.getEmployeeData()
        for employee in employees:
            print(employee)

    def run(self):
        while True:
            print("Type 1 to create an Employee")
            print("Type 2 to update Employee")
            print("Type 3 to view all Employees")
            print("q to quit")
            user_choice = input("Type 1, 2, 3 or q: ")
            if user_choice == "1":
                self.createEmployee()
            elif user_choice == "2":
                ID = input("Pls input ID of user to update: ")
                self.updateEmployee(ID)
            elif user_choice == "3":
                self.displayEmployees()
            elif user_choice == "q":
                print("Quitting")
                break
            else:
                print("Invalid Input")


if __name__ == "__main__":
    ui = UItest()
    print("Type 1 to Create an Employee")
    print("Type q to quit the program")
    initial_input = input()
    if initial_input == "1":
        ui.run()

