import json
import os

import requests
from datetime import datetime

from dotenv import load_dotenv

from Config.LoggerConfig import logger

load_dotenv()


def get_weather(api_key, country_name, country_code):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    query = f'?q={country_name},{country_code}&APPID={api_key}'
    complete_url = base_url + query
    response = requests.get(complete_url)
    logger.info("weather query resp: {}", response)
    weather_data = response.json()
    if weather_data['cod'] == 200:
        return weather_data
    else:
        return None


api_key = os.environ["WEATHER_OPENWEATHER_API_KEY"]
country_code = os.environ["WEATHER_COUNTRY_CODE"]


def description(country_name):
    weather = get_weather(api_key, country_name, country_code)
    if weather is None:
        logger.error("天气查询失败")
        raise Exception("天气查询失败");
        return None
    return json.dumps(weather)
