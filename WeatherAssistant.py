from Assistant.AIAssistant import suggestion
from Message.MessagePush import send


class WeatherSub:

    def __init__(self, city):
        self.city = city

    def process(self):
        suggest = suggestion(self.city)
        send(suggest, self.city)
