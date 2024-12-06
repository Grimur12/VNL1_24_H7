## Test to create an employee
from os import system, name

from Logic_Layer.LogicLayerAPI import LogicLayerAPI

class UItest:
    def __init__(self) -> None:
        self.logicLayerWrapper = LogicLayerAPI()

    def display_temp_employee(self, temp, error = None):

        self.clear_terminal()

        print("\n--- Adding a new Employee ---")
        print(temp)            
        print("--------------------------\n")

        if error:
            print(f"Error: {error}\n")

    def display_temp_property(self, temp, error = None):
        
        self.clear_terminal()

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

    def printContractor(self, contractor):

        print("\n--- Contractor Information ---")

        print("--------------------------\n")

    def updatePropertyMenu(self, property, error = None):
        
        self.clear_terminal()
        print(f"""
--- Updating employee {property.propertyID} ---
ID: {property.propertyID}
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
        
    def updateEmployeeMenu(self, employee, error = None):
        """ Turns the class into a string to print out with, mainly for UI display """
        self.clear_terminal()
        print(f"""
--- Updating employee {employee.employeeID} ---
You can not change Employee's ID, Social Security or Type
ID: {employee.employeeID}
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
    
    def updateContractorMenu(self, contractor, error = None):
        """ Turns the class into a string to print out with, mainly for UI display """
        self.clear_terminal()
        print(f"""
--- Updating employee {contractor.employeeID} ---
You can not change Employee's ID, Social Security or Type
ID: {contractor.employeeID}
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

    def employeeMenu(self):
        self.clear_terminal()
        while True:
            print("Type 1 to create an Employee")
            print("Type 2 to create a Manager")
            print("Type 3 to create a Contractor")
            print("Type 4 to update an Employee")
            print("Type 5 to update a Contractor")
            print("Type 6 to view all Employees")
            print("B to go back")
            print("Q to Quit")
            employee_user_choice = input("Choice: ")
            
            if employee_user_choice.lower() == "q":
                print("Quitting")
                exit()
            elif employee_user_choice.lower() == "b":
                break

            elif employee_user_choice in ["1","2","3"]:
                self.createEmployee(employee_user_choice)
                self.clear_terminal()
            elif employee_user_choice == "4":
                ID = input("ID of the Employee to update: ")
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clear_terminal()
                    continue
                self.updateEmployee(ID)
                self.clear_terminal()
            elif employee_user_choice == "5":
                ID = input("ID of the Contractor to update: ")
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clear_terminal()
                    continue
                self.updateContractor(ID)
                self.clear_terminal()
            elif employee_user_choice == "6":
                self.clear_terminal()
                self.displayEmployees()
            else:
                print("Invalid Input")

    def propertyMenu(self):
        self.clear_terminal()
        while True:
            print("Type 1 to create a Property")
            print("Type 2 to update a Property")
            print("Type 3 to view all Properties")
            print("B to go back")
            print("Q to Quit")
            property_user_choice = input("Choice: ")

            if property_user_choice.lower() == "q":
                print("Quitting")
                exit()
            elif property_user_choice.lower() == "b":
                break
            elif property_user_choice == "1": # Creating a property
                self.createProperty()
                self.clear_terminal()
            elif property_user_choice == "2": # Update a property
                ID = input("ID of the Property to update: ")
                if ID.lower() == "q":
                    print("Quitting")
                    exit()
                elif ID.lower() == "b":
                    self.clear_terminal()
                    continue
                self.updateProperty(ID)
                self.clear_terminal()
            elif property_user_choice == "3": #View a property
                self.clear_terminal()
                self.displayProperties()
            else:
                print("Invalid Input")
        
    def maintenanceMenu(self):
        self.clear_terminal()
        while True:
            print("Type 1 to create a Maintenance Task")
            print("Type 2 to add a Maintenane Task to a Schedule")
            print("Type 3 to update a Maintenance Schedule")
            print("Type 4 to change Maintenance Task Status")
            print("Type 5 to view all Maintenance Tasks")
            print("Type 6 to view all Scheduled Maintainance Tasks")
            print("B to go back")
            print("Q to Quit")
            print("NOT IMPLEMENTED YET, Press B to go back or Q to quit")
            maintenance_user_choice = input("Choice: ")

            if maintenance_user_choice.lower() == "q":
                print("Quitting")
                exit()
            elif maintenance_user_choice.lower() == "b":
                break
            elif maintenance_user_choice == "1":
                self.createMaintenance()
                self.clear_terminal()
            elif maintenance_user_choice == "2":
                self.scheduleMaintenance()
                self.clear_terminal()
            elif maintenance_user_choice == "3":
                self.updateMaintenanceSchedule()
                self.clear_terminal()
            elif maintenance_user_choice == "4":
                self.updateMaintenanceStatus()
                self.clear_terminal
            elif maintenance_user_choice == "5":
                self.clear_terminal()
                self.displayMaintenance()
            elif maintenance_user_choice == "6":
                self.clear_terminal()  
                self.displayMaintenanceSchedule()
            else:
                print("Invalid Input")
                
    def clear_terminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def createProperty(self):

        count = 1
        tempProperty = self.logicLayerWrapper.createTempProperty()
        error_message = None
        while count < 7:
            self.display_temp_property(tempProperty, error_message)
            userInput = input("Information : ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput.lower() == "b":
                break

            try:
                if self.logicLayerWrapper.validatePropertyInput(userInput, count, tempProperty):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        
        if userInput.lower() != "b":
            self.display_temp_property(tempProperty, error_message)
            self.logicLayerWrapper.createProperty(tempProperty)
            print("You have successfully created a new Property")
                    

    def createEmployee(self,type_of_employee):

        # Type of employee should be "1" for Employee, "2" for Contractor 
        count = 1
        temp = self.logicLayerWrapper.getTempEmployee(type_of_employee)
        error_message = None
        if type_of_employee == "3":
            max_parameters = 12
        else:
            max_parameters = 8
        while count < max_parameters:
            self.display_temp_employee(temp, error_message)
            userInput = input("Information: ")
            if userInput.lower() == "q":
                print("Quitting")
                exit()
            elif userInput.lower() == "b":
                print("Going back")
                break

            try:
                if self.logicLayerWrapper.validateEmployeeInput(userInput, count, temp):
                    count +=1
                    error_message = None
            except ValueError as error:
                error_message = error
                continue
        if userInput.lower() != "b":
            self.display_temp_employee(temp, error_message)
            self.logicLayerWrapper.createEmployee(temp)
            print("You have successfully created the employee")

    def updateEmployee(self, ID):
        while True:
            try:
                employee = self.logicLayerWrapper.getEmployeebyID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Employee to update: ")
                continue
        
        error_message = None
        while True:
            self.updateEmployeeMenu(employee, error_message)
            userInput = input("Number of the attribute you want to change: ")
            
            if userInput.lower() == "q":
                exit() ## QUIT...
            elif userInput.lower() == "b":
                print("Going back")
                break ## Go back one
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput in ["1", "3", "4", "5", "6", "7"]:

                newParam = input("New Information: ").strip()
                try:
                    self.logicLayerWrapper.validateEmployeeInput(newParam, userInput, employee)
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"
        if userInput.lower() != "b":
            self.logicLayerWrapper.update_employee_data(employee)

    def updateContractor(self, ID):
        while True:
            try:
                employee = self.logicLayerWrapper.getContractorbyID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Employee to update: ")
                continue

        error_message = None
        while True:
            self.updateContractorMenu(employee, error_message)
            userInput = input("Number of the attribute you want to change: ")

            if userInput.lower() == "Q":
                exit() ## QUIT...
            elif userInput.lower() == "B":
                print("Going back")
                break ## Go back one
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput in ["1", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:

                newParam = input("New Information: ").strip()
                try:
                    self.logicLayerWrapper.validateEmployeeInput(newParam, userInput, employee)
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"
        if userInput.lower() != "b":
            self.logicLayerWrapper.update_employee_data(employee)

    def updateProperty(self, ID):
        while True:
            try:
                property = self.logicLayerWrapper.getPropertyByID(ID)
                break
                
            except ValueError as error:
                print(f"Error: {error}")
                ID = input("ID of the Property to update: ")
                continue
        error_message = None
        while True:
            self.updatePropertyMenu(property, error_message)
            userInput = input("Number of the attribute you want to change: ")

            if userInput.lower() == "q":
                exit() ## QUIT...
            elif userInput.lower() == "b":
                print("Going back")
                break ## Go back one
            elif userInput.lower() == "d":
                print("Saving Changes")
                break

            elif userInput in ["1", "3", "4", "5", "6"]:

                newParam = input("New Information: ").strip()
                try:
                    self.logicLayerWrapper.validatePropertyInput(newParam, userInput, property)
                    error_message = None
                except ValueError as error:
                    error_message = error
                    continue
            else:
                error_message = "Not a Valid Choice, Try Again"
        if userInput.lower() != "b":
            self.logicLayerWrapper.updateProperty(property)

    def displayEmployees(self):
        employees = self.logicLayerWrapper.getEmployeeData()
        for employee in employees:
            print(employee)

    def displayProperties(self):
        properties = self.logicLayerWrapper.getPropertyData()
        for property in properties:
            self.printProperty(property)

    def run(self):
        while True:
            print("Type 1 to access Employee features")
            print("Type 2 to access Maintenance features")
            print("Type 3 to access Property features")
            print("B to go Back")
            print("Q to quit")
            user_choice = input("Type 1, 2, 3 or q: ")
            # Exit out of the loop

            if user_choice.lower() == "q":
                print("Qutting")
                exit()

            if user_choice.lower() == "b":
                print("Going back")
                break

            if user_choice == "1":
                self.employeeMenu()
            elif user_choice == "2":
                self.maintenanceMenu()
            elif user_choice == "3":
                self.propertyMenu()
            else:
                print("Invalid Input")


if __name__ == "__main__":
    ui = UItest()
    ui.clear_terminal()
    while True:
        print("1: If you are a Manager")
        print("Type Q to quit the program")

        initial_input = input("Choice: ")
        if initial_input.lower() == "q":
            print("Quitting")
            break
        elif initial_input == "1":
            ui.clear_terminal()
            ui.run()
        else:
            print("Invalid Input.")