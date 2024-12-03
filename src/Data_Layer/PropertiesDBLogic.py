# Properties DB Logic
import os
import json
from Models.Property import Property

class PropertiesDBLogic:
    def __init__(self) -> None:
        self.properties = []
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_path = os.path.join(self.base_dir, "Data_Layer/Databases", "Properties.json")

    def loadPropertiesLog(self) -> None:
        """ Function loads all saved properties from DB and turns back into class instances of Property and saves it internally """
        with open(self.file_path, "r") as propertyDBOpen:
            property_list = json.load(propertyDBOpen)
        for property in property_list:
            self.properties.append(Property(*property.values()))

    def createProperty(self, params) -> None:
        """ This function takes in a list of parameters and creates a property and stores in the json DB """
        self.properties.append(Property(*params))

    def removeProperty(self, ID) -> None:
        """ We take in the ID of the property we want to remove, find it, delete it from the internal list and save the internal list to DB """
        index_to_remove = -1
        for index, property in enumerate(self.property):
            if property.employeeID == ID:
                index_to_remove = index
                break
        # Remove that property from the internal list
        if index_to_remove != -1:
            del self.properties[index_to_remove]
        # Save the modified internal list to the DB
        self.saveProperties()
    
    def updateProperty(self, params) -> None:
        """ This function takes in a list of parameters, some may be new some may still be the older ones and stores them in the json DB """
        for index, property in enumerate(self.properties):
            if property.propertyID == params[0]:
                self.properties[index] = Property(*params)
        self.saveProperties()

    def saveProperties(self) -> None:
        """ Function saves all instances of the Property class saved in self.properties in dictionary form into json Database """
        Property = [property.Property_dict for property in self.properties]

        with open(self.file_path, 'w') as file:
            json.dump(Property, file, indent=4)
    
    def propagateData(self) -> list:
        """ Returns the internally stored employees list for other layers/classes to use """
        return self.properties

    def printProperties(self) -> None:
        for property in self.properties:
            print("-------------------------------------------------------------------------------------------------------------")
            for key, value in property.__dict__.items():
                print(f"{key}: {value}")