#defining the Maintenance schedule classes.

class MaintenanceSchedule:
    def __init__(self, ID, maintenanceID = "", taskType = "", frequency = "", startDate = "") -> None:
        """ Defines variables for Maintenance Schedule """
        # We reference the maintenanceID in the shcedule
        self.maintenanceScheduleID = ID # Unique ID of the schedule
        self.maintenanceID = maintenanceID # Reference to the maintenance that is being scheduled,
        self.taskType = taskType # Type of maintenance is it normal (cleaning the sink) or abnormal (checking for leaks)
        self.frequency = frequency # Daily, Weekly, Monthly
        self.startDate = startDate # Starting Date of the schedule

    def MaintenanceSchedule_Dict(self) -> dict:
        """ Returns all the variables in our Maintenance Schedule class into a dictionary """
        return {
        "maintenanceScheduleID": self.maintenanceScheduleID,
        "maintenanceID": self.maintenanceID,
        "taskType": self.taskType,
        "frequency": self.frequency,
        "startDate": self.startDate,
        }

