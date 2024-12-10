# Maintenance DB Logic
import os
import json
from Models.Maintenance import Maintenance
from Models.MaintenanceSchedule import MaintenanceSchedule
from Models.MaintenanceReport import MaintenanceReport
from datetime import datetime

class MaintenanceDBLogic:

    def __init__(self):
        """ Holds a reference to all Maintenance related Databases """
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.maintenance_file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "Maintenance.json")
        self.maintenance_Schedule_file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "MaintenanceSchedule.json")
        self.maintenance_Report_file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "MaintenanceReport.json")
        self.datetimeFormat = "%d.%m.%Y.%H:%M"

    def loadMaintenanceLog(self) -> list:
        """ Function loads all saved maintenances from DB and turns back into class instances of Maintenance and returns the entire list """
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
                maint["startDate"] = datetime.strptime(maint["startDate"], self.datetimeFormat)
            if maint["endDate"]:
                maint["endDate"] = datetime.strptime(maint["endDate"], self.datetimeFormat)
            maintenances.append(Maintenance(*maint.values()))
        return maintenances

    def loadMaintenanceScheduleLog(self) -> list:
        """ Function loads all saved maintenance schedules from DB and turns back into class instances of Maintenance Schedules and returns the entire list """
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
            if schedule["startDate"]: # need to convert back into datetime format
                schedule["startDate"] = datetime.strptime(schedule["startDate"], self.datetimeFormat)

            maintenanceSchedules.append(MaintenanceSchedule(*schedule.values()))
        return maintenanceSchedules

    def loadMaintenanceReportLog(self) -> list:
        """ Function loads all saved maintenance reports from DB and turns back into class instances of Maintenance Report and returns the entire list """
        maintenanceReport_list = []
        try:
            with open(self.maintenance_Report_file_path, "r") as maintenanceReportDBopen:
                maintenanceReport_list = json.load(maintenanceReportDBopen)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        maintenanceReports = []
        for report in maintenanceReport_list:
            maintenanceReports.append(MaintenanceReport(*report.values()))
        return maintenanceReports

    def updateMaintenance(self, maintenanceTask) -> None:
        """ This function takes in a maintenance instance, finds old version of it by checking the ID, overwrites it and saves the maintenance again in the json DB"""
        maintenances = self.loadMaintenanceLog()
        for index, maint in enumerate(maintenances):
            if maint.maintenanceID == maintenanceTask.maintenanceID:
                maintenances[index] = maintenanceTask
        self.saveMaintenance(maintenances)

    def updateMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ This function takes in a maintenanceSchedule instance, finds old version of it by checking the ID, overwrites it and saves the maintenanceSchedule again in the json DB"""
        maintenanceSchedules = self.loadMaintenanceScheduleLog()
        for index, schedule in enumerate(maintenanceSchedules):
            if schedule.maintenanceScheduleID == maintenanceSchedule.maintenanceScheduleID:
                maintenanceSchedules[index] = maintenanceSchedule
        self.saveMaintenanceSchedule(maintenanceSchedules)

    def updateMaintenanceReport(self, maintenanceReport) -> None:
        """ This function takes in a maintenanceReport instance, finds old version of it by checking the ID, overwrites it and saves the maintenanceReports again in the json DB"""
        maintenanceReports = self.loadMaintenanceReportLog()
        for index, report in enumerate(maintenanceReports):
            if report.maintenanceReportID == maintenanceReport.maintenanceReportID:
                maintenanceReports[index] = maintenanceReport
        self.saveMaintenanceReport(maintenanceReports)

    def createMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ This function takes in an instance of maintenanceSchedule, adds it to the current database list and stores in the json DB """
        maintenanceSchedules = self.loadMaintenanceScheduleLog()
        maintenanceSchedules.append(maintenanceSchedule)
        self.saveMaintenanceSchedule(maintenanceSchedules)

    def createMaintenance(self, maintenance) -> None:
        """ This function takes in an instance of maintenance, adds it to the current database list and stores in the json DB """
        maintenances = self.loadMaintenanceLog()
        maintenances.append(maintenance)
        self.saveMaintenance(maintenances)

    def createMaintenanceReport(self, maintenanceReport) -> None:
        """ This function takes in a completed instance of a maintenance Report, adds it to the existant maintenance Reports and saves it in the database"""

        maintenanceReports = self.loadMaintenanceReportLog()
        maintenanceReports.append(maintenanceReport)
        self.saveMaintenanceReport(maintenanceReports)

    def saveMaintenance(self, maintenances) -> None:
        """ Function saves all instances of the Maintenance class received in the maintenances parameter in dictionary form into json Database """
        Maintenances = []
        for maint in maintenances:
            # We cant store the datetime so we will convert the datetime into string when saving and convert it back when loading in
            if maint.startDate:
                maint.startDate = maint.startDate.strftime(self.datetimeFormat)
            if maint.endDate:
                maint.endDate = maint.endDate.strftime(self.datetimeFormat)
            Maintenances.append(maint.Maintenance_Dict())

        with open(self.maintenance_file_path, "w") as file:
            json.dump(Maintenances, file, indent=4)
            
    def saveMaintenanceSchedule(self, schedules) -> None:
        """ Function saves all instances of the MaintenanceSchedule class received in the schedules paramater in dictionary form into json Database """
        MaintenanceSchedules = []
        for schedule in schedules:
            # We cant store the datetime so we will convert the datetime into string when saving and convert it back when loading in
            if schedule.startDate:
                schedule.startDate = schedule.startDate.strftime(self.datetimeFormat)

            MaintenanceSchedules.append(schedule.MaintenanceSchedule_Dict())

        with open(self.maintenance_Schedule_file_path, "w") as file:
            json.dump(MaintenanceSchedules, file, indent=4)

    def saveMaintenanceReport(self, maintenanceReports) -> None:
        """ Function saves all instances of the MaintenanceReport class saved in the maintenanceReports list it received into the json Database """
        saveMaintenanceReports = []
        for report in maintenanceReports:
            saveMaintenanceReports.append(report.MaintenanceReport_Dict())
        
        with open(self.maintenance_Report_file_path, "w") as file:
            json.dump(saveMaintenanceReports, file, indent=4)