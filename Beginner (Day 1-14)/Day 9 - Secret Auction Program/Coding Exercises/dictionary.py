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
# ------------- VERSION 1 --------------------
def add_new_country(country, visit, city):
    travel_log.append({"country":country,"visits":visit,"cities":city})

# -------------- VERSION 2 -------------------
def add_new_country(country, visit, city):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visit
    new_country["cities"] = city
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

#addition: changing value of a nested dictionary inside a list:
for travel_entry in travel_log:
    if travel_entry["country"] == "France":
        travel_entry["country"] = "China"

#addition: assiging a dictionary to another dictionary
final_travelLog = travel_log #this will get all of the contents inside the list 
print(final_travelLog)