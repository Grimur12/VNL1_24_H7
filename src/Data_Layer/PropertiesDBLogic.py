# Properties DB Logic
import os
import json
from Models.Property import Property

class PropertiesDBLogic:
    def __init__(self) -> None:
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "Properties.json")

    def loadPropertiesLog(self) -> list[Property]:
        """ Loads all properties from json database, creates the classes again, stores in a list to return"""
        property_list = []
        try:
            with open(self.file_path, "r") as propertyDBOpen:
                property_list = json.load(propertyDBOpen)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        properties = []
        for prop in property_list:
            properties.append(Property(*prop.values()))
        return properties

    def createProperty(self, property) -> None:
        """ This function takes in an instance of a property and stores in the json DB """
        properties = self.loadPropertiesLog()
        properties.append(property)
        self.saveProperties(properties)

    def updateProperty(self, updated_property) -> None:
        """ This function takes in a property instance, finds old version of it by checking the ID, overwrites it and saves the properties again in the json DB"""
        properties = self.loadPropertiesLog()
        for index, prop in enumerate(properties):
            if prop.propertyID == updated_property.propertyID:
                properties[index] = updated_property
        self.saveProperties(properties)

    def saveProperties(self, properties) -> None:
        """ Function saves all instances of the Property class received in the properties paramater in dictionary form into json Database """
        Properties = []
        for prop in properties:
            Properties.append(prop.Property_dict())

        with open(self.file_path, "w") as file:
            json.dump(Properties, file, indent=4)

    def printProperties(self) -> None:
        """ Internal, prints out properties, for testing purposes in DB layer """
        properties = self.loadPropertiesLog()
        for prop in properties:
            print("-------------------------------------------------------------------------------------------------------------")
            for key, value in prop.__dict__.items():
                print(f"{key}: {value}")
