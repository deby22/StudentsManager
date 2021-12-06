# StudentsManager


## Instalation

Before running project you have to start postgres:

```bash
docker run --name postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```

Set flask enviroment variable

```bash
export FLASK_APP=run.py
```
 
 Next, create database

 ```bash
 python manage.py create_db
 ```