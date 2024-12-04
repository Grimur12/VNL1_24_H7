# Maintenance DB Logic
import os
import json
from Models.Maintenance import Maintenance
from Models.MaintenanceSchedule import MaintenanceSchedule

class MaintenanceDBLogic:

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.maintenance_file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "Maintenance.json")
        self.maintenance_Schedule_file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "MaintenanceSchedule.json")

    def loadMaintenanceLog(self) -> list:
        """ Function loads all saved maintenances from DB and turns back into class instances of Maintenance and saves it internally """
        with open(self.maintenance_file_path, "r") as maintenanceDBOpen:
            maintenance_list = json.load(maintenanceDBOpen)
        maintenances = []
        for maint in maintenance_list:
            maintenances.append(Maintenance(*maint.values()))
        return maintenances

    def loadMaintenanceSchedule(self) -> list:
        with open(self.maintenance_Schedule_file_path, "r") as maintenanceScheduleDBOpen:
            maintenanceSchedule_list = json.load(maintenanceScheduleDBOpen)
        maintenanceSchedules = []
        for schedule in maintenanceSchedule_list:
            maintenanceSchedules.append(MaintenanceSchedule(*schedule.values()))
        return maintenanceSchedules

    def updateMaintenanceStatus(self, params) -> None:
        """ This function takes in a list of parameters, some may be new some may still be the older ones and stores them in the json DB """
        maintenances = self.loadMaintenanceLog()
        for index, maint in enumerate(maintenances):
            if maint.maintenanceID == params[0]:
                maintenances[index] = Maintenance(*params)
        self.saveMaintenance(maintenances)

    def updateMaintenanceSchedule(self, params) -> None:
        """ This function takes in a list of parameters, some may be new some may still be the older ones and stores them in the json DB """
        maintenanceSchedules = self.loadMaintenanceSchedule()
        for index, schedule in enumerate(maintenanceSchedules):
            if schedule.maintenanceScheduleID == params[0]:
                maintenanceSchedules[index] = MaintenanceSchedule(*params)
        self.saveMaintenanceSchedule(maintenanceSchedules)

    def createMaintenanceSchedule(self, params) -> None:
        """ This function takes in a list of parameters and creates a maintenanceSchedule and stores in the json DB """
        maintenanceSchedules = self.loadMaintenanceSchedule()
        maintenanceSchedules.append(MaintenanceSchedule(*params))
        self.saveMaintenanceSchedule(maintenanceSchedules)

    def createMaintenance(self, params) -> None:
        """ This function takes in a list of parameters and creates a maintenance and stores in the json DB """
        maintenances = self.loadMaintenanceLog()
        maintenances.append(Maintenance(*params))
        self.saveMaintenance(maintenances)

    def removeMaintenance(self, ID) -> None:
        """ We take in the ID of the maintenance we want to remove, find it, delete it from the internal list and save the internal list to DB """
        maintenances = self.loadMaintenanceLog()
        maintenances = [maintenance for maintenance in maintenances if maintenance.maintenanceID != ID] # Remove the maintenance based on ID, (if its the same)
        self.saveMaintenance(maintenances)  # Save updated list to DB

    def removeMaintenanceSchedule(self, ID) -> None:
        """ We take in the ID of the maintenanceSchedule we want to remove, find it, delete it from the internal list and save the internal list to DB """
        maintenanceSchedules = self.loadMaintenanceSchedule()
        maintenanceSchedules = [schedule for schedule in maintenanceSchedules if schedule.maintenanceID != ID] # Remove the maintenanceschedule based on ID, (if its the same)
        self.saveMaintenanceSchedule(maintenanceSchedules)  # Save updated list to DB

    def saveMaintenance(self, maintenances) -> None:
        """ Function saves all instances of the Maintenance class saved in self.maintenance in dictionary form into json Database """
        Maintenances = []
        for maint in maintenances:
            Maintenances.append(maint.Maintenance_Dict())

        with open(self.maintenance_file_path, 'w') as file:
            json.dump(Maintenances, file, indent=4)
            
    def saveMaintenanceSchedule(self, schedule) -> None:
        """ Function saves all instances of the MaintenanceSchedule class saved in self.maintenanceschedule in dictionary form into json Database """
        MaintenanceSchedules = []
        for schedule in schedule:
            MaintenanceSchedules.append(schedule.maintenanceSchedule_Dict())

        with open(self.maintenance_Schedule_file_path, 'w') as file:
            json.dump(MaintenanceSchedules, file, indent=4)