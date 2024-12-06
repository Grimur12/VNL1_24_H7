## Manager creates a maintenance Task.
## Employee or contractor chooses task to assign the 
## 

## Employee once finished with the task has to create a maintenance Report
## and flag it as being ready to be closed
## After maintenance has been flagged as closed the manager can then accept it and then close the maintenance Task

class MaintenanceReport:
    def __init__(self, maintenanceReportID = "", maintenanceID = "", employeeID = "", contractorID = "", contractorCost = "", readyToClose = "") -> None:
        self.maintenanceReportID = maintenanceReportID
        self.maintenanceID = maintenanceID
        self.employeeID = employeeID # Reference to employee that decides to take the task
        self.contractor = contractorID # This is a contractor ID, reference to contractor
        self.contractorcost = contractorCost
        self.readyToClose = readyToClose

    def MaintenanceReport_Dict(self):
        """ Returns all the variables in our MaintenanceReport class into dictionary, needed for DB json writing """
        return {
        "maintenanceReportID": self.maintenanceReportID
        }



#  It should possible to request, in a print-friendly format:
# -All maintenance performed on a specified property over a specified date range
# -An overview of all tasks completed by a specified contractor over a specified date
# range
# -An overview of all tasks completed by a specified employee over a specified date
# range

# Contractor registration:
# -A superior must be able to register new contractors and change contractor info
# -Employees must be able to find information on contractors
# -When completing a maintenance report, it must be possible to reference at least one
# contractor (if relevant)
# -When filing a maintenance report, where a contractor is referenced, it should also be
# possible to specify what the contractor was paid, and a superior should be able to add
# comments on the ticket when they close it.

# Recurring maintenance:
# -When registering new tickets it should be possible to indicate whether they are
# recurring, and if so then the interval (daily, weekly, monthly, annually), based on
# an initial date thats also registered on the ticket

# Ticket prioritization:
# -It must be possible to prioritize tickets, with at least three levels of urgency:
# Emergency, Now, As soon as possible. Hint: User testing could be helpful in
# determining the best way to implement this.
# -Superiors handle assigning priority levels to outstanding tickets and can modify it,
# but they cannot modify it when a report has been turned in for that ticket.
# Summaries and overviews: It should possible to request, in a print-friendly format:
# -All maintenance performed on a specified property over a specified date range
# -An overview of all tasks completed by a specified contractor over a specified date
# range
# -An overview of all tasks completed by a specified employee over a specified date
# range