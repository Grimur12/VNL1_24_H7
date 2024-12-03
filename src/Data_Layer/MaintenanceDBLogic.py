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

    def updateMaintenanceStatus(self, params) -> None:
        """ This function takes in a list of parameters, some may be new some may still be the older ones and stores them in the json DB """
        for index, maint in enumerate(self.maintenance):
            if maint.maintenanceID == params[0]:
                self.maintenance[index] = Maintenance(*params)
        self.saveMaintenance()

    def updateMaintenanceSchedule(self, params) -> None:
        """ This function takes in a list of parameters, some may be new some may still be the older ones and stores them in the json DB """
        for index, schedule in enumerate(self.maintenanceSchedule):
            if schedule.maintenanceScheduleID == params[0]:
                self.maintenanceSchedule[index] = MaintenanceSchedule(*params)
        self.saveMaintenanceSchedule()

    def createMaintenanceSchedule(self, params) -> None:
        """ This function takes in a list of parameters and creates a maintenanceSchedule and stores in the json DB """
        self.maintenanceSchedule.append(MaintenanceSchedule(*params))
        self.saveMaintenanceSchedule()

    def createMaintenance(self, params) -> None:
        """ This function takes in a list of parameters and creates a maintenance and stores in the json DB """
        self.maintenance.append(Maintenance(*params))
        self.saveMaintenance()

    def removeMaintenance(self, ID) -> None:
        """ We take in the ID of the maintenance we want to remove, find it, delete it from the internal list and save the internal list to DB """
        index_to_remove = -1
        for index, maint in enumerate(self.maintenance):
            if maint.maintenanceID == ID:
                index_to_remove = index
                break
        # Remove that maintenance from the internal list
        if index_to_remove != -1:
            del self.maintenance[index_to_remove]
            # Save the modified internal list to the DB
            self.saveMaintenance()

        def removeMaintenanceSchedule(self, ID) -> None:
        """ We take in the ID of the maintenanceSchedule we want to remove, find it, delete it from the internal list and save the internal list to DB """
        index_to_remove = -1
        for index, schedule in enumerate(self.maintenanceSchedule):
            if schedule.maintenanceScheduleID == ID:
                index_to_remove = index
                break
        # Remove that maintenanceSchedule from the internal list
        if index_to_remove != -1:
            del self.maintenanceSchedule[index_to_remove]
            # Save the modified internal list to the DB
            self.saveMaintenanceSchedule()

    def saveMaintenance(self) -> None:
        """ Function saves all instances of the Maintenance class saved in self.maintenance in dictionary form into json Database """
        Maintenances = []
        for maint in self.maintenance:
            Maintenances.append(maint.Maintenance_Dict()

        with open(self.maintenance_file_path, 'w') as file:
            json.dump(Maintenances, file, indent=4)
            
    def saveMaintenanceSchedule(self) -> None:
        """ Function saves all instances of the MaintenanceSchedule class saved in self.maintenanceschedule in dictionary form into json Database """
        MaintenanceSchedules = []
        for schedule in self.maintenanceSchedule:
            MaintenanceSchedules.append(schedule.maintenanceSchedule_Dict()

        with open(self.maintenance_Schedule_file_path, 'w') as file:
            json.dump(MaintenanceSchedules, file, indent=4)

    def propagateMaintenanceData(self) -> list:
        """ Returns the internally stored Maintenance list for other layers/classes to use """
        return self.maintenance

    def propagateMaintenanceScheduleData(self) -> list:
        """ Returns the internally stored MaintenanceSchedule list for other layers/classes to use """
        return self.maintenanceSchedule
