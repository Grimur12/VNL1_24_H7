#defining the class Maintenence

class Maintenance:
    def __init__(self, ID, propertyID = "" ,startDate = "", endDate = "", statusMaintenance = "", priority = "", feedback = "") -> None:
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
        "contractors": self.contractor,
        "startDate": self.startDate,
        "statusMaintenance": self.statusMaintenance,
        "standardMaintenance": self.standardMaintenance,
        "hasAPool": self.totalCost,
        "totalCost": self.contractorCost,
        "managerApproval": self.managerApproval,
        "priority": self.priority,
        "feedback": self.feedback,
        "endDate": self.endDate,
        }