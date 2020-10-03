
def calculateGasTripCost(milesToDrive, milesPerGallon, dollarsPerGallon):
    gallonsUsed = milesToDrive / milesPerGallon
    tripCost = gallonsUsed * dollarsPerGallon
    return tripCost

def calculateElectricTripCost(milesToDrive, milesPerKWh, dollarsPerKWh):
    kWhUsed = milesToDrive / milesPerKWh
    tripCost = kWhUsed * dollarsPerKWh
    return tripCost

def displayBanner():
    print("<--------------------------->")
    print("<< DRIVING COST CALCULATOR >>")
    print("<--------------------------->")

milesToDrive = 100.0
milesPerGallon = 10.0
dollarsPerGallon = 2.0
milesPerKWh = 4.0
dollarsPerKWh = .25

gasTripCost = calculateGasTripCost(milesToDrive, milesPerGallon, dollarsPerGallon)
electricTripCost = calculateElectricTripCost(milesToDrive, milesPerKWh, dollarsPerKWh)
formattedGasTripCost = "{:.2f}".format(gasTripCost)
formattedElectricTripCost = "{:.2f}".format(electricTripCost)

displayBanner()
print("The cost of a "+str(milesToDrive)+" mile trip by gas is $"+formattedGasTripCost+" and by electric is $"+formattedElectricTripCost+".")
