import requests

BASE_URL = "https://restcountries.com/v3.1"

def get_countries_all():
    url = f"{BASE_URL}/all"
    params = {
        "fields": "name,population,region"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return [
            {
                "nome": countrie.get("name", {}).get("common"),
                "populacao": countrie.get("population"),
                "continente": countrie.get("region"),
            }
            for countrie in data

            if countrie.get("name") and isinstance(countrie.get("population"), int)
        ]
    return []

def get_countrie_by_name(name: str):
    url = f"{BASE_URL}/name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data:
            return data[0]
    return None
