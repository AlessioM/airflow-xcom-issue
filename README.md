# setup

## start postgres
`docker-compose up -d postgres_airflow`

## init db and add user
`docker-compose run airflow_init`

## run webserver
`docker-compose up -d airflow_webserver`

## run scheduler
`docker-compose up  airflow_scheduler`


# running
* web server is exposed on port 9090
* login admin/airflow
* dag_id is `xcom_docker_dag`
* task logs can be found in `./logs`

# reproduce
* run dag `xcom_docker_dag`
* task `xcom_no` succedes, `xcom_all` and `xcom_last` fail with `TypeError: Object of type bytes is not JSON serializable`

# fix
* mount fixed_docker.py into scheduler (uncommend line in `docker-compose.yml`)
* run dag `xcom_docker_dag`
* all task succeed
* check xcom of tasks:
  * `xcom_no`: empty
  * `xcom_all`: 	0 1 2 3 4 5 6 7 8 9
  * `xcom_last`: 	9