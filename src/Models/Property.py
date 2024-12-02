# Defining Property classes

class Property:
    def __init__(self, nameOfProperty, location, availability, hasAPool, hasATub, hasOvens,) -> None:
        """Defines variables for our properties"""
        self.propertyID = 1 # ID calculate
        self.nameOfProperty = nameOfProperty
        self.location = location
        self.availability = availability
        self.hasAPool = hasAPool
        self.hasATub = hasATub
        self.hasOvens = hasOvens 

    def Property_dict(self) -> dict:
        """ Returns all the variables in our Property class into a dictionary"""
        return {
        "propertyID": self.propertyID,
        "nameOfProperty": self,
        "location": self.location,
        "availability": self.availability,
        "hasAPool": self.hasAPool,
        "hasATub": self.hasATub,
        "hasOvens": self.hasOvens          
        }

