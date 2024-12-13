
from os import system, name
from prettytable import PrettyTable
from Logic_Layer.LogicLayerAPI import LogicLayerAPI

class Displays:
    def __init__(self) -> None:
        """ No attributes needed for this class it only holds our displays to print in the other UI's"""
        self.LogicLayerWrapper = LogicLayerAPI()

    def clearTerminal(self) -> None:
        """ Function is responsible for clearing the terminal the user is operating the system on """
        if name == "nt":
            system("cls")
        else:
            system("clear")  

    # ALL FUNCTIONS TO PRINT THE MODEL CLASSES, Editing and Creating, title message is default for information but editing or creating can specify another title if they wish

    def printProperty(self, property, title_message = "Property Information", error = None, edit_message = "", done_message = "", mode = "") -> None:
        """ Function takes has a set title message for displaying the property but can be changed if needed to edit/create, 
        has an error message feature along with edit message done message and mode, all of these for the other displays to input to specify what they are using this print function for"""
        print(f"\n--- {title_message} ---") 
        print(f"{edit_message}")
        print(f"Property Number: {property.propertyID}") # For all of these we get a property object from the logic layer and we display it
        print(f"1.Name: {property.nameOfProperty}" + ("              // Ex. Igloo" if mode == "hints" else "")) # These hints are for the creation process, for the other UI's to specify
        print(f"2.Description: {property.description}" + ("       // Ex. 4 Rooms, 100 m^2, Has an Ocean View" if mode == "hints" else "")) # These hints are for the creation process, for the other UI's to specify
        print(f"3.Location: {property.location}" + ("          // Ex. 1 (Valid Destination Number)" if mode == "hints" else ""))
        print(f"4.Availability: {property.availability}" + ("      // Ex. True" if mode == "hints" else ""))
        print(f"5.Pool: {property.hasAPool}" + ("              // Ex. False" if mode == "hints" else ""))
        print(f"6.Hot Tub: {property.hasATub}" + ("           // Ex. False" if mode == "hints" else ""))
        print(f"7.Ovens: {property.hasOvens}" + ("             // Ex. True" if mode == "hints" else ""))
        print("--------------------------")
        print("B: To Go Back")
        print("Q: To Quit")
        print(f"{done_message}") 

        if error:
            print(f"Error: {error}\n")

    def printEmployee(self, employee, title_message = "Employee Information", error = None, edit_message = "", done_message = "", mode = "") -> None:
        """ Function takes has a set title message for displaying the employee but can be changed if needed to edit/create, 
        has an error message feature along with edit message done message and mode, all of these for the other displays to input to specify what they are using this print function for"""
        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        if employee.type == "Contractor": # This is so we can use the same function for both contractor and employees since they share many attributes, use what the logic layer provided us with to print the relevant data

            print(f"Employee Number: {employee.employeeID}") # For all of these we get an object from the logic layer and we display it
            print(f"1.Name: {employee.name}" + ("                // Ex. Karl Jónsson" if mode == "hints" else "")) # These hints are for the creation process, for the other UI's to specify
            print(f"2.Social Security: {employee.socialSecurity}" + ("     // Ex. 020398-2490" if mode == "hints" else ""))
            print(f"3.Address: {employee.address}" + ("             // Ex. Brekkuvegur 91" if mode == "hints" else ""))
            print(f"4.Home Phone: {employee.atHomePhone}" + ("          // Ex. +242 32 66 21234" if mode == "hints" else ""))
            print(f"5.GSM Phone: {employee.gsmPhone}" + ("           // Ex. 882-1234" if mode == "hints" else ""))
            print(f"6.Email: {employee.email}" + ("               // Ex. Karl@gmail.com" if mode == "hints" else ""))
            print(f"7.Work Location: {employee.workLocation}" + ("       // Ex. 1 (Valid Destination Number)" if mode == "hints" else ""))
            print(f"Type: {employee.type}")
            print(f"8.Previous Task: {employee.previousTask}" + ("       // Ex. 1 or 1,2,3 (Valid Maintenance Task(s), Can Be Empty)" if mode == "hints" else ""))
            print(f"9.Performance Rating: {employee.performanceRating}" + ("  // Ex. 9 (Can Be Empty If No Previous Tasks or a Performance Rating from the internet)" if mode == "hints" else ""))
            print(f"10.Contractor Contact: {employee.contractorContact}" + (" // Ex. 1 (Valid Employee Number)" if mode == "hints" else ""))
            print(f"11.Opening Hours: {employee.openingHours}" + ("      // Ex. 9-5" if mode == "hints" else ""))

        else: # This would be for the other employees

            print(f"Employee Number: {employee.employeeID}")
            print(f"1.Name: {employee.name}" + ("                // Ex. Karl Jónsson" if mode == "hints" else "")) # These hints are for the creation process, for the other UI's to specify
            print(f"2.Social Security: {employee.socialSecurity}" + ("     // Ex. 020398-2490" if mode == "hints" else ""))
            print(f"3.Address: {employee.address}" + ("             // Ex. Brekkuvegur 91" if mode == "hints" else ""))
            print(f"4.Home Phone: {employee.atHomePhone}" + ("          // Ex. +242 32 66 21234" if mode == "hints" else ""))
            print(f"5.GSM Phone: {employee.gsmPhone}" + ("           // Ex. 882-1234" if mode == "hints" else ""))
            print(f"6.Email: {employee.email}" + ("               // Ex. Karl@gmail.com" if mode == "hints" else ""))
            print(f"7.Work Location: {employee.workLocation}" + ("       // Ex. 1 (Valid Destination Number)" if mode == "hints" else ""))
            print(f"Type: {employee.type}")         
        print("--------------------------")
        print("B: To Go Back")
        print("Q: To Quit")
        print(f"{done_message}") 

        if error:
            print(f"Error: {error}\n")

    def printMaintenanceTask(self, task, title_message = "Maintenance Task Information", error = None, edit_message = "", done_message = "", mode = "") -> None:
        """ Function takes has a set title message for displaying the maintenance Task but can be changed if needed to edit/create, 
        has an error message feature along with edit message done message and mode, all of these for the other displays to input to specify what they are using this print function for"""
        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        print(f"Maintenance Number: {task.maintenanceID}") # For all of these we get a maintenance object from the logic layer and we display it
        print(f"1.Maintenance done on Property Number: {task.propertyID}" + ("   // Ex. 1 (Valid Property Number)" if mode == "hints" else "")) # These hints are for the creation process, for the other UI's to specify
        print(f"2.Description of Task: {task.description}" + ("                   // Ex. Cleaning The Sink" if mode == "hints" else ""))
        print(f"3.Start Date: {task.startDate}" + ("                            // Ex. 10.03.2023.12:30" if mode == "hints" else ""))
        print(f"4.End Date: {task.endDate}" + ("                              // Ex. 10.03.2023.16:30" if mode == "hints" else ""))
        print(f"5.Status of Maintenance: {task.statusMaintenance}" + ("                 // Ex. Ongoing" if mode == "hints" else ""))
        print(f"6.Priorty: {task.priority}" + ("                               // Ex. ASAP" if mode == "hints" else ""))
        print(f"7.Recurring: {task.recurring}" + ("                             // Ex. True" if mode == "hints" else ""))
        print("--------------------------")
        print("B: To Go Back")
        print("Q: To Quit")
        print(f"{done_message}") 

        if error:
            print(f"Error: {error}\n")

    def printMaintenanceSchedule(self, schedule, title_message = "Maintenance Schedule Information", error = None, edit_message = "", done_message = "", mode = "") -> None:
        """ Function takes has a set title message for displaying the maintenance schedule but can be changed if needed to edit/create, 
        has an error message feature along with edit message done message and mode, all of these for the other displays to input to specify what they are using this print function for"""
        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        print(f"Maintenance Schedule Number: {schedule.maintenanceScheduleID}") # For all of these we get a maintenance Schedule object from the logic layer and we display it
        print(f"1.Scheduled Maintenance Task Number: {schedule.maintenanceID}" + ("       // Ex. 1 (Valid Maintenance Task Number)" if mode == "hints" else "")) # These hints are for the creation process, for the other UI's to specify
        print(f"2.Type of Maintenance Task: {schedule.taskType}" + ("                   // Ex. Normal" if mode == "hints" else ""))
        print(f"3.Frequency of Maintenance Task: {schedule.frequency}" + ("              // Ex. Weekly" if mode == "hints" else ""))
        print(f"4.Start Date of Scheduled Maintenance: {schedule.startDate}" + ("        // Ex. 10.03.2023.12:30" if mode == "hints" else ""))
        print("--------------------------")
        print("B: To Go Back")
        print("Q: To Quit")
        print(f"{done_message}") 

        if error:
            print(f"Error: {error}\n")

    def printMaintenanceReport(self, report, title_message = "Maintenance Report Information", error = None, edit_message = "", done_message = "", mode = "") -> None:
        """ Function takes has a set title message for displaying the maintenance report but can be changed if needed to edit/create, 
        has an error message feature along with edit message done message and mode, all of these for the other displays to input to specify what they are using this print function for"""
        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        print(f"Maintenance Report Number: {report.maintenanceReportID}") # For all of these we get an Maintenance report object from the logic layer and we display it
        print(f"1.Report on Maintenance Task Number: {report.maintenanceID}" + ("                         // Ex. 1 (Valid Maintenance Task Number)" if mode == "hints" else "")) # These hints are for the creation process, for the other UI's to specify
        print(f"2.Employee Number of the Employee that took on the Task: {report.employeeID}" + ("     // Ex. 2 (Valid Employee Number)" if mode == "hints" else ""))
        print(f"3.Cost of materials: {report.materialCost}" + ("                                         // Ex. 1000 (Number With No Currency)" if mode == "hints" else ""))
        print(f"4.Contractor Number of the Contractor that took the Task: {report.contractorID}" + ("    // Ex. 1 (Valid Contractor Number)" if mode == "hints" else ""))
        print(f"5.Cost of the Contrator doing the Task: {report.contractorCost}" + ("                      // Ex. 1000 (Number With No Currency)" if mode == "hints" else ""))
        print(f"6.Is the Maintenance Task ready to be closed: {report.readyToClose}")
        print(f"7.Supervisor Has accepted the work done: {report.supervisorClosed}")
        print(f"8.Feedback on the completed work: {report.supervisorFeedback}")
        print("--------------------------")
        print("B: To Go Back")
        print("Q: To Quit")
        print(f"{done_message}") 

        if error:
            print(f"Error: {error}\n")

    def printDestination(self, destination, title_message = "Destination Information", error = None, edit_message = "", done_message = "", mode = "") -> None:
        """ Function takes has a set title message for displaying the destination but can be changed if needed to edit/create, 
        has an error message feature along with edit message done message and mode, all of these for the other displays to input to specify what they are using this print function for"""
        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        print(f"Destination Number: {destination.destinationID}") # For all of these we get a destination object from the logic layer and we display it
        print(f"1.Name: {destination.name}")
        print(f"2.Country: {destination.country}")
        print(f"3.Timezone: {destination.timezone}")
        print(f"4.Airport Name: {destination.airportName}")
        print(f"5.Phone Number: {destination.phoneNumber}")
        print(f"6.Opening Hours: {destination.openingHours}")
        print(f"7.Manager Of Destination: {destination.managerOfDestination}")
        print("--------------------------")
        print("B: To Go Back")
        print("Q: To Quit")
        print(f"{done_message}") 

        if error:
            print(f"Error: {error}\n")

    ## A WARNING MESSAGE FOR USER CREATING A MANAGER

    def overWriteManager(self, error = None) -> None:
        """ Function prints out the options the user when he is creating a manager"""
        print("\n----------------------------------------------------------------------------------------------------------------------")
        print("Destination already has a Manager, Would you like to demote him to a General Employee or abort creating a new Manager")
        print("----------------------------------------------------------------------------------------------------------------------\n")
        print("1: To continue creating the new Manager, demoting the current one")
        print("2: To stop the creation process of a new Manager")
        print("Q: To Quit the Program")

        if error:
            print(error)


    # ALL MENUS USED BY THE UI

    def ContractorMenu(self) -> PrettyTable:
        contractor_menu = PrettyTable()
        contractor_menu.title = "Contractor Menu"
        contractor_menu.header = False
        contractor_menu.add_row(["1: Create a Maintenance Report"]) # Add the relevant rows to the menu
        contractor_menu.add_row(["2: Viewing features"])
        contractor_menu.add_row(["B: Go Back"])
        contractor_menu.add_row(["Q: Quit"])

        contractor_menu.align = "l"
        return contractor_menu
    
    def EmployeeMenu(self) -> PrettyTable:
        """ Function creates the XX Menu for the other UI's to call and use to print out for the user to see """
        employee_menu = PrettyTable()
        employee_menu.title = " Employee Menu"
        employee_menu.header = False
        employee_menu.add_row(["1: Create a Maintenance Report"]) # Add the relevant rows to the menu
        employee_menu.add_row(["2: Viewing features"])
        employee_menu.add_row(["B: Go Back"])
        employee_menu.add_row(["Q: Quit"])
        employee_menu.align = "l"
        return employee_menu

    def MainMenu(self) -> PrettyTable:
        """ Function creates the XX Menu for the other UI's to call and use to print out for the user to see """
        main_menu = PrettyTable()
        main_menu.title = "---Welcome to NAN Air!---"
        main_menu.header = False
        main_menu.add_row(["Are you a manager, employee or a contractor?"]) # Add the relevant rows to the menu
        main_menu.add_row([""])
        main_menu.add_row(["1: Manager"])
        main_menu.add_row(["2: Employee"])
        main_menu.add_row(["3: Contractor"])
        main_menu.add_row(["Q: Quit"])
        main_menu.add_row([""])
        main_menu.align = 'l'
        main_menu.max_table_width = 100
        
        return main_menu
    
    def ViewMenu(self) -> PrettyTable:
        """ Function creates the XX Menu for the other UI's to call and use to print out for the user to see """
        view_menu = PrettyTable()
        view_menu.title = " Viewing menu"
        view_menu.header = False
        view_menu.add_row(["1: View all Employees"]) # Add the relevant rows to the menu
        view_menu.add_row(["2: View all Contractors"])
        view_menu.add_row(["3: View all Properties"])
        view_menu.add_row(["4: View all Maintenance Tasks"])
        view_menu.add_row(["5: View all Scheduled Maintenance Tasks"])
        view_menu.add_row(["6: View all Maintenance Reports"])
        view_menu.add_row(["7: View all Destinations"])
        view_menu.add_row(["B: Go back"])
        view_menu.add_row(["Q: Quit"])
        view_menu.align = 'l'  

        return view_menu
    
    def ManagerMainMenu(self) -> PrettyTable:
        """ Function creates the Manager Menu for the other UI's to call and use to print out for the user to see """
        manager_menu = PrettyTable()
        manager_menu.title = "Manager menu"
        manager_menu.header = False
        manager_menu.add_row(["1: Create new Properties, Employees or Maintenance Tasks"]) # Add the relevant rows to the menu
        manager_menu.add_row(["2: Edit Properties, Employees or Maintenance Tasks"])
        manager_menu.add_row(["3: View Properties, Employess or Maintenance Tasks"])
        manager_menu.add_row(["B: Go Back"])
        manager_menu.add_row(["Q: Quit"])
        manager_menu.align = "l"

        return manager_menu
    
    def ManagerAddMenu(self) -> PrettyTable:
        """ Function creates the Add Menu which is a derivative from the manager menu for the other UI's to call and use to print out for the user to see """
        manager_add_menu = PrettyTable()
        manager_add_menu.title = "Create Menu - Manager position"
        manager_add_menu.header = False
        manager_add_menu.add_row(["1: Create a new General Employee "]) # Add the relevant rows to the menu
        manager_add_menu.add_row(["2: Create a new Manager"])
        manager_add_menu.add_row(["3: Create a new Contractor"])
        manager_add_menu.add_row(["4: Create a new Property"])
        manager_add_menu.add_row(["5: Create a new Maintenance Task"])
        manager_add_menu.add_row(["6: Create a new Maintenance Schedule"])
        manager_add_menu.add_row(["B: Go Back"])
        manager_add_menu.add_row(["Q: Quit"])
        manager_add_menu.align = "l"

        return manager_add_menu

    def ManagerEditMenu(self) -> PrettyTable:
        """ Function creates the Edit Menu which is a derivative from the manager menu for the other UI's to call and use to print out for the user to see """
        manager_edit_menu = PrettyTable()
        manager_edit_menu.title = "Edit Menu - Manager Position"
        manager_edit_menu.header = False
        manager_edit_menu.add_row(["1: Edit an Employee or a Manager"]) # Add the relevant rows to the menu
        manager_edit_menu.add_row(["2: Edit a Contractor"])
        manager_edit_menu.add_row(["3: Edit a Property"])
        manager_edit_menu.add_row(["4: Edit a Maintenance Task"])
        manager_edit_menu.add_row(["5: Edit a Maintenance Schedule"])
        manager_edit_menu.add_row(["6: To close a Maintenance Report"])
        manager_edit_menu.add_row(["B: Go Back"])
        manager_edit_menu.add_row(["Q: Quit"])
        manager_edit_menu.align = "l"
        
        return manager_edit_menu
    
    def filterEmployeesMenu(self) -> PrettyTable:
        """ Function creates the Filter Employees Menu, used by the viewingUI (viewMenu) for the other UI's to call and use to print out for the user to see """
        filter_employees_menu = PrettyTable()
        filter_employees_menu.title = "Specific Employee Information"
        filter_employees_menu.header = False
        filter_employees_menu.add_row(["1: To view additional information of a specific Employee"]) # Add the relevant rows to the menu
        filter_employees_menu.add_row(["2: To view all tasks an Employee has worked on"])
        filter_employees_menu.add_row(["3: To view the Manager(s)"])
        filter_employees_menu.add_row(["B: To Go Back"])
        filter_employees_menu.add_row(["Q: To Quit"])
        filter_employees_menu.align = "l"

        return filter_employees_menu
    
    def filterContractorsMenu(self) -> PrettyTable:
        """ Function creates the filter contractors Menu, used by the viewingUI (viewMenu) for the other UI's to call and use to print out for the user to see """
        filter_contractors_menu = PrettyTable()
        filter_contractors_menu.title = "Specific Contractor Information"
        filter_contractors_menu.header = False
        filter_contractors_menu.add_row(["1: To view additional information of a specific Contractor"]) # Add the relevant rows to the menu
        filter_contractors_menu.add_row(["2: To view all tasks a Contractor has worked on"])
        filter_contractors_menu.add_row(["B: To Go Back"])
        filter_contractors_menu.add_row(["Q: To Quit"])
        filter_contractors_menu.align = "l"

        return filter_contractors_menu

    def filterPropertiesMenu(self) -> PrettyTable:
        """ Function creates the filter properties Menu, used by the viewingUI (viewMenu) for the other UI's to call and use to print out for the user to see """
        filter_properties_menu = PrettyTable()
        filter_properties_menu.title = "Specific Property Information"
        filter_properties_menu.header = False
        filter_properties_menu.add_row(["1: To view additional information of a specific Property"]) # Add the relevant rows to the menu
        filter_properties_menu.add_row(["2: To view all Maintenance on a specific Property"])
        filter_properties_menu.add_row(["B: To Go Back"])
        filter_properties_menu.add_row(["Q: To Quit"])
        filter_properties_menu.align = "l"

        return filter_properties_menu 

    def filterMaintenanceMenu(self) -> PrettyTable:
        """ Function creates the filter maintenance Menu, used by the viewingUI (viewMenu) for the other UI's to call and use to print out for the user to see """
        filter_maintenance_menu = PrettyTable()
        filter_maintenance_menu.title = "Specific Maintenance Task Information"
        filter_maintenance_menu.header = False
        filter_maintenance_menu.add_row(["1: To view additional information of a specific Maintenance Task"]) # Add the relevant rows to the menu
        filter_maintenance_menu.add_row(["2: To view all Maintenance Tasks that are ready to be closed (Through closing the Maintenance Report)"])
        filter_maintenance_menu.add_row(["B: To Go Back"])
        filter_maintenance_menu.add_row(["Q: To Quit"])
        filter_maintenance_menu.align = "l"

        return filter_maintenance_menu 
    
    def filterMaintenanceScheduleMenu(self) -> PrettyTable:
        """ Function creates the filter maintenance schedule Menu, used by the viewingUI (viewMenu) for the other UI's to call and use to print out for the user to see """
        filter_maintenanceSchdule_menu = PrettyTable()
        filter_maintenanceSchdule_menu.title = "Specific Maintenance Schedule Information"
        filter_maintenanceSchdule_menu.header = False
        filter_maintenanceSchdule_menu.add_row(["1: To view additional information of a specific Maintenance Schedule"]) # Add the relevant rows to the menu
        filter_maintenanceSchdule_menu.add_row(["B: To Go Back"])
        filter_maintenanceSchdule_menu.add_row(["Q: To Quit"])
        filter_maintenanceSchdule_menu.align = "l"

        return filter_maintenanceSchdule_menu 
    
    def filterMaintenanceReportMenu(self) -> PrettyTable:
        """ Function creates the filter maintenance report Menu, used by the viewingUI (viewMenu) for the other UI's to call and use to print out for the user to see """
        filter_maintenanceReport_menu = PrettyTable()
        filter_maintenanceReport_menu.title = "Specific Maintenance Report Information"
        filter_maintenanceReport_menu.header = False
        filter_maintenanceReport_menu.add_row(["1: To view additional information of a specific Maintenance Report"]) # Add the relevant rows to the menu
        filter_maintenanceReport_menu.add_row(["B: To Go Back"])
        filter_maintenanceReport_menu.add_row(["Q: To Quit"])
        filter_maintenanceReport_menu.align = "l"

        return filter_maintenanceReport_menu 
    
    def filterDestinationMenu(self) -> PrettyTable:
        """ Function creates the filter destination Menu, used by the viewingUI (viewMenu) for the other UI's to call and use to print out for the user to see """
        filter_destination_menu = PrettyTable()
        filter_destination_menu.title = "Specific Destination Information"
        filter_destination_menu.header = False
        filter_destination_menu.add_row(["1: To view information about Employees at a specific Destination"]) # Add the relevant rows to the menu
        filter_destination_menu.add_row(["2: To view information about Contractors at a specific Destination"])
        filter_destination_menu.add_row(["3: To view information about Properties at a specific Destination"])
        filter_destination_menu.add_row(["4: To view information about Maintenance Tasks at a specific Destination"])
        filter_destination_menu.add_row(["B: To Go Back"])
        filter_destination_menu.add_row(["Q: To Quit"])
        filter_destination_menu.align = "l"

        return filter_destination_menu 
    
    def FilterDateMenu(self) -> PrettyTable:
        """ Function creates the filter date Menu, used by the viewingUI (viewMenu) for the other UI's to call and use to print out for the user to see """
        filter_date_menu = PrettyTable()
        filter_date_menu.title = "Specific Date Information"
        filter_date_menu.header = False
        filter_date_menu.add_row(["1: To view tasks over a specific time period"]) # Add the relevant rows to the menu
        filter_date_menu.add_row(["B: To Go Back"])
        filter_date_menu.add_row(["Q: To Quit"])
        filter_date_menu.align = "l"

        return filter_date_menu 

    # To display all the information we have in pretty tables
    def displayEmployees(self, destination = None) -> None:
        """ Function creates a table to display all of the employees in a specified format, it is also used when the user is filtering on a destination, the logic layer only provides us with a list of employees related to that destination"""
        # For displaying employees in the pretty table we omit, Address and Home phone
        # User can easily find that information through choosing to view additional information on a specific employee
        employeespretty = PrettyTable()
        employeespretty.field_names = ["Employee Number", "Employee Name", "Social Security Number", "GSM Phone","Email", "Working at destination", "Type of Employee"]
        employees = self.LogicLayerWrapper.getEmployeeData(destination)
        for employee in employees:
            employeespretty.add_row([employee.employeeID, employee.name, employee.socialSecurity, employee.gsmPhone, employee.email, employee.workLocation , employee.type], divider=True)        
        employeespretty.align = 'l'
        employeespretty.max_table_width = 150
        employeespretty.min_table_width = 100
        employeespretty.max_width = 30
        print(employeespretty)

    def displayManagers(self, destination = None) -> None:
        """ Function creates a table to display all of the managers in a specified format, it is also used when the user is filtering on a destination, the logic layer only provides us with a list of managers related to that destination"""
        # For displaying managers in the pretty table we omit, Address and Home phone
        # User can easily find that information through choosing to view additional information on a specific employee
        managerspretty = PrettyTable()
        managerspretty.field_names = ["Employee Number", "Employee Name", "Social Security Number", "GSM Phone","Email", "Working at destination", "Type of Employee"]
        managers = self.LogicLayerWrapper.getManagers(destination)
        for manager in managers:
            managerspretty.add_row([manager.employeeID, manager.name, manager.socialSecurity, manager.gsmPhone, manager.email, manager.workLocation , manager.type], divider=True)        
        managerspretty.align = 'l'
        managerspretty.max_table_width = 150
        managerspretty.min_table_width = 100
        managerspretty.max_width = 30
        print(managerspretty)
        
    def displayContractors(self, destination=None) -> None:
        """ Function creates a table to display all of the contractors in a specified format, it is also used when the user is filtering on a destination, the logic layer only provides us with a list of contractors related to that destination"""
        # For displaying contractors in the pretty table we omit, Address, Home Phone, Previous Task and Performance Rating
        # User can easily find that information through choosing to view additional information on that specific contractor
        contractors_pretty = PrettyTable()
        contractors_pretty.field_names = ["Contractor Number", "Name", "Social Security", "GSM Phone", "Email", "Work Location", "Type", "Contractor Contact", "Opening Hours"]
        contractors = self.LogicLayerWrapper.getContractorData(destination)

        for contractor in contractors:
            contractors_pretty.add_row([contractor.employeeID, contractor.name, contractor.socialSecurity, contractor.gsmPhone, contractor.email, contractor.workLocation, contractor.type,  contractor.contractorContact, contractor.openingHours])
        contractors_pretty.align = 'l'  
        contractors_pretty.max_table_width = 160 
        contractors_pretty.min_table_width = 100  
        contractors_pretty.max_width = 30  
        contractors_pretty.hrules = True 
        contractors_pretty.vrules = True

        print(contractors_pretty)

    def displayProperties(self, destination = None) -> None:
        """ Function creates a table to display all of the properties in a specified format, it is also used when the user is filtering on a destination, the logic layer only provides us with a list of properties related to that destination"""
        # Omitted from this table for clarity, Tub available and ovens available
        propertiespretty = PrettyTable()
        propertiespretty.field_names = ["Property Number", "Property Name", "Description", "Location", "Available for rental", "Pool Available"]
        properties = self.LogicLayerWrapper.getPropertyData(destination)
        for property in properties:
            propertiespretty.add_row([property.propertyID,property.nameOfProperty,property.description,property.location,property.availability,property.hasAPool])
        propertiespretty.align = 'l'
        propertiespretty.max_width = 30
        propertiespretty.max_table_width = 150
        propertiespretty.min_table_width = 100
        propertiespretty.hrules = True 
        propertiespretty.vrules = True  
  
        print(propertiespretty)

    def displayMaintenanceTasks(self, destination = None) -> None:
        """ Function creates a table to display all of the maintenance tasks in a specified format, it is also used when the user is filtering on a destination, the logic layer only provides us with a list of maintenance tasks related to that destination"""
        maintenanceTasks = self.LogicLayerWrapper.getMaintenanceTaskData(destination)
        tasks_pretty = PrettyTable()
        tasks_pretty.field_names = ["Task ID", "Property ID", "Description", "Start Date", "End Date", "Status", "Priority", "Recurring"]
        for task in maintenanceTasks:
            tasks_pretty.add_row([task.maintenanceID,task.propertyID,task.description,task.startDate,task.endDate,task.statusMaintenance,task.priority,task.recurring])
        tasks_pretty.align = "l"  
        tasks_pretty.max_width = 30  
        tasks_pretty.min_table_width = 100 
        tasks_pretty.max_table_width = 150  
        tasks_pretty.hrules = True 
        tasks_pretty.vrules = True 

        # Display the table
        print(tasks_pretty)

    def displayMaintenanceSchedules(self) -> None:
        """ Function creates a table to display all of the maintenanceschedules in a specified format"""
        maintenanceSchedules = self.LogicLayerWrapper.getMaintenanceScheduleData()
        schedules_pretty = PrettyTable()
        schedules_pretty.field_names = ["Schedule ID", "Maintenance ID", "Task Type", "Frequency", "Start Date"]
        for schedule in maintenanceSchedules:
            schedules_pretty.add_row([ schedule.maintenanceScheduleID, schedule.maintenanceID, schedule.taskType, schedule.frequency, schedule.startDate])
        schedules_pretty.align = "l"  
        schedules_pretty.max_width = 30  
        schedules_pretty.min_table_width = 100  
        schedules_pretty.max_table_width = 140
        schedules_pretty.hrules = 1 
        schedules_pretty.hrules = True 
        schedules_pretty.vrules = True 

        # Display the table
        print(schedules_pretty)


    def displayMaintenanceReports(self) -> None:
        """ Function creates a table to display all of the maintenance reports in a specified format"""
        # Omitted Ready to close and supervisor feedback
        maintenanceReports = self.LogicLayerWrapper.getMaintenanceReportData()
        maintenance_reports_pretty = PrettyTable()
        maintenance_reports_pretty.field_names = ["Report ID", "Maintenance ID", "Employee ID", "Material Cost", "Contractor ID", "Contractor Cost", "Supervisor Closed"]

        # We need to change what the user sees based on whats inside the attribute
        for report in maintenanceReports:
            maintenance_reports_pretty.add_row([
            report.maintenanceReportID,
            report.maintenanceID,
            report.employeeID if report.employeeID else "N/A",
            report.materialCost,
            report.contractorID if report.contractorID else "N/A",
            report.contractorCost if report.contractorCost else "N/A",
            "Yes" if report.supervisorClosed.lower() == "true" else "No"
            ])

        maintenance_reports_pretty.align = "l"  
        maintenance_reports_pretty.max_width = 90
        maintenance_reports_pretty.min_table_width = 100 
        maintenance_reports_pretty.max_table_width = 150
        maintenance_reports_pretty.hrules = True 
        maintenance_reports_pretty.vrules = True 

        print(maintenance_reports_pretty)

    def displayDestinations(self) -> None:
        """ Function creates a table to display all of the destinations in a specified format"""
        destinations = self.LogicLayerWrapper.getDestinationData()
        destinations_pretty = PrettyTable()
        destinations_pretty.field_names = ["Destination ID", "Name", "Country", "Timezone", "Airport Name", "Phone Number", "Opening Hours", "Manager ID"]
        for destination in destinations:
            destinations_pretty.add_row([destination.destinationID, destination.name, destination.country, destination.timezone, destination.airportName, destination.phoneNumber, destination.openingHours, destination.managerOfDestination])
        destinations_pretty.align = "l" 
        destinations_pretty.max_width = 30 
        destinations_pretty.min_table_width = 100 
        destinations_pretty.max_table_width = 160 
        destinations_pretty.hrules = True 

        print(destinations_pretty)
