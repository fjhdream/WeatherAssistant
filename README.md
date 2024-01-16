# WeatherAssistant

WeatherAssistant is a Python application that provides weather suggestions for a specified city and sends these suggestions as messages.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Copy the `.env.example` file and rename it to `.env`:
    ```bash
    cp .env.example .env
    ```
2. Open the .env file and fill in all the environment variables. These variables include:
   - WEATHER_OPENWEATHER_API_KEY: The API key for the weather query
   - WEATHER_COUNTRY_CODE: The country code for querying the weather
   - PUSH_SERVER_SEND_KEY: The key for the sever sauce
   - PUSH_NTFY_SUB_PREFIX: The prefix for the push
   - OPENAI_API_KEY: The API key for OPENAI
   - OPENAI_API_BASE: The base URL for the OPENAI API
3. Save the .env file and run your application.

The main functionality of the application is encapsulated in the `WeatherSub` class. Here is a basic example of how to use it:

```python
from WeatherAssistant import WeatherSub

# Create an instance of WeatherSub for the city you are interested in
weather = WeatherSub('city_name')

# Call the process method to get the weather suggestion and send it
weather.process()
```

Replace `'city_name'` with the name of the city you are interested in.



## Scheduling

The application includes functionality to schedule the weather suggestions to be sent at specific times. This is done using the `schedule` library. The scheduling is set up to run the `process` method of the `WeatherSub` class every hour between 8:00 and 18:00 China time.

## Environment Variables

The application uses environment variables for configuration. These are loaded from a `.env` file at the root of the project. The following environment variables are used:

- `WEATHER_OPENWEATHER_API_KEY`: The API key for the OpenWeather API.

Ensure that you have these environment variables set up in your `.env` file before running the application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)