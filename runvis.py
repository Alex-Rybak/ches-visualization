from chesvis import visualizeFile
import pandas as pd

countries_years = {"Canada": 2023, "Canada (provinces)":2023,"Europe": 2024,
         "Europe (historic)":[], "Israel": [],
         "LatAm":[]}

print("Enter the regions and years you wish to see. The options are Canada, Canada (provinces), Europe, Europe (historic), Israel, LatAm")
sets = input("Enter the regions with \", \" between them: ").split(", ")
print(sets)
years = []
for set in sets:
    if set == "Israel" or set == "Europe (historic)":
        years += input("Enter the years you wish to see data for: ").split(", ")
    else:
        years.append(countries_years[set])
print(years)

visualizeFile(sets,years)

