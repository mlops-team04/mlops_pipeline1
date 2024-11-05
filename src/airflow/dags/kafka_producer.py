#import subprocess

#subprocess.run("sudo pip install kafka-python")

from kafka import KafkaProducer

import json

#Kafka 프로듀서 인스턴스 생성
#KafkaProducer(bootstrap_servers), 추가 옵션 key_serializer
#메시지 전송
#send(topic, value), 추가 옵션 key, headers, partition, timestamp_ms
# producer = KafkaProducer(bootstrap_servers='localhost:9092')
# producer.send('api_call_1', response_content)
# producer.flush()

#Kafka 프로듀서 인스턴스 생성
#KafkaProducer(bootstrap_servers), 추가 옵션 key_serializer
#메시지 전송
#send(topic, value), 추가 옵션 key, headers, partition, timestamp_ms
#토픽 같게 하고 키 값에 따라 밸류 다르게 하려면 api 받고 전처리를 잘 해서 넘겨줘야 하네

def send_kafka_broker():

    producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap.default.svc:9092', key_serializer=str.encode)

    FILE_PATH = '/opt/airflow/temp/response_content.json'

    with open(FILE_PATH, 'r') as f:
        data = json.dump(f)

    producer.send('my-topic', data, key='subway')
    producer.flush()
