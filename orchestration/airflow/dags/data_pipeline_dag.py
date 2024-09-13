from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from ingestion.kafka.kafka_producer import produce_data
from processing.spark.spark_job import run_spark_job

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('data_pipeline_dag', default_args=default_args, schedule_interval='@quarterly')

ingest_task = PythonOperator(
    task_id='ingest_data',
    python_callable=produce_data,
    dag=dag
)

process_task = PythonOperator(
    task_id='process_data',
    python_callable=run_spark_job,
    dag=dag
)

ingest_task >> process_task
