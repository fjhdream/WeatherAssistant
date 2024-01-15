# 使用轻量级的 Python 3.9 镜像
FROM python:3.9-slim-buster

# 设置工作目录
WORKDIR /app

# 将项目文件复制到工作目录
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置运行应用的命令
CMD ["python", "main.py"]