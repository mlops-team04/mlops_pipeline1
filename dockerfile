FROM apache/airflow:2.10.0-python3.11

USER airflow

RUN pip install kafka-python
RUN pip install python-dotenv
RUN pip install requests


# Git 계정 등록
RUN git config --global Heo-Gyeom
RUN git config --global ajdlarmrp@gmail.com

RUN git clone https://github.com/mlops-team04/mlops_pipeline1.git