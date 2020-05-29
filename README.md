# News_board API

This API provides the ability to receive, publish, modify and delete posts and comments to these posts.
You can try to use it here: [News board API](http://134.122.114.146:8000/api/v1/news_posts/posts/ "News Board").

Also, you can find the whole documentation of API here: [Documentation](https://web.postman.co/collections/10954999-e7f1b9de-b52c-4e99-97e7-3d8f30c5fd7e?version=latest&workspace=40909c67-9842-465d-843f-367334184f57#c812fcc9-c719-438a-b46b-fe5a6c9df0f6 "API's documentation")

### Installation for launching a project **`News_board`**
##### - Python
```
$ python3 --version or $ python3 -V
$ sudo apt-get update
$ sudo apt-get install python3
$ sudo apt-get install -y python3-venv
```
##### - Docker
```
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
$ sudo apt update
$ apt-cache policy docker-ce
$ sudo apt install docker-ce

  Executing the Docker commands without sudo (Optional):
$ sudo usermod -aG docker ${USER}
$ su - ${USER}
$ id -nG
$ sudo usermod -aG docker *username*
```
##### - Docker-compose

```
$ sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```

### Creating a folder for the project

```
$ mkdir project
$ cd project
$ mkdir run
```

### Cloning project

```
git clone https://github.com/Zencrazycat/news_board.git
        # Clone with HTTPS
OR

git clone git@github.com:Zencrazycat/news_board.git
        # Clone with SSH
```

### Creation of **`virtual environment`** and launch

```
$ python3.6 -m venv env
$ source env/bin/activate
```

### Installing **`dependency`** packages

```
$ pip install -r requirements.txt
```

### Add .env file in root directory with your environment variables for Django, Docker, PostreSQL and RabbitMQ

Example:
```
SERVER=dev  # or prod
COMPOSE_FILE=docker-compose.yml
WSGI_PORT=8000
DOCKER_BUILD=0.0.1

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

RABBITMQ_VERSION=3.8-rc-management
RABBITMQ_DEFAULT_HOST=rabbitmq
RABBITMQ_DEFAULT_PORT=5672
RABBITMQ_DEFAULT_USER=guest
RABBITMQ_DEFAULT_PASS=123456qwerty
```

#### You can also add settings_local.py in project/src/news_board/ with some settings, like DEBUG, SECRET_KEY etc

### Launch and building a project in docker containers

```
$ docker-compose up -d
```
#### Data migrations
```
$ docker exec -it api python src/manage.py makemigrations
$ docker exec -it api python src/manage.py migrate
```

### Congratulations!
