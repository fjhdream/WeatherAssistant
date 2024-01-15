from datetime import datetime
import time

import pytz
import schedule
from dotenv import load_dotenv

import WeatherAssistant

load_dotenv()


def job(city):
    xianWeatherAssistant = WeatherAssiatant.WeatherSub(city)
    xianWeatherAssistant.process()


def hourly_job(city):
    # 获取当前的时间
    tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.now(tz)

    # 如果当前的时间在 8:00 到 18:00 之间，那么执行 job 函数
    if 8 <= current_time.hour <= 18:
        job(city)


schedule.every().hour.do(hourly_job(city='xian'))
schedule.every().hour.do(hourly_job(city='Beijing'))

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(60)
