#defining the class Maintenence

class Maintenance:
    def __init__(self, ID, propertyID = "", description = "", startDate = "", endDate = "", statusMaintenance = "", priority = "", recurring = "") -> None:
        """ Defines variables for Maintenances """
        # One employee / contractor per maintenance
        self.maintenanceID = ID 
        self.propertyID = propertyID # Reference to a specific property by ID
        self.description = description # To say what the task is about
        self.startDate = startDate # Starting date of the maintenance Task
        self.endDate = endDate # Ending date of the maintenance Task
        self.statusMaintenance = statusMaintenance # Current status, Ongoing or Closed.. 
        self.priority = priority # Priority should be either Emergency, Now or ASAP, can change but not after a maintenance report has been made
        self.recurring = recurring # This is either a recurring task or not, if it is you can create multiple maintenance Reports on it if not you can only make one
        
    def Maintenance_Dict(self) -> dict:
        """ Returns all the variables in our Maintenance class into a dictionary """
        return {
        "maintenanceID": self.maintenanceID,
        "propertyID": self.propertyID,
        "description": self.description,
        "startDate": self.startDate,
        "endDate": self.endDate,
        "statusMaintenance": self.statusMaintenance,
        "priority": self.priority,
        "recurring": self.recurring
        }