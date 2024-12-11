
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

        newEmployeePretty = PrettyTable()
        newEmployeePretty.title = "Adding a New Employee"
        newEmployeePretty.header = False
        newEmployeePretty.add_row("Employee ID")
        newEmployeePretty.add_row("Name")
        newEmployeePretty.add_row("Role")
        newEmployeePretty.align = 'l'
        newEmployeePretty.bottom_left_junction_char = '|'
        newEmployeePretty.bottom_right_junction_char = '|'
        newEmployeePretty.max_table_width = 100


        if error:
            print(f"Error: {error}\n")

    def display_temp_property(self, temp, error = None):


        #print("\n--- Adding a new Property ---")
        #print(f"Property Number: {temp.propertyID}")
        #print(f"Name: {temp.nameOfProperty}")
        #print(f"Location: {temp.location}")
        #print(f"Availability: {temp.availability}")
        #print(f"Does it have a pool: {temp.hasAPool}")
        #print(f"Does it have a hot Tub: {temp.hasATub}")
        #print(f"Does it have ovens: {temp.hasOvens}")            
        #print("--------------------------\n")

        newPropertyPretty = PrettyTable()
        newPropertyPretty.title = "Adding a New Property"
        newPropertyPretty.add_row(["Property Number", temp.get("propertyID")])
        newPropertyPretty.add_row(["Name", temp.get("nameOfProperty")])
        newPropertyPretty.add_row(["Location", temp.get("location")])
        newPropertyPretty.add_row(["Availability", temp.get("availability")])
        newPropertyPretty.add_row(["Has Pool", temp.get("hasAPool")])
        newPropertyPretty.add_row(["Has Hot Tub", temp.get("hasATub")])
        newPropertyPretty.add_row(["Has Ovens", temp.get("hasOvens")])
        newPropertyPretty.align = 'l'
        newPropertyPretty.max_table_width = 100
        newPropertyPretty.bottom_left_junction_char = '|'
        newPropertyPretty.bottom_right_junction_char = '|'


        if error:
            print(f"Error: {error}\n")

    def display_temp_maintenanceTask(self, temp, error = None):

        # print("\n--- Adding a new Maintenance Task ---")
        # print(f"Maintenance Number: {temp.maintenanceID}")
        # print(f"Maintenance done on Property Number: {temp.propertyID}")
        # print(f"Start Date: {temp.startDate}")
        # print(f"End Date: {temp.endDate}")
        # print(f"Status of Maintenance: {temp.statusMaintenance}")
        # print(f"Feedback: {temp.feedback}")
        # print(f"Priorty: {temp.priority}")
        # print("--------------------------\n")

        maintenancePretty = PrettyTable()
        maintenancePretty.title = "Adding a Maintenance Task"
        maintenancePretty.add_row(["Maintenance Number", temp.get("maintenanceID")])
        maintenancePretty.add_row(["Maintenance done or Property Number", temp.get("PropertyID")])
        maintenancePretty.add_row(["Start Date", temp.get("startDate")])
        maintenancePretty.add_row(["End Date", temp.get("EndDate")])
        maintenancePretty.add_row(["Status of Maintenance", temp.get("statusMaintenance")])
        maintenancePretty.add_row(["Feedback", temp.get("feedback")])
        maintenancePretty.add_row(["Priority", temp.get("priority")])
        maintenancePretty.align = 'l'
        maintenancePretty.bottom_left_junction_char = '|'
        maintenancePretty.bottom_right_junction_char = '|'
        maintenancePretty.max_table_width = 100

        if error:
            print(f"Error: {error}\n")

    def display_temp_maintenanceSchedule(self, temp, error = None):

        # print("\n--- Adding a new Maintenance Schedule ---")
        # print(f"Maintenance Schedule Number: {temp.maintenanceScheduleID}")
        # print(f"Scheduled on Maintenance Task Number: {temp.maintenanceID}")
        # print(f"Type of Maintenance Task: {temp.taskType}")
        # print(f"Frequency of Maintenance Task: {temp.frequency}")
        # print("--------------------------\n")

        scheduelePretty.title = "Adding a new Maintenance Schedule"
        scheduelePretty = PrettyTable()
        scheduelePretty.add_row(["Maintenance Schedule Number", temp.get("maintenanceScheduleID")])
        scheduelePretty.add_row(["Scheduled on Maintenance Task Number", temp.get("maintenanceID")])
        scheduelePretty.add_row(["Type of Maintenance Task", temp.get("taskType")])
        scheduelePretty.add_row(["Frequency of Maintenance Task", temp.get("frequency")])
        scheduelePretty.bottom_left_junction_char = '|'
        scheduelePretty.bottom_right_junction_char = '|'
        scheduelePretty.max_table_width = 100
        scheduelePretty.align = 'l'



        if error:
            print(f"Error: {error}\n")

    def display_temp_maintenanceReport(self, temp, error = None):

        self.clearTerminal()

        # print("\n--- Adding a new Maintenance Report ---")
        # print(f"maintenanceReportID: {temp.maintenanceReportID}")
        # print(f"maintenanceID: {temp.maintenanceID}")
        # print(f"employeeID: {temp.employeeID}")
        # print(f"contractorID: {temp.contractorID}")
        # print(f"contractorCost: {temp.contractorCost}")
        # print(f"readyToClose: {temp.readyToClose}")
        # print("--------------------------\n")

        maintenanceReportPretty = PrettyTable()
        maintenanceReportPretty.title = "Adding a new Maintenance Report"
        maintenanceReportPretty.field_names = ["Field"]
        maintenanceReportPretty.add_row(["Maintenance Report ID", temp.maintenanceReportID])
        maintenanceReportPretty.add_row(["Maintenance ID", temp.get("maintenanceID")])
        maintenanceReportPretty.add_row(["employee ID", temp.get("employeeID")])
        maintenanceReportPretty.add_row(["contractor ID", temp.get("contractorID")])
        maintenanceReportPretty.add_row(["contractor Cost", temp.get("ContractorCost")])
        maintenanceReportPretty.add_row(["ready To Close", temp.get("readyToClose")])
        maintenanceReportPretty.align = 'l'
        maintenanceReportPretty.max_table_width = 100
        maintenanceReportPretty.bottom_left_junction_char = '|'
        maintenanceReportPretty.bottom_right_junction_char = '|'

       

        if error:
            print(f"Error: {error}\n")


    def printProperty(self, property):

        # print("\n--- Property Information ---")
        # print(f"Property Number: {property.propertyID}")
        # print(f"Name: {property.nameOfProperty}")
        # print(f"Location: {property.location}")
        # print(f"Availability: {property.availability}")
        # print(f"Pool: {property.hasAPool}")
        # print(f"Hot Tub: {property.hasATub}")
        # print(f"Ovens: {property.hasOvens}")
        # print("--------------------------\n") 

        propertyPretty = PrettyTable()
        propertyPretty.title = "Property Information"
        propertyPretty.header = False
        propertyPretty.add_row(["Property number"])
        propertyPretty.add_row(["Property name"])
        propertyPretty.add_row(["Availability"])
        propertyPretty.add_row(["Pool"])
        propertyPretty.add_row(["Hot tub"])
        propertyPretty.add_row(["Ovens"])
        propertyPretty.align = 'l'
        propertyPretty.max_table_width = 100
        propertyPretty.bottom_left_junction_char = '|'
        propertyPretty.bottom_right_junction_char = '|'
        
        #print(propertypretty)


        # print("\n--- Employee Information ---")
        # print(f"Employee Number: {employee.employeeID}")
        # print(f"Name: {employee.name}")
        # print(f"Social Security: {employee.socialSecurity}")
        # print(f"Address: {employee.address}")
        # print(f"Home Phone: {employee.atHomePhone}")
        # print(f"GSM Phone: {employee.gsmPhone}")
        # print(f"Email: {employee.email}")
        # print(f"Work Location: {employee.workLocation}")
        # print(f"Type: {employee.type}")
        # print("--------------------------\n")

    def printEmployee(self, employee):

        
        employeePretty = PrettyTable()
        employeePretty.title = "Employee Information"
        employeePretty.header = False
        employeePretty.add_row(["Employee Number", employee.employeeID])
        employeePretty.add_row(["Name", employee.name])
        employeePretty.add_row(["Social Security", employee.socialSecurity])
        employeePretty.add_row(["Address", employee.address])
        employeePretty.add_row(["Home Phone", employee.atHomePhone])
        employeePretty.add_row(["GSM Phone", employee.gsmPhone])
        employeePretty.add_row(["Email", employee.email])
        employeePretty.add_row(["Work Location", employee.workLocation])
        employeePretty.add_row(["Type", employee.type])
        employeePretty.align = 'l'
        employeePretty.max_table_width = 100
        employeePretty.bottom_left_junction_char = '|'
        employeePretty.bottom_right_junction_char = '|'


    
        #print(table)



    #     print("\n--- Contractor Information ---")
    #     print(f"Contractor Number: {contractor.employeeID}")
    #     print(f"Name: {contractor.name}")
    #     print(f"Social Security: {contractor.socialSecurity}")
    #     print(f"Address: {contractor.address}")
    #     print(f"Home Phone: {contractor.atHomePhone}")
    #     print(f"GSM Phone: {contractor.gsmPhone}")
    #     print(f"Email: {contractor.email}")
    #     print(f"Work Location: {contractor.workLocation}")
    #     print(f"Type: {contractor.type}")
    #     print(f"Previous Task: {contractor.previousTask}")
    #     print(f"Performance Rating: {contractor.performanceRating}")
    #     print(f"Contractor Contact: {contractor.contractorContact}")
    #     print(f"Opening Hours: {contractor.openingHours}")
    #     print("--------------------------\n")

    def printContractor(self, contractor):

        contractorPretty = PrettyTable()
        contractorPretty.title = "Contractor Information"        
        contractorPretty.header = False
        contractorPretty.add_row(["Contractor Number", contractor.employeeID])
        contractorPretty.add_row(["Name", contractor.name])
        contractorPretty.add_row(["Social Security", contractor.socialSecurity])
        contractorPretty.add_row(["Address", contractor.address])
        contractorPretty.add_row(["Home Phone", contractor.atHomePhone])
        contractorPretty.add_row(["GSM Phone", contractor.gsmPhone])
        contractorPretty.add_row(["Email", contractor.email])
        contractorPretty.add_row(["Work Location", contractor.workLocation])
        contractorPretty.add_row(["Type", contractor.type])
        contractorPretty.add_row(["Previous Task", contractor.previousTask])
        contractorPretty.add_row(["Performance Rating", contractor.performanceRating])
        contractorPretty.add_row(["Contractor Contact", contractor.contractorContact])
        contractorPretty.add_row(["Opening Hours", contractor.openingHours])
        contractorPretty.align = 'l'
        contractorPretty.max_table_width = 100
        contractorPretty.bottom_left_junction_char = '|'
        contractorPretty.bottom_right_junction_char = '|'

    #print(table)


    def printMaintenanceTask(self, task):
        
        # print("\n--- Maintenance Task Information ---")
        # print(f"Maintenance Number: {task.maintenanceID}")
        # print(f"Maintenance done on Property Number: {task.propertyID}")
        # print(f"Start Date: {task.startDate}")
        # print(f"End Date: {task.endDate}")
        # print(f"Status of Maintenance: {task.statusMaintenance}")
        # print(f"Feedback: {task.feedback}")
        # print(f"Priorty: {task.priority}")
        # print("--------------------------\n")


        maintennanceTaskPretty = PrettyTable()
        maintennanceTaskPretty.title = "Maintenance Task Information"
        maintennanceTaskPretty.header = False
        maintennanceTaskPretty.add_row(["Maintenance Number", task.maintenanceID])
        maintennanceTaskPretty.add_row(["Property Number", task.propertyID])
        maintennanceTaskPretty.add_row(["Start Date", task.startDate])
        maintennanceTaskPretty.add_row(["End Date", task.endDate])
        maintennanceTaskPretty.add_row(["Status of Maintenance", task.statusMaintenance])
        maintennanceTaskPretty.add_row(["Feedback", task.feedback])
        maintennanceTaskPretty.add_row(["Priority", task.priority])
        maintennanceTaskPretty.align = 'l'
        maintennanceTaskPretty.max_table_width = 100
        maintennanceTaskPretty.bottom_left_junction_char = '|'
        maintennanceTaskPretty.bottom_right_junction_char = '|'

        #print(table)

        

    def printMaintenanceSchedule(self, schedule):
        
        # print("\n--- Maintenance Schedule Information ---")
        # print(f"Maintenance Schedule Number: {schedule.maintenanceScheduleID}")
        # print(f"Scheduled on Maintenance Task Number: {schedule.maintenanceID}")
        # print(f"Type of Maintenance Task: {schedule.taskType}")
        # print(f"Frequency of Maintenance Task: {schedule.frequency}")
        # print("--------------------------\n")


        maintenanceScheduelePretty = PrettyTable()
        maintenanceScheduelePretty.title = "Information"
        maintenanceScheduelePretty.header = False
        maintenanceScheduelePretty.add_row(["Maintenance Schedule Number", schedule.maintenanceScheduleID])
        maintenanceScheduelePretty.add_row(["Scheduled on Maintenance Task Number", schedule.maintenanceID])
        maintenanceScheduelePretty.add_row(["Type of Maintenance Task", schedule.taskType])
        maintenanceScheduelePretty.add_row(["Frequency of Maintenance Task", schedule.frequency])
        maintenanceScheduelePretty.align = 'l'
        maintenanceScheduelePretty.max_table_width = 100
        maintenanceScheduelePretty.bottom_left_junction_char = '|'
        maintenanceScheduelePretty.bottom_right_junction_char = '|'


        #print(table)



    def printMaintenanceReport(self, report):

        # print("\n--- Maintenance Report Information ---")
        # print(f"Maintenance Report Number: {report.maintenanceReportID}")
        # print(f"Report on Maintenance Task Number: {report.maintenanceID}")
        # print(f"Employee Number of the Employee that took on the Task: {report.employeeID}")
        # print(f"Contractor Number of the Contractor that took the Task: {report.contractorID}")
        # print(f"Cost of the Contrator doing the Task: {report.contractorCost}")
        # print(f"Is the Maintenance Task ready to be closed: {report.readyToClose}")
        # print("--------------------------\n")

        maintenanceReportPretty = PrettyTable()
        maintenanceReportPretty.title = "Maintenance Report Information"
        maintenanceReportPretty.header = False
        maintenanceReportPretty.add_row(["Maintenance Report Number", report.maintenanceReportID])
        maintenanceReportPretty.add_row(["Report on Maintenance Task Number", report.maintenanceID])
        maintenanceReportPretty.add_row(["Employee Number of Task Taker", report.employeeID])
        maintenanceReportPretty.add_row(["Contractor Number of Task Taker", report.contractorID])
        maintenanceReportPretty.add_row(["Contractor Cost", report.contractorCost])
        maintenanceReportPretty.add_row(["Ready to Close", report.readyToClose])
        maintenanceReportPretty.align = 'l'
        maintenanceReportPretty.max_table_width = 100
        maintenanceReportPretty.bottom_left_junction_char = '|'
        maintenanceReportPretty.bottom_right_junction_char = '|'


        #print(table)


    def clearTerminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")