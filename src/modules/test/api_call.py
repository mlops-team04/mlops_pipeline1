import os
import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

#env 파일에서 API 호출 키 읽어옴

load_dotenv()
API_KEY = os.environ.get('API_KEY')

def get_data_cnt(use_date: str) -> int:
    requests_type = 'json'
    service = 'CardSubwayStatsNew' #서비스 명
    start_index = 1
    end_index = 1000
    base_url = f'http://openapi.seoul.go.kr:8088/'
    use_date = (datetime.now() - timedelta(days=4)).strftime('%Y%m%d')

    url = f'{base_url}' + f'{API_KEY}/{requests_type}/{service}/{start_index}/{end_index}/{use_date}'


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
        data_cnt = 0
        return data_cnt
    
def api_call(start_index, end_index, use_date) -> list[dict]:
    request_type = 'json'  # xml : xml, xml파일 : xmlf, 엑셀파일 : xls, json파일 : json
    service = 'CardSubwayStatsNew'  # 서비스 명
    # start_index = 1  # 정수 입력 (페이징 시작번호 입니다 : 데이터 행 시작번호)
    # end_index = 5  # 정수 입력 (페이징 끝번호 입니다 : 데이터 행 끝번호) max: 1000
    # use_date = '20240826'  # YYYYMMDD 형식의 문자열
    base_url = f'http://openapi.seoul.go.kr:8088/'
    url = f'{base_url}' + f'{API_KEY}/{request_type}/{service}/{start_index}/{end_index}/{use_date}'

    responses = requests.get(url).json()  # responses: json -> dict
    try:
        if responses['CardSubwayStatsNew']['RESULT']['CODE'] == 'INFO-000':
            datas = responses['CardSubwayStatsNew']["row"]  # datas: list
            return datas
        else: raise KeyError
    except KeyError:
        msg = responses['RESULT']['MESSAGE']
        print(msg)
        datas = []
        return datas

def div_cnt_api_call(data_cnt: int, use_date: str) -> list[dict]:

    if data_cnt == 0:
        return []
    cnt = data_cnt // 1000
    cnt_mod = data_cnt % 1000
    datas=list()
    for i in range(cnt):
        datas.extend(api_call(i * 1000 + 1, (i + 1) * 1000, use_date))
    datas.extend(api_call(cnt * 1000 + 1, cnt * 1000 + cnt_mod, use_date))
    return datas


def save_json_data(datas: list[dict]) -> None:
    if datas == []:
        return None
    use_data = datas[0]['USE_YMD']
    file_name = f'{use_data}.json'
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(datas, file, ensure_ascii=False, indent=4)
    print(f'SJON 데이터가 {file_name} 파일로 저장되었습니다.')
    
    
    

