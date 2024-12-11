from os import system, name
from Logic_Layer.LogicLayerAPI import LogicLayerAPI
from .Displays import Displays
from prettytable import PrettyTable

# here is the UI logic where the viewing and filtering functions are

class ViewUILogic:
    def __init__(self):
        self.LogicLayerWrapper = LogicLayerAPI()
        self.Displays = Displays()

    def viewMenu(self):
        self.clearTerminal()
        while True:
            # here is the viewing menu of the manager, the user can see all of the things they are able to View
            main_menu = PrettyTable()
            main_menu.title = " Viewing menu - Manager Position"
            main_menu.header = False
            main_menu.add_row(["1: View all Employees"])
            main_menu.add_row(["2: View all Contractors"])
            main_menu.add_row(["3: View all Properties"])
            main_menu.add_row(["4: View all Maintenance Tasks"])
            main_menu.add_row(["5: View all Scheduled Maintenance Tasks"])
            main_menu.add_row(["6: View all Maintenance Reports"])
            main_menu.add_row(["B: Go back"])
            main_menu.add_row(["Q: Quit"])

            main_menu.align = "l"
            print(main_menu)

            # print("1: View all Employees")
            # print("2: View all Contractors")
            # print("3: View all Properties")
            # print("4: View all Maintenance Tasks")
            # print("5: View all Scheduled Maintenance Tasks")
            # print("6: View all Maintenance Reports")
            # print("B: To Go Back")
            # print("Q: To Quit\n")


            # Here the user can choose what they want to view
            print("Which one would you like to view?")
            user_choice = input("Choice: ")

            # if the user chooses to quit the program
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            # if the user chooses to go back in the program
            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break

            elif user_choice == "1":
                self.displayEmployees() # Show them the complete list and then ask if they want any more filtering....
                self.filterEmployees()
            elif user_choice == "2":
                self.displayContractors() # Show them the complete list and then ask if they want any more fliltering...
                self.filterContractors()
            elif user_choice == "3":
                self.displayProperties() # Show them the complete list and then ask if they want any more filtering....
                self.filterProperties()
            elif user_choice == "4":
                self.displayMaintenanceTasks() #Show them the complete list and then ask if they want any more filtering....
                self.filterMaintenanceTasks()
            elif user_choice == "5":
                self.displayMaintenanceSchedules() # Show them the complete list and then ask if they want any more filtering....
                self.filterMaintenanceSchedules()
            elif user_choice == "6":
                self.displayMaintenanceReports() # Show them the complete list and then ask if they want any more filtering....
                self.filterMaintenanceReports()
            else:
                print("Invalid Input")
            
    def clearTerminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def displayEmployees(self):
        employees = self.LogicLayerWrapper.getEmployeeData()
        for employee in employees:
            self.Displays.printEmployee(employee)

    def displayContractors(self):
        contractors = self.LogicLayerWrapper.getContractorData()
        for contractor in contractors:
            self.Displays.printContractor(contractor)

    def displayProperties(self):
        properties = self.LogicLayerWrapper.getPropertyData()
        for property in properties:
            self.Displays.printProperty(property)

    def displayMaintenanceTasks(self):
        maintenanceTasks = self.LogicLayerWrapper.getMaintenanceTaskData()
        for task in maintenanceTasks:
            self.Displays.printMaintenanceTask(task)

    def displayMaintenanceSchedules(self):
        maintenanceSchedules = self.LogicLayerWrapper.getMaintenanceScheduleData()
        for schedule in maintenanceSchedules:
            self.Displays.printMaintenanceSchedule(schedule)

    def displayMaintenanceReports(self):
        maintenanceReports = self.LogicLayerWrapper.getMaintenanceReportData()
        for report in maintenanceReports:
            self.Displays.printMaintenanceReport(report)

    def filterEmployees(self):

        # Here is the information menu of the manager, this is if they want to filter employees additionally
        info_menu_em = PrettyTable()
        info_menu_em.title = " Additional Information on Employees - Manager Position"
        info_menu_em.header = False
        info_menu_em.add_row(["1: View information of a specific Employee by ID"])
        info_menu_em.add_row(["2: View all tasks an Employee has worked on"])
        info_menu_em.add_row(["B: Go Back"])
        info_menu_em.add_row(["Q: Quit"])

        info_menu_em.align = "l"
        print(info_menu_em)


        # print("\n-------------------------------------------------------")
        # print("1: View additional information of a specific Employee")
        # print("2: View all tasks an Employee has worked on")
        # print("B: To Go Back")
        # print("Q: To Quit")
        # print("-------------------------------------------------------\n")

        while True:
            # The user can choose what they want to do
            user_choice = input("Choice: ")

            # User chooses to quit the program
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            # The user chooses to go back in the program 
            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break

            # The user chooses to filter additionally the employees
            elif user_choice == "1":
                # asking what employee id they want to look up
                ID = input("ID of the Employee you want to look up: ")

                # if the user chooses to quit the program
                if ID.lower() == "q":
                    print("Quitting")
                    exit()

                # if the user chooses to go back in the program
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    employee = self.LogicLayerWrapper.getEmployeebyID(ID)
                    self.Displays.printEmployee(employee)
                except ValueError as error:
                    print(error)

            # if the chooses to view tasks an employee has worked on
            elif user_choice == "2":
                # asking for id of that employee
                ID = input("ID of the Employee you want to show tasks for: ")

                # user chooses to quit the program
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                #user chooses to go back in the program
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    tasks = self.LogicLayerWrapper.getTasksForEmployeeID(ID) # Takes in x amount of Maintenance Tasks an employee has worked
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter
                except ValueError as error:
                    print(error)
            else:
                print("Invalid Input")

    def filterContractors(self):

        # Here is the menu for additional information on contractors
        # Here you can view specific contractor or a task a specific contractor has worked on

        info_menu_co = PrettyTable()
        info_menu_co.title = " Additional Information on Contractors - Manager Position"
        info_menu_co.header = False
        info_menu_co.add_row(["1: View information of a specific Contractor by ID"])
        info_menu_co.add_row(["2: View all tasks an Contractor has worked on"])
        info_menu_co.add_row(["B: Go Back"])
        info_menu_co.add_row(["Q: Quit"])

        info_menu_co.align = "l"
        print(info_menu_co)

        # print("\n-------------------------------------------------------")
        # print("1: View additional information of a specific Contractor")
        # print("2: View all tasks a Contractor has worked on")
        # print("B: Go Back")
        # print("Q: Quit")
        # print("-------------------------------------------------------\n")


        
        while True:
            # asking the user what they want to do
            user_choice = input("Choice: ")
            # user can choose to quit the program
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            # user can choose to go back in the program
            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            
            # user can choose to look up information on a specific contractor
            elif user_choice == "1":
                # program asks for the id of the contractor
                ID = input("ID of the Contractor you want to look up: ")

                # the user can choose to quit
                if ID.lower() == "q":
                    print("Quitting")
                    exit()

                # the user can choose to go back
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    contractor = self.LogicLayerWrapper.getContractorbyID(ID)
                    self.Displays.printContractor(contractor)
                except ValueError as error:
                    print(error)

            # user can choose to view additional information on tasks of a specific contractor
            elif user_choice == "2":
                # asking the id of that contractor
                ID = input("ID of the Contractor you want to show tasks for: ")

                # the user can choose to quit the program
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                # the user can choose to go back in the program
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    tasks = self.LogicLayerWrapper.getTasksForContractorID(ID)# Takes in x amount of Maintenance Tasks a contractor has worked 
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter
                except ValueError as error:
                    print(error)
            # if the input is something else than is on the table it is an invalid input
            else:
                print("Invalid Input")

    def filterProperties(self):

        # here is the menu to filter properties by a specific ID or the maintenance task

        info_menu_pr = PrettyTable()
        info_menu_pr.title = " Additional Information on Properties - Manager Position"
        info_menu_pr.header = False
        info_menu_pr.add_row(["1: View information of a specific Property by ID"])
        info_menu_pr.add_row(["2: View all Maintenance on a specific Property"])
        info_menu_pr.add_row(["B: Go Back"])
        info_menu_pr.add_row(["Q: Quit"])

        info_menu_pr.align = "l"
        print(info_menu_pr)




        # print("\n-------------------------------------------------------")
        # print("1: View additional information of a specific Property")
        # print("2: View all Maintenance on a specific Property")
        # print("B: Go Back")
        # print("Q: Quit")
        # print("-------------------------------------------------------\n")
        while True:
            # asking the choice of the user
            user_choice = input("Choice: ")
            # the user can quit if they want 
            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            # the user can choose to go back in the program
            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            
            # the user can choose to look up a property by their ID
            elif user_choice == "1":
                # asking for the ID
                ID = input("ID of the Property you want to look up: ")

                # the user can choose to quit
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                # the user can choose to go back
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    property = self.LogicLayerWrapper.getPropertyByID(ID)
                    self.Displays.printProperty(property)
                except ValueError as error:
                    print(error)

            # the user can choose to look up the tasks on the property by ID
            elif user_choice == "2":
                # asking for the ID of the property
                print("Be aware that ID's of properties are starting from 1 and up.")
                ID = input("ID of the Property you want to show tasks for: ")

                # The user can choose to quit the program
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                # the user can choose to go back in the program
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    tasks = self.LogicLayerWrapper.getTasksForPropertyID(ID) # Takes in x amount of Maintenance Tasks done on specific property
                    for task in tasks:
                        self.Displays.printMaintenanceTask(task)
                    self.dateFilter(tasks) # get the datefilter
                except ValueError as error:
                    print(error)
            # if the input of the user is not valid or not in the right form it will return invalid input
            else:
                print("Invalid Input")
    
    def filterMaintenanceTasks(self):

        # here is the filtering for maintenance tasks. here you can look up a maintenance task
        info_menu_ma = PrettyTable()
        info_menu_ma.title = " Additional Information on Maintenance Task - Manager Position"
        info_menu_ma.header = False
        info_menu_ma.add_row(["1: View information of a specific Maintenance Task by ID"])
        info_menu_ma.add_row(["B: Go Back"])
        info_menu_ma.add_row(["Q: Quit"])

        info_menu_ma.align = "l"
        print(info_menu_ma)


        # print("\n-------------------------------------------------------")
        # print("1: View additional information of a specific MaintenanceTask") ## IS THIS NEEDED ?
        # print("B: Go Back")
        # print("Q: Quit")
        # print("-------------------------------------------------------\n")
        while True:
            # the option the user chose will be input
            user_choice = input("Choice: ")
            #the user can choose to quit the program at any time
            if user_choice.lower() == "q":
                print("Qutting")
                exit()
            # the user can choose to go back in the program at any time
            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            # the user can choose to look up a task by the id
            elif user_choice == "1":
                print("Be aware that ID's of maintenance tasks are starting from 1 and up.")
                ID = input("ID of the Maintenance Task you want to look up: ")

                #user can quit at any moment
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                # user can go back
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    task = self.LogicLayerWrapper.getMaintenanceTaskByID(ID)
                    self.Displays.printMaintenanceTask(task)
                except ValueError as error:
                    print(error)
            # anything else is an invalid input and will return invalid input.
            else:
                print("Invalid Input")

    def filterMaintenanceSchedules(self):

        # here is the menu to see additional information on a specific maintenance schedule

        info_menu_ms = PrettyTable()
        info_menu_ms.title = " Additional Information on Maintenance Schedule - Manager Position"
        info_menu_ms.header = False
        info_menu_ms.add_row(["1: View information of a Maintenance Schedule by ID"])
        info_menu_ms.add_row(["B: Go Back"])
        info_menu_ms.add_row(["Q: Quit"])

        info_menu_ms.align = "l"
        print(info_menu_ms)




        # print("\n-------------------------------------------------------")
        # print("1: View additional information of a specific MaintenanceSchedule") ## IS THIS NEEDED ?
        # print("B: Go Back")
        # print("Q: Quit")
        # print("-------------------------------------------------------\n")



        while True:
            # user can choose here
            user_choice = input("Choice: ")
            # user can choose to quit the program
            if user_choice.lower() == "q":
                print("Qutting")
                exit()
            # user can choose to go back in the program
            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            # user can choose to view maintenance schedule by thei ID
            elif user_choice == "1": 
                print("Be aware that ID's of maintenance schedules are starting from 1 and up.")
                ID = input("ID of the Maintenance Schedule you want to look up: ")
                # user can choose to quit the program
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                # user can choose to go back in the program
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    task = self.LogicLayerWrapper.getMaintenanceScheduleByID(ID)
                    self.Displays.printMaintenanceSchedule(task)
                except ValueError as error:
                    print(error)
            # an invalid input will lead to a return in invalid input
            else:
                print("Invalid Input")            

    def filterMaintenanceReports(self):

        # Here is the menu for the additional information on a maintenence reports

        info_menu_mr = PrettyTable()
        info_menu_mr.title = " Additional Information on Maintenance Report - Manager Position"
        info_menu_mr.header = False
        info_menu_mr.add_row(["1: View information of a specific Maintenance Report by ID"])
        info_menu_mr.add_row(["B: Go Back"])
        info_menu_mr.add_row(["Q: Quit"])

        info_menu_mr.align = "l"
        print(info_menu_mr)


        # print("\n-------------------------------------------------------")
        # print("1: View additional information of a specific MaintenanceReport") ## IS THIS NEEDED ?
        # print("B: Go Back")
        # print("Q: Quit")
        # print("-------------------------------------------------------\n")
        while True:
            # here they ask what they want to do
            user_choice = input("Choice: ")
            # the user can choose to quit the program
            if user_choice.lower() == "q":
                print("Qutting")
                exit()
            # the user can choose to go back by one in the program
            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            # the user can choose to look up a maintenance report by ID
            elif user_choice == "1":
                print("Be aware that ID's of maintenance reports are starting from 1 and up.")
                ID = input("ID of the Maintenance Report you want to look up: ")
                # the user can choose to quit
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                # the user can choose to go back in the program
                elif ID.lower() == "b":
                    self.clearTerminal()
                    continue
                try:
                    report = self.LogicLayerWrapper.getMaintenanceReportByID(ID)
                    self.Displays.printMaintenanceReport(report)
                except ValueError as error:
                    print(error)
            # any invalid input is going to let the user know
            else:
                print("Invalid Input")
    
    def dateFilter(self, tasks):

        # Here is the menu for additional information on the time period
        date_filter = PrettyTable()
        date_filter.title = " Additional Information on a time period - Manager Position"
        date_filter.header = False
        date_filter.add_row(["1: View tasks over a specific time period by ID"])
        date_filter.add_row(["B: Go Back"])
        date_filter.add_row(["Q: Quit"])

        date_filter.align = "l"
        print(date_filter)

        # print("\n-------------------------------------------------------")
        # print("1: View tasks over a specific time period")
        # print("B: Go Back")
        # print("Q: Quit")
        # print("-------------------------------------------------------\n")


        while True:
            # here they ask what the user wants to do
            user_choice = input("Choice: ")
            # user can quit the program
            if user_choice.lower() == "q":
                print("Qutting")
                exit()
            # user can go back in the program
            elif user_choice.lower() == "b":
                print("Going back")
                self.clearTerminal()
                break
            # user can choose to see maintenence schedule by ID
            elif user_choice == "1":
                print(" be aware that Start Date and End Date needs to be in the form of X:XX or XX:XX")
                startDate = input("Start Date: ") 
                endDate = input("End Date: ")
                filtered_tasks = self.LogicLayerWrapper.filterMaintenanceTasksDates(tasks, startDate, endDate)
                for filtered_task in filtered_tasks:
                    self.Displays.printMaintenanceTask(filtered_task)
            else:
                # any invalid input will lead to a notice of that, so user knows they are not doing it right.
                print("Invalid Input")