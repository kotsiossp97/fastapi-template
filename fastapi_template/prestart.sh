#! /usr/bin/env bash

# Let the DB start
python /fastapi/app/pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python /fastapi/app/initial_data.py
