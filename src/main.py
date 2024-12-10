from UI_Layer.ContractorUILogic import ContractorUILogic
from UI_Layer.EmployeeUILogic import EmployeeUILogic
from UI_Layer.ManagerUILogic import ManagerUILogic
from UI_Layer.ViewUILogic import ViewUILogic
from prettytable import PrettyTable

# Main program

class main:
    def __init__(self):
        self.ContractorUI = ContractorUILogic()
        self.EmployeeUI = EmployeeUILogic()
        self.ManagerUI = ManagerUILogic()
        self.ViewUI = ViewUILogic()

if __name__ == "__main__":
    start = main()
    invalid = False
    while True: 
 
        start.ViewUI.clearTerminal()

        # print("------------ Welcome to NAN Air ------------")
        # print("--------------------------------------------")
        # print("Are you a manager, employee or a contractor?")
        # print("1: Manager")
        # print("2: Employee")
        # print("3: Contractor")
        # print("Q: To quit\n")
        # print("-------------------------------------------- ")
        # print("-------------------------------------------- ")
        
        main_menu = PrettyTable()
        main_menu.title = "Main Menu"
        main_menu.header = False
        main_menu.add_row(["1: Manager"])
        main_menu.add_row(["2: Employee"])
        main_menu.add_row(["3: Contractor"])
        main_menu.add_row(["Q: Quit"])

        main_menu.align = "l"
        print(main_menu)

        if invalid:
            print("Error: Invalid Input\n")

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
            invalid = True
            
