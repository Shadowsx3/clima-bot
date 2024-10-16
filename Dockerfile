FROM python:3.12-slim
WORKDIR /bot
COPY . /bot
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "bot.py", "prod"]