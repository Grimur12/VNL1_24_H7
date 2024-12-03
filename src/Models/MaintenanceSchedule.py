#defining the Maintenance schedule classes.

class MaintenanceSchedule:
    def __init__(self, maintenanceSchedule_ID, maintenanceIDreference, employee_ID, taskType, frequency):
        """ Defines variables for Maintenance Schedule """
        self.maintenanceSchedule_ID = maintenanceSchedule_ID
        self.maintenanceIDreference = maintenanceIDreference
        self.employee_ID = employee_ID
        self.taskType = taskType
        self.frequency = frequency

    def maintenanceSchedule_Dict(self) -> dict:
        """ Returns all the variables in our Maintenance Schedule class into a dictionary """
        return {
        "maintenanceSchedule _ID": self.maintenanceSchedule_ID,
        "maintenanceIDreference": self.maintenanceIDreference,
        "employee_ID": self.employee_ID,
        "taskType": self.taskType,
        "frequency": self.frequency
        }

