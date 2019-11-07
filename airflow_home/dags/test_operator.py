from datetime import datetime

from airflow.operators import TestOperator
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('new_operator_test',
          description='try new operator',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

dummy_task = DummyOperator(task_id='dummy_task', dag=dag)
operator_task = TestOperator(my_operator_param='TEST RUN',
                             task_id='test_operator_task',
                             dag=dag)

dummy_task >> operator_task
