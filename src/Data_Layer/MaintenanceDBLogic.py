# Maintenance DB Logic
import os
import json
from Models.Maintenance import Maintenance
from Models.MaintenanceSchedule import MaintenanceSchedule

class MaintenanceDBLogic:

    def __init__(self):
        self.maintenance = []
        self.maintenanceSchedule = []
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.maintenance_file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "Maintenance.json")
        self.maintenance_Schedule_file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "MaintenanceSchedule.json")

    def loadMaintenanceLog(self) -> None:
        """ Function loads all saved maintenances from DB and turns back into class instances of Maintenance and saves it internally """
        with open(self.maintenance_file_path, "r") as maintenanceDBOpen:
            maintenance_list = json.load(maintenanceDBOpen)
        for maint in maintenance_list:
            self.maintenance.append(Maintenance(*maint.values()))

    def loadMaintenanceSchedule(self) -> None:
        with open(self.maintenance_Schedule_file_path, "r") as maintenanceScheduleDBOpen:
            maintenanceSchedule_list = json.load(maintenanceScheduleDBOpen)
        for schedule in maintenanceSchedule_list:
            self.maintenance.append(MaintenanceSchedule(*schedule.values()))

    def updateMaintenanceStatus(self) -> None:
        pass

    def updateMaintenanceSchedule(self) -> None:
        pass

    def createMaintenanceSchedule(self) -> None:
        pass

    def createMaintenance(self) -> None:
        pass

    def removeMaintenance(self) -> None:
        pass

    def saveMaintenance(self) -> None:
        pass