import logging

# 创建一个 logger
logger = logging.getLogger(__name__)

# 设置全局日志级别为 DEBUG
logger.setLevel(logging.INFO)

# # 创建一个 handler，用于写入日志文件
# fh = logging.FileHandler('app.log')
#
# # 定义 handler 的输出格式
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
#
# # 给 logger 添加 handler
# logger.addHandler(fh)