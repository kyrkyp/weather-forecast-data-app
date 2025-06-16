import requests

API_KEY = "860b7080ce40b90c1abdd96d7f9418e3"

def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        if response.status_code == 404:
            raise Exception(f"City '{place}' doesn't exist. Please check the name and try again.")
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Athens", forecast_days=3))