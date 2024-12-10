#defining the Maintenance schedule classes.

class MaintenanceSchedule:
    def __init__(self, ID, maintenanceID = "", taskType = "", frequency = "", startDate = "") -> None:
        """ Defines variables for Maintenance Schedule """
        # We reference the maintenanceID in the shcedule
        self.maintenanceScheduleID = ID
        self.maintenanceID = maintenanceID
        self.taskType = taskType
        self.frequency = frequency
        self.startDate = startDate

    def MaintenanceSchedule_Dict(self) -> dict:
        """ Returns all the variables in our Maintenance Schedule class into a dictionary """
        return {
        "maintenanceScheduleID": self.maintenanceScheduleID,
        "maintenanceID": self.maintenanceID,
        "taskType": self.taskType,
        "frequency": self.frequency,
        "startDate": self.startDate,
        }

