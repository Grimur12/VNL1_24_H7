
from os import system, name
from prettytable import PrettyTable
# Need to make all these displays look better 
class Displays:
    def __init__(self):
        pass

    def editContractorMenu(self, contractor, error = None):
        """ Turns the class into a string to print out with, mainly for UI display """
        self.clearTerminal()
        print(f"""
--- Updating Contractor {contractor.employeeID} ---
You can not change Contractor's ID, Social Security or Type
Contractor Number: {contractor.employeeID}
1.Name: {contractor.name}
Social Security: {contractor.socialSecurity}
3.Address: {contractor.address}
4.Home Phone: {contractor.atHomePhone}
5.GSM Phone: {contractor.gsmPhone}
6.Email: {contractor.email}
7.Work Location: {contractor.workLocation}
Type: {contractor.type}
8.Previous Task: {contractor.previousTask}
9.Performance Rating: {contractor.performanceRating}
10.Contractor Contact: {contractor.contractorContact}
11.Opening Hours: {contractor.openingHours}
B: To Go Back
Q: To Quit
D: To Quit Chaning and Save Changes\n
------""")
        if error:
            print(f"Error: {error} \n")

    def editEmployeeMenu(self, employee, error = None):
        """ Turns the class into a string to print out with, mainly for UI display """
        self.clearTerminal()
        print(f"""
--- Updating employee {employee.employeeID} ---
You can not change Employee's ID, Social Security or Type
Employee Number: {employee.employeeID}
1.Name: {employee.name}
Social Security: {employee.socialSecurity}
3.Address: {employee.address}
4.Home Phone: {employee.atHomePhone}
5.GSM Phone: {employee.gsmPhone}
6.Email: {employee.email}
7.Work Location: {employee.workLocation}
Type: {employee.type}
B: To Go Back
Q: To Quit
D: To Quit Chaning and Save Changes\n
------""")
        if error:
            print(f"Error: {error} \n")

    def editPropertyMenu(self, property, error = None):
        
        self.clearTerminal()
        print(f"""
--- Updating Property {property.propertyID} ---
Property Number: {property.propertyID}
1.Name: {property.nameOfProperty}
2.Location: {property.location}
3.Availability: {property.availability}
4.Pool: {property.hasAPool}
5.Hot Tub: {property.hasATub}
6.Ovens: {property.hasOvens}
B: To Go Back
Q: To Quit
D: To Quit Chaning and Save Changes\n
------""")
        if error:
            print(f"Error: {error} \n")
        
    def editMaintenanceTaskMenu(self, maintenanceTask, error = None):

        self.clearTerminal()
        print(f"""
--- Updating Maintenance Task {maintenanceTask.maintenanceID} ---
You can not change the Number, Maintenance done on Property, Start- or EndDate, Status or if its recurring or not
Maintenance Number: {maintenanceTask.maintenanceID}
Maintenance done on Property Number: {maintenanceTask.propertyID}
2.Description of Task: {maintenanceTask.description}
Start Date: {maintenanceTask.startDate}
End Date: {maintenanceTask.endDate}
Status of Maintenance: {maintenanceTask.statusMaintenance}
6.Priorty: {maintenanceTask.priority}
Recurring: {maintenanceTask.recurring}
B: To Go Back
Q: To Quit
D: To Quit Chaning and Save Changes\n
------""")
        if error:
            print(f"Error: {error}\n")

    def editMaintenanceScheduleMenu(self, schedule, error = None):

        self.clearTerminal()
        print(f"""
--- Updating Maintenance Schedule {schedule.maintenanceScheduleID} ---
You can not change Schedule Number, Scheduled Task, Type of Maintenance Task or the Start Date
Maintenance Schedule Number: {schedule.maintenanceScheduleID}
Scheduled on Maintenance Task Number: {schedule.maintenanceID}
Type of Maintenance Task: {schedule.taskType}
3.Frequency of Maintenance Task: {schedule.frequency}
Start Date of Scheduled Maintenance: {schedule.startDate}
B: To Go Back
Q: To Quit
D: To Quit Chaning and Save Changes\n
------""")
        if error:
            print(f"Error: {error}\n")


    def display_temp_employee(self, temp, error = None):

        self.clearTerminal()

        print("\n--- Adding a new Employee ---")
        print(temp)            
        print("--------------------------\n")

        if error:
            print(f"Error: {error}\n")

    def display_temp_property(self, temp, error = None):
        
        self.clearTerminal()

        print("\n--- Adding a new Property ---")
        print(f"Property Number: {temp.propertyID}")
        print(f"Name: {temp.nameOfProperty}")
        print(f"Location: {temp.location}")
        print(f"Availability: {temp.availability}")
        print(f"Does it have a pool: {temp.hasAPool}")
        print(f"Does it have a hot Tub: {temp.hasATub}")
        print(f"Does it have ovens: {temp.hasOvens}")            
        print("--------------------------\n")

        if error:
            print(f"Error: {error}\n")

    def display_temp_maintenanceTask(self, temp, error = None):
        
        self.clearTerminal()

        print("\n--- Adding a new Maintenance Task ---")
        print(f"Maintenance Number: {temp.maintenanceID}")
        print(f"Maintenance done on Property Number: {temp.propertyID}")
        print(f"Description of Task: {temp.description}")
        print(f"Start Date: {temp.startDate}")
        print(f"End Date: {temp.endDate}")
        print(f"Status of Maintenance: {temp.statusMaintenance}")
        print(f"Priorty: {temp.priority}")
        print(f"Recurring: {temp.recurring}")
        print("--------------------------\n")

        if error:
            print(f"Error: {error}\n")

    def display_temp_maintenanceSchedule(self, temp, error = None):

        self.clearTerminal()

        print("\n--- Adding a new Maintenance Schedule ---")
        print(f"Maintenance Schedule Number: {temp.maintenanceScheduleID}")
        print(f"Scheduled on Maintenance Task Number: {temp.maintenanceID}")
        print(f"Type of Maintenance Task: {temp.taskType}")
        print(f"Frequency of Maintenance Task: {temp.frequency}")
        print(f"Start Date of Scheduled Maintenance: {temp.startDate}")
        print("--------------------------\n")

        if error:
            print(f"Error: {error}\n")

    def display_temp_maintenanceReport(self, temp, error = None):

        self.clearTerminal()

        print("\n--- Adding a new Maintenance Report ---")
        print(f"maintenanceReportID: {temp.maintenanceReportID}")
        print(f"maintenanceID: {temp.maintenanceID}")
        print(f"employeeID: {temp.employeeID}")
        print(f"materialCost: {temp.materialCost}")
        print(f"contractorID: {temp.contractorID}")
        print(f"contractorCost: {temp.contractorCost}")
        print(f"readyToClose: {temp.readyToClose}")
        print(f"supervisorClosed: {temp.supervisorClosed}")
        print(f"supervisorFeedback: {temp.supervisorFeedback}")
        print("--------------------------\n")

        if error:
            print(f"Error: {error}\n")


    def printProperty(self, property):

        print("\n--- Property Information ---")
        print(f"Property Number: {property.propertyID}")
        print(f"Name: {property.nameOfProperty}")
        print(f"Location: {property.location}")
        print(f"Availability: {property.availability}")
        print(f"Pool: {property.hasAPool}")
        print(f"Hot Tub: {property.hasATub}")
        print(f"Ovens: {property.hasOvens}")
        print("--------------------------\n") 

    def printEmployee(self, employee):
        
        print("\n--- Employee Information ---")
        print(f"Employee Number: {employee.employeeID}")
        print(f"Name: {employee.name}")
        print(f"Social Security: {employee.socialSecurity}")
        print(f"Address: {employee.address}")
        print(f"Home Phone: {employee.atHomePhone}")
        print(f"GSM Phone: {employee.gsmPhone}")
        print(f"Email: {employee.email}")
        print(f"Work Location: {employee.workLocation}")
        print(f"Type: {employee.type}")
        print("--------------------------\n")

    def printContractor(self, contractor):

        print("\n--- Contractor Information ---")
        print(f"Contractor Number: {contractor.employeeID}")
        print(f"Name: {contractor.name}")
        print(f"Social Security: {contractor.socialSecurity}")
        print(f"Address: {contractor.address}")
        print(f"Home Phone: {contractor.atHomePhone}")
        print(f"GSM Phone: {contractor.gsmPhone}")
        print(f"Email: {contractor.email}")
        print(f"Work Location: {contractor.workLocation}")
        print(f"Type: {contractor.type}")
        print(f"Previous Task: {contractor.previousTask}")
        print(f"Performance Rating: {contractor.performanceRating}")
        print(f"Contractor Contact: {contractor.contractorContact}")
        print(f"Opening Hours: {contractor.openingHours}")
        print("--------------------------\n")

    def printMaintenanceTask(self, task):
        
        print("\n--- Maintenance Task Information ---")
        print(f"Maintenance Number: {task.maintenanceID}")
        print(f"Maintenance done on Property Number: {task.propertyID}")
        print(f"Description of Task: {task.description}")
        print(f"Start Date: {task.startDate}")
        print(f"End Date: {task.endDate}")
        print(f"Status of Maintenance: {task.statusMaintenance}")
        print(f"Priorty: {task.priority}")
        print(f"Recurring: {task.recurring}")
        print("--------------------------\n")

    def printMaintenanceSchedule(self, schedule):
        
        print("\n--- Maintenance Schedule Information ---")
        print(f"Maintenance Schedule Number: {schedule.maintenanceScheduleID}")
        print(f"Scheduled on Maintenance Task Number: {schedule.maintenanceID}")
        print(f"Type of Maintenance Task: {schedule.taskType}")
        print(f"Frequency of Maintenance Task: {schedule.frequency}")
        print(f"Start Date of Scheduled Maintenance: {schedule.startDate}")
        print("--------------------------\n")

    def printMaintenanceReport(self, report):

        print("\n--- Maintenance Report Information ---")
        print(f"Maintenance Report Number: {report.maintenanceReportID}")
        print(f"Report on Maintenance Task Number: {report.maintenanceID}")
        print(f"Employee Number of the Employee that took on the Task: {report.employeeID}")
        print(f"Cost of materials: {report.materialCost}")
        print(f"Contractor Number of the Contractor that took the Task: {report.contractorID}")
        print(f"Cost of the Contrator doing the Task: {report.contractorCost}")
        print(f"Is the Maintenance Task ready to be closed: {report.readyToClose}")
        print(f"Supervisor Has accepted the work done: {report.supervisorClosed}")
        print(f"Feedback on the completed work: {report.supervisorFeedback}")
        print("--------------------------\n")

    def printDestination(self, destination):
        
        print("\n--- Destination Information ---")
        print(f"Destination Number: {destination.destinationID}")
        print(f"Name: {destination.name}")
        print(f"Country: {destination.country}")
        print(f"Timezone: {destination.timezone}")
        print(f"Airport Name: {destination.airportName}")
        print(f"Phone Number: {destination.phoneNumber}")
        print(f"Opening Hours: {destination.openingHours}")
        print(f"Manager Of Destination: {destination.managerOfDestination}")
        print("--------------------------\n")

    def overWriteManager(self):
        print("\nDestination already has a Manager, Would you like to demote him to a General Employee or abort creating a new Manager")
        print("1: To continue creating the new Manager, demoting the current one")
        print("2: To stop the creation process of a new Manager")
        print("Q: To Quit the Program")

    def clearTerminal(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def ContractorMenu(self):
        contractor_menu = PrettyTable()
        contractor_menu.title = "Contractor Menu"
        contractor_menu.header = False
        contractor_menu.add_row(["1: Create a Maintenance Report"])
        contractor_menu.add_row(["2: Viewing features"])
        contractor_menu.add_row(["B: Go Back"])
        contractor_menu.add_row(["Q: Quit"])

        contractor_menu.align = "l"
        return contractor_menu
    
    def EmployeeMenu(self):
        employee_menu = PrettyTable()
        employee_menu.title = " Employee Menu"
        employee_menu.header = False
        employee_menu.add_row(["1: Create a Maintenance Report"])
        employee_menu.add_row(["2: Viewing features"])
        employee_menu.add_row(["B: Go Back"])
        employee_menu.add_row(["Q: Quit"])
        employee_menu.align = "l"
        return employee_menu

    def MainMenu(self):
        main_menu = PrettyTable()
        main_menu.title = "---Welcome to NAN Air!---"
        main_menu.header = False
        main_menu.add_row(["1: Manager"])
        main_menu.add_row(["2: Employee"])
        main_menu.add_row(["3: Contractor"])
        main_menu.add_row(["Q: Quit"])
        main_menu.align = 'l'
        main_menu.max_table_width = 100
        main_menu.bottom_left_junction_char = '|'
        main_menu.bottom_right_junction_char = '|'
        
        return main_menu
    
    def ViewMenu(self):
        view_menu = PrettyTable()
        view_menu.title = " Viewing menu - Manager Position"
        view_menu.header = False
        view_menu.add_row(["1: View all Employees"])
        view_menu.add_row(["2: View all Contractors"])
        view_menu.add_row(["3: View all Properties"])
        view_menu.add_row(["4: View all Maintenance Tasks"])
        view_menu.add_row(["5: View all Scheduled Maintenance Tasks"])
        view_menu.add_row(["6: View all Maintenance Reports"])
        view_menu.add_row(["7: View all Destinations"])
        view_menu.add_row(["B: Go back"])
        view_menu.add_row(["Q: Quit"])  

        return view_menu
    
    def ManagerMainMenu(self):
        manager_menu = PrettyTable()
        manager_menu.title = "Manager menu"
        manager_menu.header = False
        manager_menu.add_row(["1: Create new Properties, Employees or Maintenance Tasks"])
        manager_menu.add_row(["2: Edit Properties, Employees or Maintenance Tasks"])
        manager_menu.add_row(["3: View Properties, Employess or Maintenance Tasks"])
        manager_menu.add_row(["B: Go Back"])
        manager_menu.add_row(["Q: Quit"])
        manager_menu.align = "l"

        return manager_menu
    
    def ManagerAddMenu(self):
        manager_add_menu = PrettyTable()
        manager_add_menu.title = "Create Menu - Manager position"
        manager_add_menu.header = False
        manager_add_menu.add_row(["1: Create a new General Employee "])
        manager_add_menu.add_row(["2: Create a new Manager"])
        manager_add_menu.add_row(["3: Create a new Contractor"])
        manager_add_menu.add_row(["4: Create a new Property"])
        manager_add_menu.add_row(["5: Create a new Maintenance Task"])
        manager_add_menu.add_row(["5: Create a new Maintenance Schedule"])
        manager_add_menu.add_row(["B: Go Back"])
        manager_add_menu.add_row(["Q: Quit"])
        manager_add_menu.align = "l"

        return manager_add_menu

    def ManagerEditMenu(self):
        manager_edit_menu = PrettyTable()
        manager_edit_menu.title = " Edit Menu - Manager Position "
        manager_edit_menu.header = False
        manager_edit_menu.add_row(["1: Edit an Employee or a Manager"])
        manager_edit_menu.add_row(["2: Edit a Contractor"])
        manager_edit_menu.add_row(["3: Edit a Property"])
        manager_edit_menu.add_row(["4: Edit a Maintenance Task"])
        manager_edit_menu.add_row(["5: Edit a Maintenance Schedule"])
        manager_edit_menu.add_row(["6: To close a Maintenance Report"])
        manager_edit_menu.add_row(["B: Go Back"])
        manager_edit_menu.add_row(["Q: Quit"])
        manager_edit_menu.align = "l"
        
        return manager_edit_menu    