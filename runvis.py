from chesvis import visualizeFile

print("Enter the countries and years you wish to see. The options are Canada, Europe, Europe (historic), Israel, LatAm")
sets = input("Enter the countries with \", \" between them: ").split(", ")
print(sets)
years = input("Enter the years in a similar format: ").split(", ")
print(years)

visualizeFile(sets,years)