# Defining Property classes

class Property:
    def __init__(self, ID, nameOfProperty = "", description = "", location = "", availability = "", hasAPool = "", hasATub = "", hasOvens = "") -> None:
        """Defines variables for our properties"""
        ## Add a "Fasteignanumer" / property id for users to input
        ## Add a extra information field, optional, to type something in
        self.propertyID = ID # Unique ID of the property
        self.nameOfProperty = nameOfProperty # Name of the property
        self.description = description # Description of the property
        self.location = location # Reference to Destination ID
        self.availability = availability # If its available for rent
        self.hasAPool = hasAPool # Does it have a Pool
        self.hasATub = hasATub # Does it have a tub
        self.hasOvens = hasOvens # Does it have Ovens

    def Property_dict(self) -> dict:
        """ Returns all the variables in our Property class into a dictionary"""
        return {
        "propertyID": self.propertyID,
        "nameOfProperty": self.nameOfProperty,
        "description": self.description,
        "location": self.location,  
        "availability": self.availability,
        "hasAPool": self.hasAPool,
        "hasATub": self.hasATub,
        "hasOvens": self.hasOvens          
        }
