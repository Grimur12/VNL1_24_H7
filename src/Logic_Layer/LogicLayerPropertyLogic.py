# Here is our Property Logic Layer

class LogicLayerPropertyLogic:

    def __init__(self):
        #our list of properties
        self.properties = []

    def create_Property(self, property_Data):

        # for prop in self.properties:
        #     prop["id"] == property_Data["id"]
        #     return False
        #     #add try except or raise whatever!
            
        # self.properties.append(property_Data)
        # return True
        pass

    def updateStatusOfProperty(self, property_ID, new_status):
        
        for property in self.properties:
            if property["id"] == property_ID:
                
                property["status"] = new_status
                return True
            
        #if property wasnt found = return False.
        return False

    def filerProperties(self):
        pass

    def getPropertiesData(self):
        pass




    #check errors
    def checkPropertiesError():
        pass
