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
        for prop in property_list:
            self.properties.append(Property(*prop.values()))

    def createProperty(self, params) -> None:
        """ This function takes in a list of parameters and creates a property and stores in the json DB """
        self.properties.append(Property(*params))
        self.saveProperties()

    def removeProperty(self, ID) -> None:
        """ We take in the ID of the property we want to remove, find it, delete it from the internal list and save the internal list to DB """
        index_to_remove = -1
        for index, prop in enumerate(self.properties):
            if prop.propertyID == ID:
                index_to_remove = index
                break
        # Remove that property from the internal list
        if index_to_remove != -1:
            del self.properties[index_to_remove]
            # Save the modified internal list to the DB
            self.saveProperties()
    
    def updateProperty(self, params) -> None:
        """ This function takes in a list of parameters, some may be new some may still be the older ones and stores them in the json DB """
        for index, prop in enumerate(self.properties):
            if prop.propertyID == params[0]:
                self.properties[index] = Property(*params)
        self.saveProperties()

    def saveProperties(self) -> None:
        """ Function saves all instances of the Property class saved in self.properties in dictionary form into json Database """
        Properties = []
        for prop in self.properties:
            Properties.append(prop.Property_dict())

        with open(self.file_path, 'w') as file:
            json.dump(Properties, file, indent=4)
    
    def propagateData(self) -> list:
        """ Returns the internally stored employees list for other layers/classes to use """
        return self.properties

    def printProperties(self) -> None:
        """ Internal, prints out properties, for testing purposes in DB layer """
        for prop in self.properties:
            print("-------------------------------------------------------------------------------------------------------------")
            for key, value in prop.__dict__.items():
                print(f"{key}: {value}")

## Functionality Tests
# ui = PropertiesDBLogic()
# ui.createProperty([1, "Bel-Air Mansion", "Malibu", True, True, True, True])
# ui.createProperty([2, "Mosó Steinda Mansion", "Mosfellsbær", False, True, True, False])
# ui.createProperty([3, "Frenchie villa", "Toulouse", True, True, False, False])
# ui.printProperties()
# ui.loadPropertiesLog()
# ui.printProperties()
# ui.removeProperty(1)
# ui.printProperties()
# ui.createProperty([1, "Bel-Air Mansion", "Malibu", True, True, True, True])
# ui.printProperties()
# ui.updateProperty([1, "Bel-Air Mansion", "Malibu", False, True, True, True])
# ui.printProperties()
