counties = ["Arapahoe","Denver","Jefferson"]
if "Apache" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso are both in the list of counties")
else:
    print("Either Arapahoe or El Paso are not in the list of counties")
for county in counties:
    print(county)

