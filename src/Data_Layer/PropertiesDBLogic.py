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
                property_list = json.load(propertyDBOpen) # Load all the properties from DB in dict form
        except FileNotFoundError: # Unless file not found we return empty list, assume the DB dosent exist...
            return []
        except json.JSONDecodeError: # Unless DB is empty or corrupt we return an empty list
            return []

        properties = []
        for prop in property_list:
            properties.append(Property(*prop.values())) # Put the properties into Property class and append to the list we return
        return properties

    def createProperty(self, property) -> None:
        """ This function takes in an instance of a property and stores in the json DB """
        properties = self.loadPropertiesLog() # Load all properties from DB in class form
        properties.append(property) # Add the new Property to the list
        self.saveProperties(properties) # Save the Properties back into the DB

    def updateProperty(self, updated_property) -> None:
        """ This function takes in a property instance, finds old version of it by checking the ID, overwrites it and saves the properties again in the json DB"""
        properties = self.loadPropertiesLog() # Load all properties from DB in class form
        for index, prop in enumerate(properties):
            if prop.propertyID == updated_property.propertyID: # Find the property we are going to update
                properties[index] = updated_property # Overwrite it in the list of properties
        self.saveProperties(properties) # Save the list of properties into the DB with the updated property

    def saveProperties(self, properties) -> None:
        """ Function saves all instances of the Property class received in the properties paramater in dictionary form into json Database """
        Properties = []
        for prop in properties:
            Properties.append(prop.Property_dict()) # Put the properties into dict form and into a list

        with open(self.file_path, "w") as file:
            json.dump(Properties, file, indent=4) # Save all the properties into the DB in dict form