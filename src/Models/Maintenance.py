# Here is our Maintenance class

class Maintenance:
    def __init__(self, ID, propertyID = "" ,startDate = "", endDate = "", statusMaintenance = "", feedback = "", priority = "") -> None:
        """ Defines variables for Maintenances """
        # One employee / contractor per maintenance
        self.maintenanceID = ID
        self.propertyID = propertyID # Reference to a specific property by ID
        self.startDate = startDate
        self.endDate = endDate
        self.statusMaintenance = statusMaintenance
        self.feedback = feedback
        self.priority = priority
        
    def Maintenance_Dict(self) -> dict:
        """ Returns all the variables in our Maintenance class into a dictionary """
        return {
        "maintenanceID": self.maintenanceID,
        "propertyID": self.propertyID,
        "startDate": self.startDate,
        "endDate": self.endDate,
        "statusMaintenance": self.statusMaintenance,
        "feedback": self.feedback,
        "priority": self.priority,
        }