import os
import json
from Models.Destination import Destination

class DestinationDBLogic:
    def __init__(self) -> None:
        """ Holds reference to the Destination DB """
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "Destination.json")

    def loadDestinationsLog(self) -> list[Destination]:
        """ Loads all properties from json database, creates the classes again, stores in a list to return"""
        destination_list = []
        try:
            with open(self.file_path, "r") as destinationDBOpen:
                destination_list = json.load(destinationDBOpen)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        destination = []
        for dest in destination_list:
            destination.append(Destination(*dest.values()))
        return destination

    def updateDestination(self, updated_destination) -> None:
        """ This function takes in a Destination instance, finds old version of it by checking the ID, overwrites it and saves the Destinations again in the json DB"""
        destinations = self.loadDestinationsLog()
        for index, dest in enumerate(destinations):
            if dest.destinationID == updated_destination.destinationID:
                destinations[index] = updated_destination
        self.saveDestinations(destinations)

    def saveDestinations(self, destinations) -> None:
        """ Function saves all instances of the Destination class received in the properties paramater in dictionary form into json Database """
        Destinations = []
        for dest in destinations:
            Destinations.append(dest.Destination_Dict())

        with open(self.file_path, "w") as file:
            json.dump(Destinations, file, indent=4)