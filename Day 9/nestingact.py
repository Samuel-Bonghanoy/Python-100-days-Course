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

def add_new_country(country, visits, cities):
    dictionary = {}
    dictionary["country"] = country
    dictionary["visits"] = visits
    dictionary["cities"] = cities
    travel_log.append(dictionary)
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)