from kafka import KafkaConsumer
import json

# Kafka 컨슈머 인스턴스 생성
# 추가 옵션 key_deserializer, value_deserializer
consumer = KafkaConsumer('api_call',
                         group_id='test-group',
                         auto_offset_reset='latest',
                         bootstrap_servers=['localhost:9092'])

# 메시지 수신 및 출력
for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))

# postgresql에 입력하기 위해(bytes 타입 지원 하지 않음) 메시지 타입 변경(bytes -> UTF8)
# json 모양인 문자열 타입이라 json 타입으로 변경
# type 확인
message_value = message.value
message_value_utf8 = message_value.decode('utf8')
message_value_json = json.loads(message_value_utf8)
