import os
import requests
import json
import datetime


def start():

    api_key = os.getenv('API_KEY')

    now = datetime.datetime.now()
    before = now - datetime.timedelta(days=5)
    date = before.date().strftime('%Y%m%d')

    url = f'http://openapi.seoul.go.kr:8088/{api_key}/json/CardSubwayStatsNew/1/600/{date}'

    response = requests.get(url)
    response_content = response.content

    FILE_PATH = '/opt/airflow/temp/response_content.json'

    with open(FILE_PATH, 'w') as f:
        json.dump(response_content, f)

