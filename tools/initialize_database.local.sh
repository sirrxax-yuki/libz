#!/bin/sh +x

SCRIPT_DIR=$(cd $(dirname $0) && pwd)
cd ${SCRIPT_DIR}

export DATABASE_HOST=localhost
export DATABASE_PORT=3306
export DATABASE_USER=master
export DATABASE_PASSWORD=password
export DATABASE_NAME=libz

python initialize_database.py
