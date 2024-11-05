from kafka import KafkaProducer
import json


# Kafka 프로듀서 설정
def create_producer(bootstrap_servers: list):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer


# Kafka 토픽으로 데이터를 전송
def send_to_kafka(producer, topic: str, datas: list[dict]):
    for record in datas:
        producer.send(topic, record)  # 데이터 전송
        print(f"Kafka 토픽 '{topic}'에 데이터 전송: {record}")

    producer.flush()  # 메시지가 실제로 전송되도록 플러시
    print("모든 데이터가 Kafka 전송되었습니다.")
