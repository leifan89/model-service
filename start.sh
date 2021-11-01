#!/bin/bash

echo "Sleeping 20 seconds before starting Flask to wait for DB to be ready"
sleep 20
echo "Starting Flask"
flask run --no-reload --host=0.0.0.0
