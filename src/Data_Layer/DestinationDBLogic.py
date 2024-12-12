import os
import json
from Models.Destination import Destination

class DestinationDBLogic:
    def __init__(self) -> None:
        """ Holds reference to the Destination DB """
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "Destination.json")
        # The destination DB is an artificial one
        # The system depends on this destination DB, if deleted the system will not work since no features were implemented or meant to be implemented for it. It just assumes that there is a destination DB
    def loadDestinationsLog(self) -> list[Destination]:
        """ Loads all properties from json database, creates the classes again, stores in a list to return"""
        destination_list = [] # Start off with an empty list
        try:
            with open(self.file_path, "r") as destinationDBOpen:
                destination_list = json.load(destinationDBOpen) # Load all destinations from the DB
        except FileNotFoundError: # Unless file is not found, we return an empty list anyways (basically assumes that the DB dosent exist so an empty list would make sense here)
            return []
        except json.JSONDecodeError: # And unless no destinations in the DB (or corrupt) so we return an empty list, because the DB is empty
            return []
        # We loaded in all of the destinations but they are dictionaries since we store them as such
        destination = [] 
        for dest in destination_list:
            destination.append(Destination(*dest.values())) # change all the dictionaries that were loaded from the DB into the class object Destination and add to the list we return
        return destination

    def updateDestination(self, updated_destination) -> None:
        """ This function takes in a Destination instance, finds old version of it by checking the ID, overwrites it and saves the Destinations again in the json DB"""
        destinations = self.loadDestinationsLog() # Load all destinations from DB
        for index, dest in enumerate(destinations): # go through the list of destinations
            if dest.destinationID == updated_destination.destinationID: # Find the destination we are updating in the DB
                destinations[index] = updated_destination # And overwrite it 
        self.saveDestinations(destinations) # Then save the destinations again

    def saveDestinations(self, destinations) -> None:
        """ Function saves all instances of the Destination class received in the properties paramater in dictionary form into json Database """
        Destinations = []
        for dest in destinations:
            Destinations.append(dest.Destination_Dict()) # Turn all of the destinations we receive into dictionary form

        with open(self.file_path, "w") as file: # Write all the dictionary Destinations into the DB
            json.dump(Destinations, file, indent=4)