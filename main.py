import time

import schedule
from dotenv import load_dotenv

import WeatherAssistant

load_dotenv()


def job(city):
    max_attempts = 3  # 设置最大尝试次数
    for attempt in range(max_attempts):
        try:
            xianWeatherAssistant = WeatherAssistant.WeatherSub(city)
            xianWeatherAssistant.process()
            break  # 如果成功执行，跳出循环
        except Exception as e:
            print(f"Attempt {attempt+1} failed with error: {e}")
            if attempt + 1 == max_attempts:
                print("Reached maximum number of attempts. Job failed.")


def schedule_task(task, parameter):
    # 安排每天 8:00 到 18:00 之间的任务
    for hour in range(8, 19):
        schedule.every().day.at(f"{hour:02d}:00").do(task, parameter)


schedule_task(job, "xian")
schedule_task(job, "beijing")


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
