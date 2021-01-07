from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    'start_date': days_ago(2),
    'retries': 0,
}

with DAG(
        dag_id='xcom_docker_dag',
        schedule_interval=None,
        default_args=default_args,
    ) as dag:

    xcom_no = DockerOperator(
        task_id='xcom_no',
        image='python',
        command='python -c "for i in range(10): print(i)"',
        do_xcom_push=False,
        xcom_all=False,        
    )

    xcom_all = DockerOperator(
        task_id='xcom_all',
        image='python',
        command='python -c "for i in range(10): print(i)"',
        do_xcom_push=True,
        xcom_all=True,
    )

    xcom_last = DockerOperator(
        task_id='xcom_last',
        image='python',
        command='python -c "for i in range(10): print(i)"',
        do_xcom_push=True,
        xcom_all=False,
    )    