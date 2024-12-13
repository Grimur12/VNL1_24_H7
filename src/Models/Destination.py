#defining the classes of Destination

# Destinations we have are from iceland :
    # - Nuuk, Greenland
    # - Kulusuk, Greenland
    # - Thorshofn, Faroe Islands
    # - Tingwall, Shetland Islands
    # - LongYearByen, Svalbard

# We are also counting iceland as a destination so 6 in total
class Destination:
    def __init__(self, ID, name, country, timezone, airportName, phoneNumber, openingHours, managerOfDestination):
        """ Defines variables for Destination """
        self.destinationID = ID # Unique ID
        self.name = name # Name of the Destination
        self.country = country # Country of Destination
        self.timezone = timezone # Timezone the Destination is in
        self.airportName = airportName # Airport of the Destination
        self.phoneNumber = phoneNumber # Phone number of the Airport
        self.openingHours = openingHours # Opening hours 24/7 most likely (Its an Airport)
        self.managerOfDestination = managerOfDestination # Reference to an employee ID that is a manager

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
    
