from kafka import KafkaProducer
from api_call import response_content

# Kafka 프로듀서 인스턴스 생성
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# 메시지 전송
# producer.send(topic, value)
producer.send('api_call', response_content)
producer.flush()
