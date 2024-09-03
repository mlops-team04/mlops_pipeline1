
from send_to_kafka import * 

if __name__ == "__main__":
    # 오늘로부터 4일 전 날짜를 사용
    use_date = (datetime.now() - timedelta(days=4)).strftime('%Y%m%d')
    
    # 데이터 개수 가져오기
    data_cnt = get_data_cnt(use_date)
    print(f"Total data count: {data_cnt}")

    # API 호출하여 데이터 가져오기
    datas = div_cnt_api_call(data_cnt, use_date)
    
    # JSON 파일로 저장
    save_json_data(datas)