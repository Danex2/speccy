FROM python:3.6.6-alpine3.6

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install --upgrade aiohttp
RUN pip3 install --upgrade websockets

CMD ["python", "./bot.py"]