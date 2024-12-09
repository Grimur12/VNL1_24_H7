from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Workers import *
from Models.Property import Property
from Models.Maintenance import Maintenance
from .ErrorCheckers import ErrorCheckers
# Property Logic class

class LogicLayerPropertyLogic:

    def __init__(self):
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()

    def createUniqueID(self) -> int:
        """ Function loads all Properties from DB, finds the last assigned ID and adds one to it, creating a new ID, returns unique ID int"""
    # Here we create a new unique ID for a Property
        currentProperty = self.DataLayerWrapper.loadPropertiesLog()
        if len(currentProperty) != 0:
            newID = currentProperty[-1].propertyID + 1 # Assign new property to a new ID
        else:
            newID = 1
        return newID
    
    def createTempProperty(self) -> Property:
        """ Function creates a temporary Property for the user to fill out, it is assigned a unique INT ID, returns a temporary Property"""
        tempPropertyID = self.createUniqueID()
        temp_property = Property(ID=tempPropertyID)
        return temp_property
    
    def validatePropertyInput(self, input, count, temp_property) -> True:
        """ Function checks for each attribute in the Property the user changes if it is of the desired format, returns True or raises ValuError"""
        if self.Errors.checkNumber(count):
            count = int(count)

        if count == 1:  # Name Of Property
            self.Errors.errorCheckName(input)
            temp_property.nameOfProperty = input
        elif count == 2:  # Location of property
            self.Errors.checkNumber(input)
            self.checkIfDestinationExists(int(input))
            temp_property.location = int(input)
        elif count == 3:  # Availability of Property
            self.Errors.errorCheckBoolean(input)
            temp_property.availability = input
        elif count == 4:  # HasAPool
            self.Errors.errorCheckBoolean(input)
            temp_property.hasAPool = input
        elif count == 5:  # HasATub
            self.Errors.errorCheckBoolean(input)
            temp_property.hasATub = input
        elif count == 6:  # HasOvens
            self.Errors.errorCheckBoolean(input)
            temp_property.hasOvens = input
        return True

    def getPropertyByID(self, ID) -> Property:
        """ Function loads all Properties and tries to find the specified Property by ID in the DB, returns Property or raises ValueError"""
    # Check for property by property ID or name
        if self.Errors.checkNumber(ID):
            propertyLog = self.DataLayerWrapper.loadPropertiesLog()
            index_to_update = -1
            for index, property in enumerate(propertyLog):
                if property.propertyID == int(ID):
                    index_to_update = index
            if index_to_update != -1:
                property_found = propertyLog[index_to_update]
                return property_found
            else:
                raise ValueError("No Property By that ID")
            
    def checkIfDestinationExists(self, dest_ID) -> True:
        """ Function takes in destination ID, returns True if it finds destination in DB otherwise raises ValueError"""
        destinations = self.DataLayerWrapper.loadDestinationsLog()
        for dest in destinations:
            if dest.destinationID == dest_ID:
                return True
        raise ValueError("No Destination By that ID")
            
    def getTasksForPropertyID(self, ID) -> list[Maintenance]:
        """ Function finds the Property, loads all maintenance tasks and filters out all the maintenance tasks a being done on a property, returns filtered list of maintenance tasks or raises ValuError"""
        # Takes in property ID
        # probably best to call GetPropertyByID
        #MaintenanceTasksLog = self.DataLayerWrapper.loadMaintenanceReportLog()
        # Put logic to add together if property ID == property ID in the report and return that ..
        #return tasks
        property = self.getPropertyByID(ID)
        maintenanceTaskLog = self.DataLayerWrapper.loadMaintenanceLog()
        tasksDoneOnProperty = []
        for task in maintenanceTaskLog:
            if task.propertyID == property.propertyID: # Check all the maintenance tasks we have in DB, to see if they were done on the property that was specified
                tasksDoneOnProperty.append(task)
        
        if len(tasksDoneOnProperty) == 0:
            raise ValueError("No Maintenance has been done on this Property")
        
        return tasksDoneOnProperty
        
    #update the status of properties
    def updateProperty(self, property) -> None:
        """ Function takes in a property already in DB and overwrites it with the new attributes and saves it in Employee DB """
        # updateProperty = self.updateStatusOfProperty.
        self.DataLayerWrapper.updateProperty(property)

    #get properties data
    def getPropertiesData(self) -> None:
        """ Load all the Properties from the DB to return in a list format """
        getProperty = self.DataLayerWrapper.loadPropertiesLog()
        return getProperty

    def createProperty(self, tempProperty) -> None:
        """ Function takes in a completely filled out tempProperty and saves it in our Property DB"""
        self.DataLayerWrapper.createProperty(tempProperty)

    #check errors
    def checkPropertiesError():
        pass
