#!/bin/sh

export DATABASE_HOST=localhost
export DATABASE_PORT=3306
export DATABASE_USER=testmaster
export DATABASE_PASSWORD=testpassword
export DATABASE_NAME=test

trap finally EXIT
finally() {
    docker rm -f libz-testdb
}

docker run \
    --name libz-testdb \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=${DATABASE_PASSWORD} \
    -e MYSQL_USER=${DATABASE_USER} \
    -e MYSQL_PASSWORD=${DATABASE_PASSWORD} \
    -e MYSQL_DATABASE=${DATABASE_NAME} \
    -d mariadb:11.2.2-jammy
echo ready...
sleep 10
poetry run pytest
