#defining the class Maintenence

class Maintenance:
    def __init__(self, ID ,contractors, startDate, statusMaintenance, standardMaintenance, totalCost, contractorCost, priority, managerApproval = 0, feedback = 0, endDate = 0,) -> None:
        """ Defines variables for Maintenances """
        self.maintenanceID = ID
        self.contractors = contractors
        self.startDate = startDate
        self.endDate = endDate
        self.statusMaintenance = statusMaintenance
        self.standardMaintenance = standardMaintenance
        self.totalCost = totalCost
        self.contractorCost = contractorCost
        self.managerApproval = managerApproval
        self.feedback = feedback
        self.priority = priority
        
        

    def Maintenance_Dict(self) -> dict:
        """ Returns all the variables in our Maintenance class into a dictionary """
        return {
        "maintenanceID": self.maintenanceID,
        "contractors": self.contractors,
        "startDate": self.startDate,
        "statusMaintenance": self.statusMaintenance,
        "standardMaintenance": self.standardMaintenance,
        "hasAPool": self.totalCost,
        "totalCost": self.contractorCost,
        "managerApproval": self.managerApproval,
        "priority": self.priority,
        "feedback": self.feedback,
        "endDate": self.endDate
        }