# Define Managers, Employees and Contractors

class Employee:
    def __init__(self, ID = "", name = "", socialSecurity = "", address = "", atHomePhone = "", gsmPhone = "", email = "", workLocation = "", type = "") -> None:
        """ Defines variables for our Employees """
        self.employeeID = ID # Unique ID for employees, shared with all types
        self.name = name # Name of the employee
        self.socialSecurity = socialSecurity # Social security number of the employee (For this assignment even though its not only in iceland we will go with the standard icelandic format)
        self.address = address # Address of that employee
        self.atHomePhone = atHomePhone # Home phone
        self.gsmPhone = gsmPhone # GSM phone
        self.email = email # email
        self.workLocation = workLocation # Reference to destinationID of destination 
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

class Contractor(Employee):
    def __init__(self, previousTask = "", performanceRating = "", contractorContact = "", openingHours = "", *args) -> None:
        super().__init__(*args)
        self.previousTask = previousTask # Previous tasks of employee, reference to maintenance ID
        self.performanceRating = performanceRating # Performance rating of that task or tasks
        self.contractorContact = contractorContact # Reference to employee ID of an employee that is either a General or Manager type
        self.openingHours = openingHours # Opening hours of the employee workplace
        
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
        "contractorContact": self.contractorContact, # Reference to employeeID of an employee
        "openingHours": self.openingHours
        }