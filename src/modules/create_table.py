import psycopg2

conn = psycopg2.connect(dbname='api_call', user='postgres', password='postgres', host='127.0.0.1', port=5432)

cur = conn.cursor()  # 커서 생성

# 테이블 생성
cur.execute("CREATE TABLE api_call_table (\
            id SERIAL PRIMARY KEY, \
            USE_YMD integer, \
            SBWY_ROUT_LN_NM varchar, \
            SBWY_STNS_NM varchar, \
            GTON_TNOPE integer, \
            GTOFF_TNOPE integer, \
            REG_YMD integer\
            );")

conn.commit()
cur.close()
conn.close()
