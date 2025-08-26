import requests

BASE_URL = "https://restcountries.com/v3.1"

def get_countries_all():
    url = f"{BASE_URL}/all"
    params = {
        "fields": "name,population,region"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

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
    except Exception:
        return []


def get_countrie_by_name(name: str):
    url = f"{BASE_URL}/name/{name}"
    
    try: 
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if data:
            return data[0]
    except Exception:
        return None
