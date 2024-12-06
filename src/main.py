from UI_Layer.ContractorUILogic import ContractorUILogic
from UI_Layer.EmployeeUILogic import EmployeeUILogic
from UI_Layer.ManagerUILogic import ManagerUILogic
from UI_Layer.ViewUILogic import ViewUILogic

class main:
    def __init__(self):
        self.ContractorUI = ContractorUILogic()
        self.EmployeeUI = EmployeeUILogic()
        self.ManagerUI = ManagerUILogic()
        self.ViewUI = ViewUILogic()

if __name__ == "__main__":
    start = main()
    start.ViewUI.clearTerminal() 
    while True:
        print("1: If you are a Manager")
        print("2: If you are an Employee")
        print("3: If you are a Contractor")
        print("Q: To quit")

        initial_input = input("Choice: ")
        if initial_input.lower() == "q":
            print("Quitting")
            break
        elif initial_input == "1":
            start.ManagerUI.run()
        elif initial_input == "2":
            start.EmployeeUI.run()
        elif initial_input == "3":
            start.ContractorUI.run()
        else:
            print("Invalid Input.")
