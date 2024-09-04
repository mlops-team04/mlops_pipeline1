from kafka import KafkaConsumer
import json
import psycopg2

def run():
    # Kafka 컨슈머 인스턴스 생성
    consumer = KafkaConsumer('api_call',
                            group_id='test-group',
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
        # print(message_value_utf8)
        # print(type(message_value_utf8))
        # print(type(message_value_json))
        for spot in range(5):
             preprocessed_message = preprocess(message_value_json, spot)
             transport(preprocessed_message)
        

# 메시지 전처리 함수 정의
def preprocess(message, spot):
        USE_YMD = int(message["CardSubwayStatsNew"]['row'][spot]["USE_YMD"])
        SBWY_ROUT_LN_NM = str(message["CardSubwayStatsNew"]['row'][spot]["SBWY_ROUT_LN_NM"])
        SBWY_STNS_NM = str(message["CardSubwayStatsNew"]['row'][spot]["SBWY_STNS_NM"])
        GTON_TNOPE = int(message["CardSubwayStatsNew"]['row'][spot]["GTON_TNOPE"])
        GTOFF_TNOPE = int(message["CardSubwayStatsNew"]['row'][spot]["GTOFF_TNOPE"])
        REG_YMD = int(message["CardSubwayStatsNew"]['row'][spot]["REG_YMD"])
        message_values = (USE_YMD, SBWY_ROUT_LN_NM, SBWY_STNS_NM, GTON_TNOPE, GTOFF_TNOPE, REG_YMD)
        return message_values

# 메시지 전송 함수 정의
def transport(message):
    # PostgreSQL 데이터베이스에 연결
    conn = psycopg2.connect(dbname='api_call', user='postgres', password='postgres', host='127.0.0.1', port=5432)

    cur = conn.cursor()  # 커서 생성

    # 데이터 삽입
    query = "INSERT INTO api_call_table (USE_YMD, SBWY_ROUT_LN_NM, SBWY_STNS_NM, GTON_TNOPE, GTOFF_TNOPE, REG_YMD)\
          VALUES (%s, %s, %s, %s, %s, %s)"
    values = message
    cur.execute(query, values)

    # 커밋 및 연결 종료
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    run()
