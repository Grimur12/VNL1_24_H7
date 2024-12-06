
from os import system, name
# Need to make all these displays look better 
class Displays:
    def __init__(self):
        pass

    def editContractorMenu(self, contractor, error = None):
        """ Turns the class into a string to print out with, mainly for UI display """
        self.clearTerminal()
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

    def editEmployeeMenu(self, employee, error = None):
        """ Turns the class into a string to print out with, mainly for UI display """
        self.clearTerminal()
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

    def editPropertyMenu(self, property, error = None):
        
        self.clearTerminal()
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
        
    def clearTerminal(self):
        ## Not exactly how i want it... clears everything, needs to show errors...
        if name == "nt":
            system("cls")
        else:
            system("clear")