import ast
import requests

def food_facts(food):
    url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
    querystring = {"query": food}
    headers = {
        'x-rapidapi-host': "calorieninjas.p.rapidapi.com",
        'x-rapidapi-key': "7603016162msh8263f88a5aa10dfp18e91ajsna3493aef8fcf"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an error for non-successful status codes
        dict_response = response.json()

        food_facts = {
            "saturated fat": dict_response["items"][0]["fat_saturated_g"],
            "total fat": dict_response["items"][0]["fat_total_g"],
            "carbs": dict_response["items"][0]["carbohydrates_total_g"],
            "protein": dict_response["items"][0]["protein_g"],
            "sugar": dict_response["items"][0]["sugar_g"],
            "sodium": dict_response["items"][0]["sodium_mg"],
            "cholesterol": dict_response["items"][0]["cholesterol_mg"]
        }

        for key, value in food_facts.items():
            print(f"{key.title()}: {value}")

    except requests.RequestException as e:
        print("Error: Failed to make API request:", e)

    except (KeyError, IndexError):
        print("Error: Unexpected response format. Unable to extract nutrition facts.")

# Example usage
food_facts("apple")
