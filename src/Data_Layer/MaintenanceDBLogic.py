# Maintenance DB Logic
import os
import json
from Models.Maintenance import Maintenance
from Models.MaintenanceSchedule import MaintenanceSchedule
from Models.MaintenanceReport import MaintenanceReport
from datetime import datetime

class MaintenanceDBLogic:

    def __init__(self) -> None:
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
                maintenance_list = json.load(maintenanceDBOpen) # Load all Maintenances from the DB
        except FileNotFoundError: # Unless file is not found, we return an empty list anyways (basically assumes that the DB dosent exist so an empty list would make sense here)
            return []
        except json.JSONDecodeError: # And unless no Maintenances in the DB (or corrupt) so we return an empty list, because the DB is empty
            return []
        
        maintenances = []
        for maint in maintenance_list:
            # We had to convert the datetime into string to save it, so now we need to convert that string back into datetime when loading in
            if maint["startDate"]:
                maint["startDate"] = datetime.strptime(maint["startDate"], self.datetimeFormat)
            if maint["endDate"]:
                maint["endDate"] = datetime.strptime(maint["endDate"], self.datetimeFormat)
            maintenances.append(Maintenance(*maint.values())) # Turn the maintenance dictionaries we loaded into the class object Maintenance and append to the list we return
        return maintenances

    def loadMaintenanceScheduleLog(self) -> list:
        """ Function loads all saved maintenance schedules from DB and turns back into class instances of Maintenance Schedules and returns the entire list """
        maintenanceSchedule_list = []
        try:
            with open(self.maintenance_Schedule_file_path, "r") as maintenanceScheduleDBOpen:
                maintenanceSchedule_list = json.load(maintenanceScheduleDBOpen) # Load all MaintenanceSchedules from the DB
        except FileNotFoundError:  # Unless file is not found, we return an empty list anyways (basically assumes that the DB dosent exist so an empty list would make sense here)
            return []
        except json.JSONDecodeError: # And unless no MaintenanceSchedules in the DB (or corrupt) so we return an empty list, because the DB is empty
            return []
        
        maintenanceSchedules = []
        for schedule in maintenanceSchedule_list:
            if schedule["startDate"]: # need to convert the date back into datetime format since we saved it in string form
                schedule["startDate"] = datetime.strptime(schedule["startDate"], self.datetimeFormat)

            maintenanceSchedules.append(MaintenanceSchedule(*schedule.values())) # Turn the dictionaries into Maintenance Schedule class object and add to the list we return
        return maintenanceSchedules

    def loadMaintenanceReportLog(self) -> list:
        """ Function loads all saved maintenance reports from DB and turns back into class instances of Maintenance Report and returns the entire list """
        maintenanceReport_list = []
        try:
            with open(self.maintenance_Report_file_path, "r") as maintenanceReportDBopen:
                maintenanceReport_list = json.load(maintenanceReportDBopen) # Load all maintenance reports in dict form..
        except FileNotFoundError: # Unless file not found we assume it dosent exist so we return an empty list
            return []
        except json.JSONDecodeError: # And unless there is not data or corrupt so we return no empty list
            return []

        maintenanceReports = []
        for report in maintenanceReport_list:
            maintenanceReports.append(MaintenanceReport(*report.values())) # Turn the dictionaries into Maintenance Report class, append to list to return
        return maintenanceReports

    def updateMaintenance(self, maintenanceTask) -> None:
        """ This function takes in a maintenance instance, finds old version of it by checking the ID, overwrites it and saves the maintenance again in the json DB"""
        maintenances = self.loadMaintenanceLog() # Load all the maintenances from DB
        for index, maint in enumerate(maintenances):
            if maint.maintenanceID == maintenanceTask.maintenanceID: # Find the maintenance we are going to update
                maintenances[index] = maintenanceTask # overwrite the current one with the new one
        self.saveMaintenance(maintenances) # Save the list of maintenance into the DB

    def updateMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ This function takes in a maintenanceSchedule instance, finds old version of it by checking the ID, overwrites it and saves the maintenanceSchedule again in the json DB"""
        maintenanceSchedules = self.loadMaintenanceScheduleLog() # Load all the Maintenance Schedules from DB
        for index, schedule in enumerate(maintenanceSchedules):
            if schedule.maintenanceScheduleID == maintenanceSchedule.maintenanceScheduleID: # Find the Maintenance Schedule we are going to update
                maintenanceSchedules[index] = maintenanceSchedule # overwrite the current one with the new one
        self.saveMaintenanceSchedule(maintenanceSchedules) # Save the list of maintenance into the DB

    def updateMaintenanceReport(self, maintenanceReport) -> None:
        """ This function takes in a maintenanceReport instance, finds old version of it by checking the ID, overwrites it and saves the maintenanceReports again in the json DB"""
        maintenanceReports = self.loadMaintenanceReportLog() # Load all the Maintenance Reports from DB
        for index, report in enumerate(maintenanceReports):
            if report.maintenanceReportID == maintenanceReport.maintenanceReportID: # Find the maintenance report we are going to update
                maintenanceReports[index] = maintenanceReport # Overwrite the current one with the new one
        self.saveMaintenanceReport(maintenanceReports) # Save the list of maintenance reports to the DB

    def createMaintenanceSchedule(self, maintenanceSchedule) -> None:
        """ This function takes in an instance of maintenanceSchedule, adds it to the current database list and stores in the json DB """
        maintenanceSchedules = self.loadMaintenanceScheduleLog() # Load all the maintenance schedules from DB
        maintenanceSchedules.append(maintenanceSchedule)  # Add the new maintenance schedule to the mainteance schedule list
        self.saveMaintenanceSchedule(maintenanceSchedules) # Save the maintenance schedules back into the DB with the new one

    def createMaintenance(self, maintenance) -> None:
        """ This function takes in an instance of maintenance, adds it to the current database list and stores in the json DB """
        maintenances = self.loadMaintenanceLog() # Load all the maintenances from DB
        maintenances.append(maintenance) # Add the new Maintenance to the list of Maintenances
        self.saveMaintenance(maintenances) # Save the updated (the new one added) list of maintenances to the DB

    def createMaintenanceReport(self, maintenanceReport) -> None:
        """ This function takes in a completed instance of a maintenance Report, adds it to the existant maintenance Reports and saves it in the database"""
        maintenanceReports = self.loadMaintenanceReportLog() # Load all the Maintenance Reports from DB
        maintenanceReports.append(maintenanceReport) # Add the new Maintenance Reports to the list of Maintenance Reports
        self.saveMaintenanceReport(maintenanceReports) # Save the Maintenance Reports back into the DB with the new one added

    def saveMaintenance(self, maintenances) -> None:
        """ Function saves all instances of the Maintenance class received in the maintenances parameter in dictionary form into json Database """
        Maintenances = []
        for maint in maintenances:
            # We cant store the datetime so we will convert the datetime into string when saving and convert it back when loading in
            if maint.startDate:
                maint.startDate = maint.startDate.strftime(self.datetimeFormat) # Start Date into string
            if maint.endDate:
                maint.endDate = maint.endDate.strftime(self.datetimeFormat) # End Date into string
            Maintenances.append(maint.Maintenance_Dict()) # Put the maintenances into dict form

        with open(self.maintenance_file_path, "w") as file:
            json.dump(Maintenances, file, indent=4) # Save them in dictionary form into the DB
            
    def saveMaintenanceSchedule(self, schedules) -> None:
        """ Function saves all instances of the MaintenanceSchedule class received in the schedules paramater in dictionary form into json Database """
        MaintenanceSchedules = []
        for schedule in schedules:
            # We cant store the datetime so we will convert the datetime into string when saving and convert it back when loading in
            if schedule.startDate:
                schedule.startDate = schedule.startDate.strftime(self.datetimeFormat) # Start date into string

            MaintenanceSchedules.append(schedule.MaintenanceSchedule_Dict()) # Put the schedules into dict form

        with open(self.maintenance_Schedule_file_path, "w") as file:
            json.dump(MaintenanceSchedules, file, indent=4) # Save all the schedules in dict form into the DB

    def saveMaintenanceReport(self, maintenanceReports) -> None:
        """ Function saves all instances of the MaintenanceReport class saved in the maintenanceReports list it received into the json Database """
        saveMaintenanceReports = []
        for report in maintenanceReports:
            saveMaintenanceReports.append(report.MaintenanceReport_Dict()) # Put all the Reports into dict form
        
        with open(self.maintenance_Report_file_path, "w") as file:
            json.dump(saveMaintenanceReports, file, indent=4) # Save all the Reports in dict form into the DB