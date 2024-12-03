# Define Managers, Employees and Contractors

class Employee:
    def __init__(self, ID, name, socialSecurity, address, atHomePhone, gsmPhone, email, workLocation, type) -> None:
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
        "ID": self.employeeID,
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
    def __init__(self, *args, previousTask, performanceRating, contractorContact, openingHours) -> None:
        super().__init__(self, *args)
        self.previousTask = previousTask
        self.performanceRating = performanceRating
        self.contractorContact = contractorContact
        self.openingHours = openingHours
        
        
    def contractor_dict(self) -> dict:
        """ Returns all the variables in our Employee class into dictionary, needed for DB json writing """
        return {
        "ID": self.ID,
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


# class Manager(Employee):
#     def __init__(self) -> None:
#         pass

#     def Manager_dict(self):
#         pass


