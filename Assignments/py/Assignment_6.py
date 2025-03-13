# Name: Hia Al Saleh
# Date: October 25th of the year 2024
# File: Assignment_6.py

# Purpose: Store and analyze data of the top 10 cities in Ontario.

ontario_cities = {
    "Toronto": {
        "population": 2731571,
        "area (sq km)": 630.21,
        "density (people/sq km)": 4334.4, 
        "growth rate": 4.2,
        "world percentage": 0.035,
        "net change": 111779,
    },
    "Ottawa": {
        "population": 934243,
        "area (sq km)": 2790.33, 
        "density (people/sq km)": 335.0, 
        "growth rate": 5.3,
        "world percentage": 0.012,
        "net change": 47537,
    },
    "Mississauga": {
        "population": 721599,
        "area (sq km)": 292.43,
        "density (people/sq km)": 2468.3, 
        "growth rate": 7.7,
        "world percentage": 0.009,
        "net change": 51876,
    },
    "Brampton": {
        "population": 593638,
        "area (sq km)": 266.71,
        "density (people/sq km)": 2226.3, 
        "growth rate": 13.3,
        "world percentage": 0.008,
        "net change": 69392,
    },
    "Hamilton": {
        "population": 536917,
        "area (sq km)": 1138.11, 
        "density (people/sq km)": 470.8, 
        "growth rate": 4.0,
        "world percentage": 0.007,
        "net change": 20653,
    },
    "London": {
        "population": 403437,
        "area (sq km)": 420.57,
        "density (people/sq km)": 958.8,
        "growth rate": 4.8,
        "world percentage": 0.005,
        "net change": 18721,
    },
    "Markham": {
        "population": 328966,
        "area (sq km)": 212.58,
        "density (people/sq km)": 1547.1,
        "growth rate": 15.3,
    },
    "Vaughan": {
        "population": 306233,
        "area (sq km)": 273.56,
        "density (people/sq km)": 1118.5,
        "growth rate": 13.9,
        "world percentage": 0.004,
        "net change": 37265,
    },
    "Kitchener": {
        "population": 270133,
        "area (sq km)": 136.89,
        "density (people/sq km)": 1970.0,
        "growth rate": 6.3,
        "world percentage": 0.004,
        "net change": 16044,
    },
    "Windsor": {
        "population": 217188,
        "area (sq km)": 146.29,
        "density (people/sq km)": 1485.1,
        "growth rate": 2.6,
        "world percentage": 0.003,
        "net change": 5491,
    },
}

# 1. Print the data type of variable ontario_cities.
print('=' * 15 + " Question 1 " + '=' * 15)
print(type(ontario_cities))

# 2. Print the length of the ontario_cities.
print('=' * 15 + " Question 2 " + '=' * 15)
print("Number of cities in Ontario:", len(ontario_cities))

# 3. Print the keys of the ontario_cities.
print('=' * 15 + " Question 3 " + '=' * 15)
print('Ontario Cities:', list(ontario_cities.keys()))

# 4. Print the details of the city "Mississauga".
print('=' * 15 + " Question 4 " + '=' * 15)
mississauga = ontario_cities['Mississauga']
print("Details of the city Mississauga:")
print("-" * 30)
for key, value in mississauga.items():
    print(f"{key.capitalize()}: {value}")
print("-" * 30)

# 5. Print all keys in subdirectories.
print('=' * 15 + " Question 5 " + '=' * 15)
for city, details in ontario_cities.items():
    print(f"City: {city}")
    print("Keys:")
    for key in details.keys():
        print(f"  ✻ {key}") # ✻ is a star symbol as a bullet point
    print("-" * 30)

# 6. Print the population of all cities.
print('=' * 15 + " Question 6 " + '=' * 15)
for city, details in ontario_cities.items():
    print(f"The population of {city} is {details['population']}")

# 7. Print the city with the highest population.
print('=' * 15 + " Question 7 " + '=' * 15)
highest_population = 0
highest_population_city = ""
for city, details in ontario_cities.items():
    if details['population'] > highest_population:
        highest_population = details['population']
        highest_population_city = city
print(f"The city with the highest population is {highest_population_city} with a population of {highest_population}")

# 8. Print the city with the lowest population.
print('=' * 15 + " Question 8 " + '=' * 15)
lowest_population = float('inf')
lowest_population_city = ""
for city, details in ontario_cities.items():
    if details['population'] < lowest_population:
        lowest_population = details['population']
        lowest_population_city = city
print(f"The city with the lowest population is {lowest_population_city} with a population of {lowest_population}")