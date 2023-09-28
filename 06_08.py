# Дан словарь, ключ - Название страны, значение - список городов,
# на вход поступает город, необходимо сказать из какой он страны

def country_finding(city, list_of_cities):
    for country, cities in list_of_cities.items():
        if city in cities:
            return country


list_of_cities = {"Germany": ["Berlin", "Frankfurt", "Munich"],
                  "France": ["Paris", "Marcel", "Amiens"],
                  "Belgium": ["Brussel", "Gent", "Brugge"]
                  }

city_to_find = input("Введите название города: ")
result = country_finding(city_to_find, list_of_cities)
if result != "Город не найден":
    print(f"Город {city_to_find} находится в стране {result}.")
