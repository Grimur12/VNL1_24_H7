# Define Managers, Employees and Contractors

class Employee:
    def __init__(self, ID = "", name = "", socialSecurity = "", address = "", atHomePhone = "", gsmPhone = "", email = "", workLocation = "", type = "") -> None:
        """ Defines variables for our Employees """
        self.employeeID = ID # need to calculate UNIQUE ID somewhere and store it...
        self.name = name
        self.socialSecurity = socialSecurity
        self.address = address
        self.atHomePhone = atHomePhone
        self.gsmPhone = gsmPhone
        self.email = email
        self.workLocation = workLocation 
        self.type = type # Type defines if employee is, general employee, manager or contractor

    def Employee_dict(self) -> dict:
        """ Returns all the variables in our Employee class into dictionary, needed for DB json writing """
        return {
        "employeeID": self.employeeID,
        "name": self.name,
        "socialSecurity": self.socialSecurity,
        "address": self.address,
        "atHomePhone": self.atHomePhone,
        "gsmPhone": self.gsmPhone,
        "email": self.email,
        "workLocation": self.workLocation,
        "type": self.type
        }
    
    def __str__(self):
        """ Turns the class into a string to print out with, mainly for UI display """
        return f"""
--- Employee Details ---
ID: {self.employeeID}
Name: {self.name}
Social Security: {self.socialSecurity}
Address: {self.address}
Home Phone: {self.atHomePhone}
GSM Phone: {self.gsmPhone}
Email: {self.email}
Work Location: {self.workLocation}
Type: {self.type}
------------------------
"""

class Contractor(Employee):
    def __init__(self, previousTask = "", performanceRating = "", contractorContact = "", openingHours = "", *args) -> None:
        ## need to change the contractor contact to employeeID not phone number
        super().__init__(*args)
        self.previousTask = previousTask
        self.performanceRating = performanceRating
        self.contractorContact = contractorContact
        self.openingHours = openingHours
        
    def Contractor_dict(self) -> dict:
        """ Returns all the variables in our Employee class into dictionary, needed for DB json writing """
        return {
        "ID": self.employeeID,
        "name": self.name,
        "socialSecurity": self.socialSecurity,
        "address": self.address,
        "atHomePhone": self.atHomePhone,
        "gsmPhone": self.gsmPhone,
        "email": self.email,
        "workLocation": self.workLocation,
        "type": self.type,
        "previousTask": self.previousTask,
        "performanceRating": self.performanceRating,
        "contractorContact": self.contractorContact,
        "openingHours": self.openingHours
        }
    
    def __str__(self):
        """ Turns the class into a string to print out with, mainly for UI display """
        contractor_details = super().__str__()  # Using the str function in the employee class because its the same attributes
        return contractor_details + f"""
Previous Task: {self.previousTask}
Performance Rating: {self.performanceRating}
Contractor Contact: {self.contractorContact}
Opening Hours: {self.openingHours}
------------------------
        """


# class Manager(Employee):
#     def __init__(self) -> None:
#         pass

#     def Manager_dict(self):
#         pass


