FROM apache/airflow:2.10.0-python3.11

USER airflow

RUN pip install kafka-python
RUN pip install python-dotenv
RUN pip install requests