from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Workers import *
from Models.Property import Property
from Models.Maintenance import Maintenance
from .ErrorCheckers import ErrorCheckers

class LogicLayerPropertyLogic:

    def __init__(self):
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()

    def createUniqueID(self) -> int:
        """ Function loads all Properties from DB, finds the last assigned ID and adds one to it, creating a new ID, returns unique ID int"""
        # Here we create a new unique ID for a Property
        currentProperty = self.DataLayerWrapper.loadPropertiesLog() # Loads all Properties from the DB
        if len(currentProperty) != 0:
            newID = currentProperty[-1].propertyID + 1 # Assign new property to a new ID by finding the last used id and adding 1 to it
        else: # If there are no properties in the DB we start the unique count at 1
            newID = 1
        return newID
    
    def createTempProperty(self) -> Property:
        """ Function creates a temporary Property for the user to fill out, it is assigned a unique INT ID, returns a temporary Property"""
        tempPropertyID = self.createUniqueID() # Get a unique id for the temp employee
        temp_property = Property(ID=tempPropertyID) # create the property class
        return temp_property # return it with an assigned unique ID
    
    def validatePropertyInput(self, input, count, temp_property) -> True:
        """ Function checks for each attribute in the Property the user changes if it is of the desired format, returns True or raises ValuError"""
        if self.Errors.checkNumber(count):
            count = int(count)
        # This function doubles as a validation for creating properties and updating them, when editing properties instead of count we get the number of the attribute the user wants to change, thats why we need to change it into an integer even though count would usually be an integer
        if count == 1:  # Name Of Property
            self.Errors.errorCheckName(input)
            temp_property.nameOfProperty = input
        elif count == 2:  # Location of property
            self.Errors.checkNumber(input) # Check if its a number
            self.checkIfDestinationExists(int(input)) # Check if the destination exists in our DB
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

    def getPropertyByID(self, ID, destination = None) -> Property:
        """ Function loads all Properties and tries to find the specified Property by ID in the DB, can filter by destination if specified, returns Property or raises ValueError"""
        # Check for property by property ID
        if self.Errors.checkNumber(ID): # Check if its a number
            destination_filter = False
            propertyLog = self.DataLayerWrapper.loadPropertiesLog() # Loads all properties from DB
            index_to_update = -1 # start index value if we never found the property

            if destination is not None:
                destination_filter = True # This means we are applying the destination filter

            for index, property in enumerate(propertyLog):
                if destination_filter: 

                    if property.propertyID == int(ID) and property.location == destination.destinationID:
                        index_to_update = index # We found the property by id in the DB and its at the specified destination so we update the index of it
                        break
                else:
                    if property.propertyID == int(ID):
                        index_to_update = index # We found the propert by id
                        break

            if index_to_update != -1:
                property_found = propertyLog[index_to_update] # Extract the property from the DB list by index
                return property_found
            else: # Means we never found the property so raise the error
                raise ValueError("No Property By that ID")


    def checkIfDestinationExists(self, dest_ID) -> True:
        """ Function takes in destination ID, returns True if it finds destination in DB otherwise raises ValueError"""
        destinations = self.DataLayerWrapper.loadDestinationsLog() # Loads all destinations
        for dest in destinations: 
            if dest.destinationID == dest_ID: # Check if we have that destination in our DB by ID
                return True
        raise ValueError("No Destination By that ID")
            
    def getTasksForPropertyID(self, ID, destination = None) -> list[Maintenance]:
        """ Function finds the Property, loads all maintenance tasks and filters out all the maintenance tasks a being done on a property, returns filtered list of maintenance tasks or raises ValuError"""
        # Takes in property ID
        # Put logic to add together if property ID == property ID in the report and return that
        # In addition to this if we get passed a destination, the getemployeebyid function will filter on destination which means that this function does that aswell essentially
        property = self.getPropertyByID(ID, destination) # We get the property either with destination specified, if no property by that ID at that location it will raise a ValueError, otherwise it keeps going, if there was no destination specified it ignores it 
        maintenanceTaskLog = self.DataLayerWrapper.loadMaintenanceLog() # load all maintenances
        tasksDoneOnProperty = []
        for task in maintenanceTaskLog:
            if task.propertyID == property.propertyID: # Check all the maintenance tasks we have in DB, to see if they were done on the property that was specified
                tasksDoneOnProperty.append(task)
        
        if len(tasksDoneOnProperty) == 0: # If we found no tasks on that property the list will be empty so raise the error
            raise ValueError("No Maintenance has been done on this Property")
        
        return tasksDoneOnProperty
        
    #update the status of properties
    def updateProperty(self, property) -> None:
        """ Function takes in a property already in DB and overwrites it with the new attributes and saves it in Employee DB """
        self.DataLayerWrapper.updateProperty(property) # Update the property in the db

    #get properties data
    def getPropertiesData(self, destination = None) -> list[Property]:
        """ Load all the Properties from the DB to return in a list format """
        getProperty = self.DataLayerWrapper.loadPropertiesLog() # Load all properties
        if destination is not None: # If we are filtering on destination aswell
            getProperty = [prop for prop in getProperty if prop.location == destination.destinationID] # We filter the list of properties from the DB to only the ones that have a location at the destination ID
        return getProperty

    def createProperty(self, tempProperty) -> None:
        """ Function takes in a completely filled out tempProperty and saves it in our Property DB"""
        self.DataLayerWrapper.createProperty(tempProperty) # Create the finalized temp property
