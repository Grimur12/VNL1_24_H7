
from os import system, name
from prettytable import PrettyTable

class Displays:
    def __init__(self):
        pass

    def clearTerminal(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")  

    # ALL FUNCTIONS TO PRINT THE MODEL CLASSES, Editing and Creating, title message is default for information but editing or creating can specify another title if they wish

    def printProperty(self, property, title_message = "Property Information", error = None, edit_message = "", done_message = "", mode = ""):

        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        print(f"Property Number: {property.propertyID}")
        print(f"Name: {property.nameOfProperty}" + ("              // Ex. Igloo" if mode == "hints" else ""))
        print(f"Location: {property.location}" + ("          // Ex. 1 (Valid Destination Number)" if mode == "hints" else ""))
        print(f"Availability: {property.availability}" + ("      // Ex. True" if mode == "hints" else ""))
        print(f"Pool: {property.hasAPool}" + ("              // False" if mode == "hints" else ""))
        print(f"Hot Tub: {property.hasATub}" + ("           // False" if mode == "hints" else ""))
        print(f"Ovens: {property.hasOvens}" + ("             // True" if mode == "hints" else ""))
        print("--------------------------")
        print("B: To Go Back")
        print("Q: To Quit")
        print(f"{done_message}") 

        if error:
            print(f"Error: {error}\n")

    def printEmployee(self, employee, title_message = "Employee Information", error = None, edit_message = "", done_message = "", mode = ""):
        
        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        if employee.type == "Contractor":

            print(f"Employee Number: {employee.employeeID}")
            print(f"1.Name: {employee.name}" + ("                // Ex. Karl Jónsson" if mode == "hints" else ""))
            print(f"2.Social Security: {employee.socialSecurity}" + ("     // Ex. 020398-2490" if mode == "hints" else ""))
            print(f"3.Address: {employee.address}" + ("             // Ex. Brekkuvegur 91" if mode == "hints" else ""))
            print(f"4.Home Phone: {employee.atHomePhone}" + ("          // Ex. 662-1234" if mode == "hints" else ""))
            print(f"5.GSM Phone: {employee.gsmPhone}" + ("           // Ex. 882-1234" if mode == "hints" else ""))
            print(f"6.Email: {employee.email}" + ("               // Ex. Karl@gmail.com" if mode == "hints" else ""))
            print(f"7.Work Location: {employee.workLocation}" + ("       // Ex. 1 (Valid Destination Number)" if mode == "hints" else ""))
            print(f"Type: {employee.type}")
            print(f"8.Previous Task: {employee.previousTask}" + ("       // Ex. 1 or 1,2,3 (Valid Maintenance Task(s), Can Be Empty)" if mode == "hints" else ""))
            print(f"9.Performance Rating: {employee.performanceRating}" + ("  // Ex. 9 (Can Be Empty If No Previous Tasks)" if mode == "hints" else ""))
            print(f"10.Contractor Contact: {employee.contractorContact}" + (" // Ex. 1 (Valid Employee Number)" if mode == "hints" else ""))
            print(f"11.Opening Hours: {employee.openingHours}" + ("      // Ex. 9-5" if mode == "hints" else ""))

        else:

            print(f"Employee Number: {employee.employeeID}")
            print(f"1.Name: {employee.name}" + ("                // Ex. Karl Jónsson" if mode == "hints" else ""))
            print(f"2.Social Security: {employee.socialSecurity}" + ("     // Ex. 020398-2490" if mode == "hints" else ""))
            print(f"3.Address: {employee.address}" + ("             // Ex. Brekkuvegur 91" if mode == "hints" else ""))
            print(f"4.Home Phone: {employee.atHomePhone}" + ("          // Ex. 662-1234" if mode == "hints" else ""))
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

    def printMaintenanceTask(self, task, title_message = "Maintenance Task Information", error = None, edit_message = "", done_message = "", mode = ""):
        
        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        print(f"Maintenance Number: {task.maintenanceID}")
        print(f"1.Maintenance done on Property Number: {task.propertyID}" + ("   // Ex. 1 (Valid Property Number)" if mode == "hints" else ""))
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

    def printMaintenanceSchedule(self, schedule, title_message = "Maintenance Schedule Information", error = None, edit_message = "", done_message = "", mode = ""):
        
        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        print(f"Maintenance Schedule Number: {schedule.maintenanceScheduleID}")
        print(f"1.Scheduled on Maintenance Task Number: {schedule.maintenanceID}" + ("       // Ex. 1 (Valid Maintenance Task Number)" if mode == "hints" else ""))
        print(f"2.Type of Maintenance Task: {schedule.taskType}" + ("                   // Ex. Normal" if mode == "hints" else ""))
        print(f"3.Frequency of Maintenance Task: {schedule.frequency}" + ("              // Ex. Weekly" if mode == "hints" else ""))
        print(f"4.Start Date of Scheduled Maintenance: {schedule.startDate}" + ("        // Ex. 10.03.2023.12:30" if mode == "hints" else ""))
        print("--------------------------")
        print("B: To Go Back")
        print("Q: To Quit")
        print(f"{done_message}") 

        if error:
            print(f"Error: {error}\n")

    def printMaintenanceReport(self, report, title_message = "Maintenance Report Information", error = None, edit_message = "", done_message = "", mode = ""):

        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        print(f"Maintenance Report Number: {report.maintenanceReportID}")
        print(f"1.Report on Maintenance Task Number: {report.maintenanceID}" + ("                         // Ex. 1 (Valid Maintenance Task Number)" if mode == "hints" else ""))
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

    def printDestination(self, destination, title_message = "Destination Information", error = None, edit_message = "", done_message = "", mode = ""):
        
        print(f"\n--- {title_message} ---")
        print(f"{edit_message}")
        print(f"Destination Number: {destination.destinationID}")
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

    def overWriteManager(self):
        print("\n----------------------------------------------------------------------------------------------------------------------")
        print("Destination already has a Manager, Would you like to demote him to a General Employee or abort creating a new Manager")
        print("----------------------------------------------------------------------------------------------------------------------\n")
        print("1: To continue creating the new Manager, demoting the current one")
        print("2: To stop the creation process of a new Manager")
        print("Q: To Quit the Program")


    # ALL MENUS USED BY THE UI

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
        view_menu.title = " Viewing menu"
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
        manager_add_menu.add_row(["6: Create a new Maintenance Schedule"])
        manager_add_menu.add_row(["B: Go Back"])
        manager_add_menu.add_row(["Q: Quit"])
        manager_add_menu.align = "l"

        return manager_add_menu

    def ManagerEditMenu(self):
        manager_edit_menu = PrettyTable()
        manager_edit_menu.title = "Edit Menu - Manager Position"
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
    
    def filterEmployeesMenu(self):
        filter_employees_menu = PrettyTable()
        filter_employees_menu.title = "Specific Employee Information"
        filter_employees_menu.header = False
        filter_employees_menu.add_row(["1: To view additional information of a specific Employee"])
        filter_employees_menu.add_row(["2: To view all tasks an Employee has worked on"])
        filter_employees_menu.add_row(["3: To view the Manager(s)"])
        filter_employees_menu.add_row(["B: To Go Back"])
        filter_employees_menu.add_row(["Q: To Quit"])
        filter_employees_menu.align = "l"

        return filter_employees_menu
    
    def filterContractorsMenu(self):
        filter_contractors_menu = PrettyTable()
        filter_contractors_menu.title = "Specific Contractor Information"
        filter_contractors_menu.header = False
        filter_contractors_menu.add_row(["1: To view additional information of a specific Contractor"])
        filter_contractors_menu.add_row(["2: To view all tasks a Contractor has worked on"])
        filter_contractors_menu.add_row(["B: To Go Back"])
        filter_contractors_menu.add_row(["Q: To Quit"])
        filter_contractors_menu.align = "l"

        return filter_contractors_menu

    def filterPropertiesMenu(self):
        filter_properties_menu = PrettyTable()
        filter_properties_menu.title = "Specific Property Information"
        filter_properties_menu.header = False
        filter_properties_menu.add_row(["1: To view additional information of a specific Property"])
        filter_properties_menu.add_row(["2: To view all Maintenance on a specific Property"])
        filter_properties_menu.add_row(["B: To Go Back"])
        filter_properties_menu.add_row(["Q: To Quit"])
        filter_properties_menu.align = "l"

        return filter_properties_menu 

    def filterMaintenanceMenu(self):
        filter_maintenance_menu = PrettyTable()
        filter_maintenance_menu.title = "Specific Maintenance Task Information"
        filter_maintenance_menu.header = False
        filter_maintenance_menu.add_row(["1: To view additional information of a specific Maintenance Task"])
        filter_maintenance_menu.add_row(["2: To view all Maintenance Tasks that are ready to be closed (Through closing the Maintenance Report)"])
        filter_maintenance_menu.add_row(["B: To Go Back"])
        filter_maintenance_menu.add_row(["Q: To Quit"])
        filter_maintenance_menu.align = "l"

        return filter_maintenance_menu 
    
    def filterMaintenanceScheduleMenu(self):
        filter_maintenanceSchdule_menu = PrettyTable()
        filter_maintenanceSchdule_menu.title = "Specific Maintenance Schedule Information"
        filter_maintenanceSchdule_menu.header = False
        filter_maintenanceSchdule_menu.add_row(["1: To view additional information of a specific Maintenance Schedule"])
        filter_maintenanceSchdule_menu.add_row(["B: To Go Back"])
        filter_maintenanceSchdule_menu.add_row(["Q: To Quit"])
        filter_maintenanceSchdule_menu.align = "l"

        return filter_maintenanceSchdule_menu 
    
    def filterMaintenanceReportMenu(self):
        filter_maintenanceReport_menu = PrettyTable()
        filter_maintenanceReport_menu.title = "Specific Maintenance Report Information"
        filter_maintenanceReport_menu.header = False
        filter_maintenanceReport_menu.add_row(["1: To view additional information of a specific Maintenance Report"])
        filter_maintenanceReport_menu.add_row(["B: To Go Back"])
        filter_maintenanceReport_menu.add_row(["Q: To Quit"])
        filter_maintenanceReport_menu.align = "l"

        return filter_maintenanceReport_menu 
    
    def filterDestinationMenu(self):
        filter_destination_menu = PrettyTable()
        filter_destination_menu.title = "Specific Destination Information"
        filter_destination_menu.header = False
        filter_destination_menu.add_row(["1: To view information about Employees at a specific Destination"])
        filter_destination_menu.add_row(["2: To view information about Contractors at a specific Destination"])
        filter_destination_menu.add_row(["3: To view information about Properties at a specific Destination"])
        filter_destination_menu.add_row(["B: To Go Back"])
        filter_destination_menu.add_row(["Q: To Quit"])
        filter_destination_menu.align = "l"

        return filter_destination_menu 
    
    def FilterDateMenu(self):
        filter_date_menu = PrettyTable()
        filter_date_menu.title = "Specific Date Information"
        filter_date_menu.header = False
        filter_date_menu.add_row(["1: To view tasks over a specific time period"])
        filter_date_menu.add_row(["B: To Go Back"])
        filter_date_menu.add_row(["Q: To Quit"])
        filter_date_menu.align = "l"

        return filter_date_menu 
