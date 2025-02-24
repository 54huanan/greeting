FROM python:3.9-alpine

WORKDIR /srv

# 复制 requirements.txt
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt 

# 使容器启动后不退出
CMD ["sh"]  