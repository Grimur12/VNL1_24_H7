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
        # Params 8 is a reference to "type" variable in the classes
        for property in property_list:
            self.properties.append(Property(*property.values()))

    def createProperty() -> None:
        pass

    def removeProperty() -> None:
        pass
    
    def updateProperty() -> None:
        pass

    def saveProperty(self) -> None:
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