from kafka import KafkaProducer
import json
import os 

# Kafka 프로듀서 설정 
def create_producer(bootstrap_servers: list):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer

# JSON 파일을 읽어서 데이터를 가져옴
def read_json_file(file_name: str) -> list[dict]:
    if not os.path.exists(file_name):
        print(f"{file_name} 파일이 존재하지 않습니다.")
        return []
    
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Kafka 토픽으로 데이터를 전송
def send_to_kafka(producer, topic: str, datas: list[dict]):
    for record in datas:
        producer.send(topic, record)  # 데이터 전송
        print(f"Kafka 토픽 '{topic}'에 데이터 전송: {record}")

    producer.flush()  # 메시지가 실제로 전송되도록 플러시
    print("모든 데이터가 Kafka에 전송되었습니다.")
