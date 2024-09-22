from api_call import *
from datetime import datetime, timedelta
from send_to_kafka import *
from kafka import KafkaConsumer

if __name__ == "__main__":
    # 오늘로부터 3일 전 날짜를 사용
    use_date = (datetime.now() - timedelta(days=4)).strftime('%Y%m%d')

    # 데이터 개수 가져오기
    data_cnt = get_data_cnt(use_date)
    print(f"Total data count: {data_cnt}")

    # API 호출하여 데이터 가져오기
    datas = div_cnt_api_call(data_cnt, use_date)
    print(f"Actually fetched data count: {len(datas)}")

    # Kafka 설정
    bootstrap_servers = ['3.36.140.156:9092']  # Kafka 브로커 주소 리스트
    topic = 'subway_data'  # Kafka 토픽 이름

    # Kafka 프로듀서 생성
    producer = create_producer(bootstrap_servers)

    # Kafka로 데이터 전송
    if datas:
        send_to_kafka(producer, topic, datas)

    # 프로듀서 종료
    producer.close()