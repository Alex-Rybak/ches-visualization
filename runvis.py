from chesvis import visualizeFile
import pandas as pd

countries_years = {"Canada": 2023, "Canada (provinces)":2023,"Europe": 2024,
        "Europe (predicted)": 2024,"Europe (historic, predicted)":[],
         "Europe (historic)":[], "Israel": [],
         "LatAm":2020}

print("Enter the regions and years you wish to see. The options are Canada, Canada (provinces), Israel, LatAm, Europe,"
      "Europe (predicted), Europe (historic), Europe (historic, predicted)")
sets = input("Enter the regions with \", \" between them: ").split(", ")

years = []
for set in sets:
    if set == "Israel" or set == "Europe (historic)" or  set == "Europe (historic, predicted)":
        years += input("Enter the years you wish to see data for: ").split(", ")
        showYears = input("Show years? Y/n") == "Y"
    else:
        years.append(countries_years[set])
        showYears = False
    visualizeFile(sets,years,showYears)

