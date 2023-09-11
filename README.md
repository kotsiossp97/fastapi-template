# FastAPI Template Using Docker
This is a template for creating an API using the python framework FastAPI.
It uses the following:

- MySQL Database
- phpMyAdmin
- FastAPI - Alembic - PyDantic

It creates three linked Docker containers, one for the FastAPI python code, one for MySQL Database and the last for phpMyAdmin.

All the configuration for the project is done through the `.env` file.

## Local Development
Development can be done before or after Docker app creation. If any changes are done after the containers are created, you should delete all existing images before running docker compose, to ensure that the code is copied inside the container and no cache is going on.

### Create new Tables / Models
To create new tables or models, firstly define the table model in the `app/models` directory. 

Use as a reference the existing `ACCOUNTS` table, in file `accounts.py`.

Make sure that the created class is imported accordingly in `app/db/base.py` file, so that alembic pick it up.

Then, create the schema for the table in `app/schemas` directory.

When you are ready, run in the fastapi_template directory:
```bash
alembic revision --autogenerate -m "Revision Comment"
```


## Starting the stack
To start the project, simply run 
```bash
docker compose up -d
```
in the project root directory. This will create all the required containers and after a while you should be able to access the API. The API is listening on port `5000` and phpMyAdmin on port `8080`. You can change the ports through the `compose.yml` file.

To check if everything is up, head to the documentation page
```
http://localhost:5000/docs
```