# Defining Property classes

class Property:
    def __init__(self, ID, nameOfProperty, location, availability, hasAPool, hasATub, hasOvens,) -> None:
        """Defines variables for our properties"""
        self.propertyID = ID # ID calculate
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
        "nameOfProperty": self.nameOfProperty,
        "location": self.location,
        "availability": self.availability,
        "hasAPool": self.hasAPool,
        "hasATub": self.hasATub,
        "hasOvens": self.hasOvens          
        }
