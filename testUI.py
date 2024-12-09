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
viewMenu.add_row(["6: View active tasks"])
viewMenu.add_row(["7: Make a report"])
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

realDestination1 = PrettyTable()
realDestination1.field_names["Viewing {}."]
realDestination1.add_row(["1. Properties"])
realDestination1.add_row(["2. Employees"])
realDestination1.align = "l"

destinationSpecificMenu = PrettyTable()


properties = PrettyTable()
properties.field_names["Properties", "propertyID", "Availability", "Has a pool", "Has a tub", "Has ovens"]
properties.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample"], divider=True)
properties.add_row(["sample name", "sample", "sample", "sample" ,"sample", "sample"], divider=True)
properties.align = 'l'

employees = PrettyTable()
employees.field_names["Name of employee", "Employee ID", "Social security number", "Phone number", "Gmail", "Working at destination"]
employees.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample"], divider=True)
employees.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample"], divider=True)
employees.add_row(["F. Enter 'F' to filter"])
employees.add_row(["B. Back"])
employees.add_row(["Q. Quit"])
employees.align = 'l'

contractors = PrettyTable()
contractors.field_names["Name of contractor", "Contractor ID", 
                        "Social security number", "Phone number", "Gmail", "Previous tasks", "Performance rating", "Opening hours"]
contractors.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample", "sample", "sample"], divider=True)
contractors.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample", "sample", "sample"], divider=True)
contractors.add_row(["B. Back"])
contractors.add_row(["Q. Quit"])
contractors.align = 'l'

managers = PrettyTable()
managers.field_names["Name of manager", "Manager ID", "Social security number", "Phone number", "Gmail", "Working at destination"]
managers.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample"], divider=True)
managers.add_row(["sample name", "sample," "sample", "sample" ,"sample", "sample"], divider=True)
managers.add_row(["B. Back"])
managers.add_row(["Q. Quit"])
managers.align = 'l'


