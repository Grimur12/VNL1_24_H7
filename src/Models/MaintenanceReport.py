## Manager creates a maintenance Task.
## Employee or contractor chooses task to assign the 
## 

## Employee once finished with the task has to create a maintenance Report
## and flag it as being ready to be closed
## After maintenance has been flagged as closed the manager can then accept it and then close the maintenance Task

class MaintenanceReport:
    def __init__(self, ID = "", maintenanceID = "", employeeID = "", materialCost = "", contractorID = "", contractorCost = "", readyToClose = "True" , supervisorClosed = "False", supervisorFeedback = "") -> None:
        self.maintenanceReportID = ID # Unique ID
        self.maintenanceID = maintenanceID # Reference to a Maintenance ID
        self.employeeID = employeeID # Reference to employee that decides to take the task
        self.materialCost = materialCost 
        self.contractorID = contractorID # This is a contractor ID, reference to contractor
        self.contractorCost = contractorCost
        self.readyToClose = readyToClose # When creating a new maintenanceReport its assumed that the task is ready to be closed since the task is finished
        self.supervisorClosed = supervisorClosed # If the supervisor accepts he closes the report and maintenance task and writes good feedback if not he denys the closing and writes some feedback on why.
        self.supervisorFeedback = supervisorFeedback # Manager needs to provide feedback when closing a report

    def MaintenanceReport_Dict(self):
        """ Returns all the variables in our MaintenanceReport class into dictionary, needed for DB json writing """
        return {
        "maintenanceReportID": self.maintenanceReportID, # Self assigned
        "maintenanceID": self.maintenanceID, # Mandatory
        "employeeID": self.employeeID, # Not Mandatory, If there is an employee you cant input a contractor
        "materialCost": self.materialCost,
        "contractorID": self.contractorID, # Not Mandatory, If there is a contractor you cant input an employee
        "contractorCost": self.contractorCost, # Mandatory if there is a contractorID, but otherwise if employeeID you cant input anything here
        "readyToClose": self.readyToClose, # when you create the report it is automatically assumed to be ready to be closed
        "supervisorClosed": self.supervisorClosed,
        "supervisorFeedback": self.supervisorFeedback
        }