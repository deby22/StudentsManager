# StudentsManager


## Instalation

Before running project you have to start postgres:

```bash
docker run --name postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```
 
 Next, create database

 ```bash
 python manage.py create_db
 ```