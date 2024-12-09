#defining the classes of Destination

# Destinations we have are from iceland :
    # - Nuuk, Greenland
    # - Kulusuk, Greenland
    # - Thorshofn, Faroe Islands
    # - Tingwall, Shetland Islands
    # - LongYearByen, Svalbard


class Destination:
    def __init__(self, ID, name, country, timezone, airportName, phoneNumber, openingHours, managerOfDestination,):
        """ Defines variables for Destination """
        self.destinationID = ID
        self.name = name
        self.country = country
        self.timezone = timezone
        self.airportName = airportName
        self.phoneNumber = phoneNumber
        self.openingHours = openingHours
        self.managerOfDestination = managerOfDestination

    def Destination_Dict(self) -> dict:
        """ Returns all the variables in our Destination class into a dictionary """
        return {
        "destinationID": self.destinationID,    
        "name": self.name,
        "country": self.country,
        "timezone": self.timezone,
        "airportName": self.airportName,
        "phone number": self.phoneNumber,
        "openingHours": self.openingHours,
        "managerOfDestination": self.managerOfDestination
        }
    
