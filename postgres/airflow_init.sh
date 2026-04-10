#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$DB_USER" --dbname "$DB_NAME" <<-EOSQL
    CREATE USER airflow WITH PASSWORD '$AF_DB_PASSWORD';
    CREATE DATABASE airflow_db OWNER airflow;
EOSQL