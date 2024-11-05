from kafka import KafkaProducer

from api_call import response_content

# Kafka 프로듀서 인스턴스 생성
# KafkaProducer(bootstrap_servers), 추가 옵션 key_serializer
# 메시지 전송
# send(topic, value), 추가 옵션 key, headers, partition, timestamp_ms
# producer = KafkaProducer(bootstrap_servers='localhost:9092')
# producer.send('api_call_1', response_content)
# producer.flush()

# Kafka 프로듀서 인스턴스 생성
# KafkaProducer(bootstrap_servers), 추가 옵션 key_serializer
# 메시지 전송
# send(topic, value), 추가 옵션 key, headers, partition, timestamp_ms
# 토픽 같게 하고 키 값에 따라 밸류 다르게 하려면 api 받고 전처리를 잘 해서 넘겨줘야 하네
producer = KafkaProducer(bootstrap_servers='localhost:9092', key_serializer=str.encode)
producer.send('api_call', response_content, key='station')
producer.flush()
