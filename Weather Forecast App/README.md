# OpenWeatherMap API Weather Query

This Python script queries weather data for a specified city using the OpenWeatherMap API and prints out the weather details.

## Functions in the Script

- **Importing Libraries**: `requests` for making HTTP requests, `json` for JSON manipulation.

- **`get_weather_data` Function**: This function takes an API key and a city name as parameters, constructs an HTTP request to the OpenWeatherMap API, retrieves the weather data, and returns it in JSON format.

- **`display_weather` Function**: It takes the JSON data from `get_weather_data`, checks if the city is found (`"cod" != "404"`), and prints out relevant weather details such as temperature, description, humidity, and wind speed. If the city is not found, it informs the user.

- **`main` Function**: This is the main driver function. It prompts the user for a city name, calls `get_weather_data` using an API key and the entered city, then passes the result to `display_weather` to display the information.

## Execution Flow

1. An API key for OpenWeatherMap is required and should be set where `"YOUR_API_KEY"` is indicated.
2. The script prompts the user for a city name.
3. The `get_weather_data` function is called with the user-provided city and the API key to fetch the weather data.
4. The `display_weather` function takes the returned data and prints out the weather information.

## How to Run

To run the script:

- Replace `"YOUR_API_KEY"` with a valid API key from OpenWeatherMap.
- Execute the script in a Python environment.
- Enter the name of the city when prompted.
- View the printed weather details for the entered city.

Note: Ensure that you have a working internet connection and a valid API key from OpenWeatherMap for the script to function properly.
