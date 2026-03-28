import requests
import json

def tmdb_api_call(requestURL, parameters):
    try:
        response = requests.get(url=requestURL, params=parameters, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"ERROR: {e}")
        return None


def get_upcoming_movies_by_page(api_key, page_number=1):
    requestURL = "https://api.themoviedb.org/3/movie/upcoming"
    parameters = {
        "api_key": api_key,
        "page": page_number
    }
    return tmdb_api_call(requestURL, parameters)


def main():
    api_key = "5942439a1fff5c3f41eacebba7cee556"   # 🔴 Replace with new key

    data = get_upcoming_movies_by_page(api_key, 1)

    if data and "results" in data:
        for movie in data["results"]:
            print(json.dumps(movie))   # ✅ FULL JSON per movie (IMPORTANT)
    else:
        print("ERROR: Failed to fetch data")


if __name__ == "__main__":
    main()