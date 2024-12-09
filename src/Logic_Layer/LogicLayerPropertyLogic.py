from Data_Layer.DataLayerAPI import DataLayerAPI
from Models.Workers import *
from Models.Property import Property
from .ErrorCheckers import ErrorCheckers

# Here is our Property Logic class that includes all of our functions

class LogicLayerPropertyLogic:

    def __init__(self):
        self.DataLayerWrapper = DataLayerAPI()
        self.Errors = ErrorCheckers()

    def createUniqueID(self)-> int:
    # Here we create a new unique ID for a Property
        currentProperty = self.DataLayerWrapper.loadPropertiesLog()
        if len(currentProperty) != 0:
            newID = currentProperty[-1].propertyID + 1 # Assign new property to a new ID
        else:
            newID = 1
        return newID
    
    def createTempProperty(self):
        tempPropertyID = self.createUniqueID()
        temp_property = Property(ID=tempPropertyID)
        return temp_property
    
    def validatePropertyInput(self, input, count, temp_property):
        if self.Errors.checkNumber(count):
            count = int(count)

        if count == 1:  # Name Of Property
            self.Errors.errorCheckName(input)
            temp_property.nameOfProperty = input
        elif count == 2:  # Location of property
            self.Errors.errorCheckLocation(input)
            temp_property.location = input
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

    def getPropertyByID(self, ID):
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
            
    def getTasksForPropertyID(self, ID):
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
    def updateProperty(self, property):
        # updateProperty = self.updateStatusOfProperty.
        self.DataLayerWrapper.updateProperty(property)

    #get properties data
    def getPropertiesData(self):
        getProperty = self.DataLayerWrapper.loadPropertiesLog()
        return getProperty

    # Create a property
    def createProperty(self, tempProperty):
        self.DataLayerWrapper.createProperty(tempProperty)
