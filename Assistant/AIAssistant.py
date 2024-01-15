from datetime import datetime

import pytz
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_openai import ChatOpenAI

from Config.LoggerConfig import logger
from Query.WetherQuery import description

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    """
    你是一个专业的私人助理, 天气助手, 熟悉天气, 请根据当前的天气状况，提供多方面建议.
推荐合适的衣物选择，例如轻薄或保暖的服装，防晒或防雨措施。
考虑天气条件，提出室内或室外的活动建议，如晴天推荐户外运动，雨天则建议室内活动。
这些建议将帮助用户更好地准备当天的行程，确保舒适和安全。
现在的时间是: {time}
以下是今天的天气情况
{context}

以下为回复模板[()中不用在模板中带上, 作为回复指导]:
⏰现在的时间是: xxx (根据上下文中的时间, 格式为 x年x月x日x点x分)
🌡️体感是: xxxx(今天天气对个人的感觉, 寒冷, 温暖, 舒适等方面)
🧣适宜的穿搭是: xxx (在体感温度的前提下,给出合理的穿搭,适合 50 字以内)
⚽️适宜的活动是: xxx (在这样的天气下, 适合进行什么样的活动)
🎉祝福: xxx (返回一条今天的寄语或者祝福)
    """
)
output_parser = StrOutputParser()
model = ChatOpenAI(model="gpt-4-1106-preview")


def now_time(_):
    tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.now(tz)
    print(current_time)
    return current_time


chain = (
        RunnablePassthrough() |
        (lambda context: {"context": description(context), "time": now_time(context)})
        | prompt
        | model
        | output_parser
)


def suggestion(country_name):
    invoke = chain.invoke(country_name)
    logger.info(invoke)
    return invoke
