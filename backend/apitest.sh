#!/bin/sh

SCRIPT_DIR=$(cd $(dirname $0) && pwd)
cd ${SCRIPT_DIR}

export DATABASE_HOST=localhost
export DATABASE_PORT=3306
export DATABASE_USER=testmaster
export DATABASE_PASSWORD=testpassword
export DATABASE_NAME=test

trap finally EXIT
finally() {
    docker rm -f libz-testdb
    kill ${BACKEND_PID}
}

docker run \
    --name libz-testdb \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=${DATABASE_PASSWORD} \
    -e MYSQL_USER=${DATABASE_USER} \
    -e MYSQL_PASSWORD=${DATABASE_PASSWORD} \
    -e MYSQL_DATABASE=${DATABASE_NAME} \
    -d mariadb:11.2-jammy
echo ready...
sleep 10

nohup poetry run uvicorn src.main:app --host=localhost --port=3304 --reload &
BACKEND_PID=$!
echo ${BACKEND_PID}

poetry run python ./initialize_database.py

echo run stepci
cd openapi/workflows
stepci run knowledge.yml --env APP_HOST=localhost --env APP_PORT=3304
