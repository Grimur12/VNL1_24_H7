# Maintenance DB Logic
import os
import json
from Models.Maintenance import Maintenance
from Models.MaintenanceSchedule import MaintenanceSchedule
from datetime import datetime

DATETIME_FORMAT = "%d.%m.%Y.%H:%M"

class MaintenanceDBLogic:

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.maintenance_file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "Maintenance.json")
        self.maintenance_Schedule_file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "MaintenanceSchedule.json")

    def loadMaintenanceLog(self) -> list:
        """ Function loads all saved maintenances from DB and turns back into class instances of Maintenance and saves it internally """
        maintenance_list = []
        try:
            with open(self.maintenance_file_path, "r") as maintenanceDBOpen:
                maintenance_list = json.load(maintenanceDBOpen)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        
        maintenances = []
        for maint in maintenance_list:
            # We had to convert the datetime into string to save it, so now we need to convert that string back into datetime when loading in
            if maint["startDate"]:
                maint["startDate"] = datetime.strptime(maint["startDate"], DATETIME_FORMAT)
            if maint["endDate"]:
                maint["endDate"] = datetime.strptime(maint["endDate"], DATETIME_FORMAT)
            maintenances.append(Maintenance(*maint.values()))
        return maintenances

    def loadMaintenanceScheduleLog(self) -> list:
        maintenanceSchedule_list = []
        try:
            with open(self.maintenance_Schedule_file_path, "r") as maintenanceScheduleDBOpen:
                maintenanceSchedule_list = json.load(maintenanceScheduleDBOpen)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        
        maintenanceSchedules = []
        for schedule in maintenanceSchedule_list:
            maintenanceSchedules.append(MaintenanceSchedule(*schedule.values()))
        return maintenanceSchedules

    def updateMaintenanceStatus(self, maintenanceTask) -> None:
        """ This function takes in a list of parameters, some may be new some may still be the older ones and stores them in the json DB """
        maintenances = self.loadMaintenanceLog()
        for index, maint in enumerate(maintenances):
            if maint.maintenanceID == maintenanceTask.maintenanceID:
                maintenances[index] = maintenanceTask
        self.saveMaintenance(maintenances)

    def updateMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ This function takes in a list of parameters, some may be new some may still be the older ones and stores them in the json DB """
        maintenanceSchedules = self.loadMaintenanceScheduleLog()
        for index, schedule in enumerate(maintenanceSchedules):
            if schedule.maintenanceScheduleID == maintenanceSchedule.maintenanceScheduleID:
                maintenanceSchedules[index] = maintenanceSchedule
        self.saveMaintenanceSchedule(maintenanceSchedules)

    def createMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ This function takes in a list of parameters and creates a maintenanceSchedule and stores in the json DB """
        maintenanceSchedules = self.loadMaintenanceScheduleLog()
        maintenanceSchedules.append(maintenanceSchedule)
        self.saveMaintenanceSchedule(maintenanceSchedules)

    def createMaintenance(self, maintenance) -> None:
        """ This function takes in a list of parameters and creates a maintenance and stores in the json DB """
        maintenances = self.loadMaintenanceLog()
        maintenances.append(maintenance)
        self.saveMaintenance(maintenances)

    def saveMaintenance(self, maintenances) -> None:
        """ Function saves all instances of the Maintenance class saved in self.maintenance in dictionary form into json Database """
        Maintenances = []
        for maint in maintenances:
            # We cant store the datetime so we will convert the datetime into string when saving and convert it back when loading in
            maint_dict = maint.Maintenance_Dict()
            if maint.startDate:
                maint.startDate = maint.startDate.strftime(DATETIME_FORMAT)
            if maint.endDate:
                maint.endDate = maint.endDate.strftime(DATETIME_FORMAT)
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