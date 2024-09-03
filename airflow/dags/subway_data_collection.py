from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 3),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'subway_data_collection',
    default_args=default_args,
    description='Collect subway data daily',
    schedule_interval='20 20 * * *',
    catchup=False
)


#시작을 알리는 dummy 
task_start = EmptyOperator(
    task_id='start',
    dag=dag,
)

#시작이 끝나고 다음단계로 진행되었음을 나타내는 dummy
task_next = EmptyOperator(
    task_id='next',
    trigger_rule='all_success',
    dag=dag,
)

#python file을 실행시킬 bashoperator (데이터 json으로 가져오는 파일, json파일을 카프카로 보내는 파일)
#데이터를 수집하는 파일
task_collect_data = BashOperator(
    task_id='collect_data',
    bash_command='python ../../Subway_data/main.py',  # 데이터 수집 스크립트 경로
    dag=dag,
)


# #카프카로 내보내는 파일 
# task_send_to_kafka = BashOperator(
#     task_id='send_to_kafka',
#     bash_command='python ../../Subway_data/send_to_kafka.py',  # Kafka로 내보내는 스크립트 경로
#     dag=dag,
# )


# 끝을 알리는 dummy
task_finish = EmptyOperator(
    task_id='finish',
    dag=dag,
)

task_start >> task_next >> task_collect_data >> task_finish