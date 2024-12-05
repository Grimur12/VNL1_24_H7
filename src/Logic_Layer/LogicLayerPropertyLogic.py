from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Workers import *
from Models.Property import Property
from .ErrorCheckers import ErrorCheckers

# Property Logic class

class LogicLayerPropertyLogic:

    def __init__(self):
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()
        self.temp_property = None

    def createUniqueID(self)-> int:
        currentProperty = self.DataLayerWrapper.loadPropertyLog()
        if len(currentProperty) != 0:
            newID = currentProperty[-1].propertyID + 1 # Assign new property to a new ID
        else:
            newID = 1
        return newID
    
    def createTempProperty(self):
        tempPropertyID = self.createUniqueID()
        self.temp_property = Property(ID=tempPropertyID)
        return self.temp_property

    def updateStatusOfProperty(self):
        pass






    def filterProperties(self):
        pass

    def getPropertiesData(self):
        pass

    #check errors
    def checkPropertiesError():
        pass
