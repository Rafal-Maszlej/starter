# starter

### Features
* Endpoints
  * [localhost:8080](http://localhost:8080/) - React app
  * [localhost:8080/admin](http://localhost:8080/admin) - Admin panel
  * [localhost:8080/api/](http://localhost:8080/api/) - API root
  * [localhost:8080/api/jwt/](http://localhost:8080/api/jwt/) - JWT endpoints
* Automatic converting `CamelCase` <-> `snake_case` in requests between frontend and backend  
* Custom `User` model

### How to
#### Create `.env` file  
```.env
SECRET_KEY=
DEBUG=True

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

#### Prepare project  
Create `.env` file in the root folder  
```shell script
make build
```

#### Start project  
```shell script
make up
```

#### Close project  
```shell script
ctrl + c
make down
```

#### Create admin user  
```shell script
make shell
./manage.py createsuperuser
```
