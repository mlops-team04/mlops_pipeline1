from kafka import KafkaConsumer

# Kafka 컨슈머 인스턴스 생성
consumer = KafkaConsumer('api_call',
                         group_id='test-group',
                         bootstrap_servers=['localhost:9092'])

# 메시지 수신 및 출력
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
