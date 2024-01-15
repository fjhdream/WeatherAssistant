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


def kelvin_to_celsius(temp_k):
    """将开尔文温度转换为摄氏度"""
    return temp_k - 273.15


def unix_to_readable(unix_time):
    """将 UNIX 时间戳转换为可读的时间"""
    return datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S UTC')


def weather_description(data):
    city = data['name']
    weather_condition = data['weather'][0]['description']
    temp_k = data['main']['temp']
    temp_c = kelvin_to_celsius(temp_k)
    feels_like_k = data['main']['feels_like']
    feels_like_c = kelvin_to_celsius(feels_like_k)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']

    wind_speed = data['wind']['speed']
    wind_deg = data['wind']['deg']

    clouds = data['clouds']['all']
    visibility = data['visibility']

    sunrise = unix_to_readable(data['sys']['sunrise'])
    sunset = unix_to_readable(data['sys']['sunset'])

    description = (
        f"{city}当前的天气状况是{weather_condition}。"
        f"当前气温为{temp_c:.2f}摄氏度，体感温度是{feels_like_c:.2f}摄氏度。"
        f"气压为{pressure}百帕，相对湿度为{humidity}%。"
        f"风速为每秒{wind_speed}米，风向为{wind_deg}度。"
        f"云量为{clouds}%，能见度为{visibility}米。"
        f"日出时间为{sunrise}，日落时间为{sunset}。"
    )
    logger.info(description)
    return description


api_key = os.environ["WEATHER_OPENWEATHER_API_KEY"]
country_code = os.environ["WEATHER_COUNTRY_CODE"]


def description(country_name):
    weather = get_weather(api_key, country_name, country_code)
    if weather is None:
        logger.error("天气查询失败")
        raise Exception("天气查询失败");
        return None
    description = weather_description(weather)
    print(description)
    return description
