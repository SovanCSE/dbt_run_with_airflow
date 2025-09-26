from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="dbt_run_with_bash_operator",
    start_date=datetime(2023, 9, 10),
    schedule="@daily",
    catchup=False,
) as dag:

    run_dbt = BashOperator(
        task_id="dbt_run",
        bash_command=(
            "cd /opt/airflow/dags/dbt/data_pipeline && "
            "dbt run --profiles-dir /opt/airflow/.dbt"
        )
    )
