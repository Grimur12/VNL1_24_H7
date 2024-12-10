
from os import system, name
from prettytable import PrettyTable

# Need to make all these displays look better 
# Our display file where we have everything we want to display to the user.

class Displays:
    def __init__(self):
        pass
        # DO WE NEED TO ADD SOMETHING HERE????????

    def editContractorMenu(self, contractor, error = None):
        """ Turns the class into a string to print out with, mainly for UI display """
        # The display the manager sees when updating a contractor's information
        self.clearTerminal()
        print(f"""
--- Updating employee {contractor.employeeID} ---
You can not change Employee's ID, Social Security or Type
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
        # Here is the display the manager sees when updating an employee's information
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
        '''Turns the class into a string to print out with, mainly for UI display '''
        # Display of manager to edit property's information
        self.clearTerminal()
        print(f"""
--- Updating employee {property.propertyID} ---
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

    def display_temp_employee(self, temp, error = None):

        self.clearTerminal()

        #print("\n--- Adding a new Employee ---")
        #print(temp)            
        #print("--------------------------\n")

        table = PrettyTable()
        table.title = "Adding a New Employee"
        table.field_names = "Field"
        table.add_row("Employee ID")
        table.add_row("Name")
        table.add_row("Role")

        if error:
            print(f"Error: {error}\n")

    def display_temp_property(self, temp, error = None):
        
        self.clearTerminal()

        #print("\n--- Adding a new Property ---")
        #print(f"Property Number: {temp.propertyID}")
        #print(f"Name: {temp.nameOfProperty}")
        #print(f"Location: {temp.location}")
        #print(f"Availability: {temp.availability}")
        #print(f"Does it have a pool: {temp.hasAPool}")
        #print(f"Does it have a hot Tub: {temp.hasATub}")
        #print(f"Does it have ovens: {temp.hasOvens}")            
        #print("--------------------------\n")

        table = PrettyTable()
        table.title = "Adding a New Property"
        table.field_names = ["Field", "Value"]
        table.add_row(["Property Number", temp.get("propertyID", "N/A")])
        table.add_row(["Name", temp.get("nameOfProperty", "N/A")])
        table.add_row(["Location", temp.get("location", "N/A")])
        table.add_row(["Availability", temp.get("availability", "N/A")])
        table.add_row(["Has Pool", temp.get("hasAPool", "N/A")])
        table.add_row(["Has Hot Tub", temp.get("hasATub", "N/A")])
        table.add_row(["Has Ovens", temp.get("hasOvens", "N/A")])

        if error:
            print(f"Error: {error}\n")

    def display_temp_maintenanceTask(self, temp, error = None):
        
        self.clearTerminal()

        print("\n--- Adding a new Maintenance Task ---")
        print(f"Maintenance Number: {temp.maintenanceID}")
        print(f"Maintenance done on Property Number: {temp.propertyID}")
        print(f"Start Date: {temp.startDate}")
        print(f"End Date: {temp.endDate}")
        print(f"Status of Maintenance: {temp.statusMaintenance}")
        print(f"Feedback: {temp.feedback}")
        print(f"Priorty: {temp.priority}")
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
        print("--------------------------\n")

        if error:
            print(f"Error: {error}\n")

    def display_temp_maintenanceReport(self, temp, error = None):

        self.clearTerminal()

        print("\n--- Adding a new Maintenance Report ---")
        print(f"maintenanceReportID: {temp.maintenanceReportID}")
        print(f"maintenanceID: {temp.maintenanceID}")
        print(f"employeeID: {temp.employeeID}")
        print(f"contractorID: {temp.contractorID}")
        print(f"contractorCost: {temp.contractorCost}")
        print(f"readyToClose: {temp.readyToClose}")
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
        print(f"Start Date: {task.startDate}")
        print(f"End Date: {task.endDate}")
        print(f"Status of Maintenance: {task.statusMaintenance}")
        print(f"Feedback: {task.feedback}")
        print(f"Priorty: {task.priority}")
        print("--------------------------\n")

    def printMaintenanceSchedule(self, schedule):
        
        print("\n--- Maintenance Schedule Information ---")
        print(f"Maintenance Schedule Number: {schedule.maintenanceScheduleID}")
        print(f"Scheduled on Maintenance Task Number: {schedule.maintenanceID}")
        print(f"Type of Maintenance Task: {schedule.taskType}")
        print(f"Frequency of Maintenance Task: {schedule.frequency}")
        print("--------------------------\n")

    def printMaintenanceReport(self, report):

        print("\n--- Maintenance Report Information ---")
        print(f"Maintenance Report Number: {report.maintenanceReportID}")
        print(f"Report on Maintenance Task Number: {report.maintenanceID}")
        print(f"Employee Number of the Employee that took on the Task: {report.employeeID}")
        print(f"Contractor Number of the Contractor that took the Task: {report.contractorID}")
        print(f"Cost of the Contrator doing the Task: {report.contractorCost}")
        print(f"Is the Maintenance Task ready to be closed: {report.readyToClose}")
        print("--------------------------\n")

    def clearTerminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")