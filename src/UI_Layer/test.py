## Test to create an employee
from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI

class UItest:
    def __init__(self) -> None:
        self.logicLayerWrapper = LogicLayerAPI()

    def display_temp_employee(self, temp):
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

    def clear_terminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def createEmployee(self):
        count = 0
        temp = self.logicLayerWrapper.getTempEmployee()
        while count < 8:
            self.clear_terminal()
            self.display_temp_employee(temp)
            user_input = input("Information: ")
            try:
                if self.logicLayerWrapper.validateEmployeeInput(user_input, count):
                    count +=1
            except ValueError as error:
                print(f"Error: {error}")
                continue
        self.clear_terminal()
        self.display_temp_employee(temp)
        self.logicLayerWrapper.createEmployee()
        print("You have successfully created the employee")
    
    def displayEmployees(self):
        employees = self.logicLayerWrapper.getEmployeeData()
        for employee in employees:
            print(employee)

    def run(self):
        while True:
            print("Type 1 to create an Employee")
            print("Type 2 to create a Contractor")
            print("Type 3 to view all Employees")
            print("q to quit")
            user_choice = input("Type 1 or q: ")
            if user_choice == "1":
                self.createEmployee()
            elif user_choice == "2":
                print("Not implemented... try again later")
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

