#!/bin/sh

echo "Checking for postgres setup confirmation ..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python server.py run -h 0.0.0.0
