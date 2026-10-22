"""
Module Name: Country Population Analyzer Template
Description: Stores information about multiple countries and identifies the countries with the largest and smallest populations.
Author: Kollier
"""

countries = []
n = int(input("How many countries would you like to register? "))

for i in range(n):
    print(f"\n--- Country {i + 1} ---")
    name = input("Country name: ")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))
    coordinates = (latitude, longitude)
    main_dish = input("Main traditional dish: ")
    language = input("Native language: ")
    currency = input("Currency: ")
    population = int(input("Population: "))

    country = {
        "name": name,
        "coordinates": coordinates,
        "main_dish": main_dish,
        "language": language,
        "currency": currency,
        "population": population
    }
    countries.append(country)

country_largest = countries[0]
country_smallest = countries[0]

for country in countries:
    if country["population"] > country_largest["population"]:
        country_largest = country

    if country["population"] < country_smallest["population"]:
        country_smallest = country

print(f"Country with the largest population: {country_largest['name']}")
print(f"Population: {country_largest['population']:,}")

print(f"\nCountry with the smallest population: {country_smallest['name']}")
print(f"Population: {country_smallest['population']:,}")