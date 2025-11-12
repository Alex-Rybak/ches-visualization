from chesvis import visualizeFile
import pandas as pd

countries_years = {"Canada": [2023], "Canada (provinces)":[2023],"Europe": [2024],
        "Europe (predicted)": [2024],"Europe (historic predicted)":[1999, 2002, 2006, 2010, 2014, 2019],
         "Europe (historic)":[1999, 2002, 2006, 2010, 2014, 2019], "Israel": [2021,2022],
         "LatAm":[2020]}

print("Enter the regions and years you wish to see. The options are Canada, Canada (provinces), Israel, LatAm, Europe,"
      "Europe (predicted), Europe (historic), Europe (historic predicted)")
sets = input("Enter the regions with \", \" between them: ").split(", ")

years = []


for set in sets:
    if len(countries_years[set]) > 1:
        years += input(f"Enter the years you wish to see data for (available years: {countries_years[set]}): ").split(", ")
    else:
        years += countries_years[set]
showYears = input("Show years? Y/n")=="Y"


visualizeFile(sets,years,showYears)

