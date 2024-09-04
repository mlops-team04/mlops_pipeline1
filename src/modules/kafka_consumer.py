from kafka import KafkaConsumer

# Kafka 컨슈머 인스턴스 생성
consumer = KafkaConsumer('api_call',
                         group_id='test-group',
                         bootstrap_servers=['localhost:9092'])

# 메시지 수신 및 출력
for message in consumer:
    # print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                      message.offset, message.key,
    #                                      message.value))

# postgresql에 입력하기 위해(bytes 타입 지원 하지 않음) 메시지 타입 변경(bytes -> UTF8)
    print(type(message.value))
