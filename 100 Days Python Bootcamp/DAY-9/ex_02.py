# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.

# Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.

# add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
# DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

# Example Input
# Brazil
# 5
# ["Sao Paulo", "Rio de Janeiro"]
# Example Output
# I've been to Brazil 5 times.
# My favourite city was Sao Paulo.
# Hint
# Look at the function call above to see what the name of the function should be.

# The inputs for the function are positional arguments. The order is very important.

# Feel free to choose your own parameter names.

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string
  
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)
# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

def add_new_country(country, visits, cities):

    travel_log2.append({'country': country, 'cities_visited': cities, 'total_visits': int(visits) })

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

travel_log["France"] = {'cities_visited' : ["Paris", "Lille", "Dijon"]}

print(travel_log)

travel_log2 = [
    {'country':'France',
     'cities_visited' :["Paris", "Lille", "Dijon"],
     'total_visits' : 12,
     },
    {'country':'Germany',
     'cities_visited' :["Berlin", "Hamburg", "Stuttgart"],
     'total_visits' : 5,
     },
]

print(travel_log2)

add_new_country('Russia', 2, ["Moscow", "St. Petersburg"])
print(travel_log2)
