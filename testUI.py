from prettytable import PrettyTable
viewMenu = PrettyTable()
viewMenu.border = True
viewMenu.header = False
viewMenu.left_padding_width = 1
viewMenu.right_padding_width = 1
viewMenu.align = "l"
viewMenu.title = "Main menu"


viewMenu.add_row(["1: View destinations"])
viewMenu.add_row(["2: View properties"])
viewMenu.add_row(["3: View employees"])
viewMenu.add_row(["4: View contractors"])
viewMenu.add_row(["5: View managers"])
viewMenu.add_row(["6: Make a report"])
viewMenu.add_row(["7: View all tasks"])
viewMenu.add_row(["r. Change size, sample: 30"])
viewMenu.add_row(["B: Back"])
viewMenu.add_row(["Q: Quit"])
print(viewMenu) 

destinationMenu = PrettyTable()
destinationMenu.field_names = ["Destination Menu"]
destinationMenu.add_row(["1. Reykjavik, Iceland"])
destinationMenu.add_row(["2. Nuuk, Greenland"])
destinationMenu.add_row(["3. Kulusuk, Greenland"])
destinationMenu.add_row(["4. Tórshavn, Faroe Islands"])
destinationMenu.add_row(["5. Tingwall, Scotland"])
destinationMenu.add_row(["6. Longyearbyen, Norway"])
destinationMenu.align = 'l'
destinationMenu.add_row(["B: Back"])
destinationMenu.add_row(["Q: Quit"])

print(destinationMenu)

realDestination = PrettyTable()
realDestination.field_names["Viewing"]
realDestination.add_row(["1. Properties"])
realDestination.add_row(["2. Employees"])
realDestination.add_row(["3. Contractors"])
realDestination.align = "l"

print(realDestination)

properties = PrettyTable()
properties.field_names["Properties", "propertyID", "Availability", "Has a pool", "Has a tub", "Has ovens"]
properties.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample"], divider=True)
properties.add_row(["sample name", "sample", "sample", "sample" ,"sample", "sample"], divider=True)
properties.add_row(["Enter property ID to view work reports: "])
properties.align = 'l'

print(properties)

employees = PrettyTable()
employees.field_names["Name of employee", "Employee ID", "Social security number", "Phone number", "Gmail", "Working at destination"]
employees.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample"], divider=True)
employees.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample"], divider=True)
employees.add_row(["F. Enter 'F' to filter"])
employees.add_row(["B. Enter 'B' to go back"])
employees.add_row(["Q. Enter'Q' to Quit"])
employees.align = 'l'

print(employees)

contractors = PrettyTable()
contractors.field_names["Name of contractor", "Contractor ID", 
                        "Social security number", "Phone number", "Gmail", "Previous tasks", "Performance rating", "Opening hours"]
contractors.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample", "sample", "sample"], divider=True)
contractors.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample", "sample", "sample"], divider=True)
contractors.add_row(["B. Back"])
contractors.add_row(["Q. Quit"])
contractors.align = 'l'

print(contractors)

managers = PrettyTable()
managers.field_names["Name of manager", "Manager ID", "Social security number", "Phone number", "Gmail", "Working at destination"]
managers.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample"], divider=True)
managers.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample"], divider=True)
managers.add_row(["B. Back"])
managers.add_row(["Q. Quit"])
managers.align = 'l'

print(managers)

viewTasks = PrettyTable()
viewTasks.field_names["Enter employee number to view maintenace task list."]
viewTasks.add_row["Search by employee number: "]
viewTasks.add_row["B. Back"]
viewTasks.add_row["Q. Quit"]
viewTasks.align = 'l'

print(viewTasks)

# viewTasksOfEmployee = PrettyTable()
# viewTasksOfEmployee.field_names["Viewing all tasks"]
# viewTasksOfEmployee.add_row["1. View completed tasks"]
# viewTasksOfEmployee.add_row["2. View active tasks"]
# viewTasksOfEmployee.add_row["B. Back"]
# viewTasksOfEmployee.add_row["Q. Quit"]

makeReport = PrettyTable()
makeReport.field_names["Make a report"]
makeReport.add_row["Enter Employee name: "]
makeReport.add_row["Enter employee ID"]
makeReport.add_row["Enter date, sample: 26/10/24"]
makeReport.add_row["Refer a contractor: "]
makeReport.add_row["Write your report: "]
makeReport.add_row["Is the task complete? Y/N"]
makeReport.add_row["To save report, Enter 'S'."]
makeReport.add_row["B. Back"]
makeReport.add_row["Q. Quit"]
makeReport.align = 'l'

print(makeReport)
