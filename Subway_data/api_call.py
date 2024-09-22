import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
from kafka import KafkaProducer
import json

# env 파일에서 API 호출 키 읽어옴
load_dotenv()
API_KEY = os.environ.get('API_KEY')

def get_data_cnt(use_date: str) -> int:
    requests_type = 'json'
    service = 'CardSubwayStatsNew'  # 서비스 명
    start_index = 1
    end_index = 1000
    base_url = f'http://openapi.seoul.go.kr:8088/'
    url = f'{base_url}{API_KEY}/{requests_type}/{service}/{start_index}/{end_index}/{use_date}'
    responses = requests.get(url).json()
    try:
        if responses['CardSubwayStatsNew']['RESULT']['CODE'] == 'INFO-000':
            data_cnt = responses['CardSubwayStatsNew']['list_total_count']
            return data_cnt
        else:
            raise KeyError
    except KeyError:
        msg = responses['RESULT']['MESSAGE']
        print(msg)
        return 0

def api_call(start_index, end_index, use_date) -> list[dict]:
    request_type = 'json'
    service = 'CardSubwayStatsNew'
    base_url = f'http://openapi.seoul.go.kr:8088/'
    url = f'{base_url}{API_KEY}/{request_type}/{service}/{start_index}/{end_index}/{use_date}'
    responses = requests.get(url).json()
    try:
        if responses['CardSubwayStatsNew']['RESULT']['CODE'] == 'INFO-000':
            return responses['CardSubwayStatsNew']["row"]
        else:
            raise KeyError
    except KeyError:
        msg = responses['RESULT']['MESSAGE']
        print(msg)
        return []

def div_cnt_api_call(data_cnt: int, use_date: str) -> list[dict]:
    if data_cnt == 0:
        return []
    cnt = data_cnt // 1000
    cnt_mod = data_cnt % 1000
    datas = []
    for i in range(cnt):
        datas.extend(api_call(i * 1000 + 1, (i + 1) * 1000, use_date))
    datas.extend(api_call(cnt * 1000 + 1, cnt * 1000 + cnt_mod, use_date))
    return datas