# docker-nginx-circus-django
docker-nginx-circus-django with python3



## build image:

    git clone https://github.com/sergicolladosopra/docker-nginx-circus-django.git dockerDjango
    cd dockerDjango
    docker build -t django .

## run image:

    #run as daemon
    docker run -d -v $PWD/app:/opt/app  --net=host djangorest
    #run as temporal interactive terminal
    docker run -ti -v $PWD/app:/opt/app  --net=host djangorest


## ports

    8000    #nginx -> circus -> django
    9999    #circus -> django

## run to dev

    mkvirtualenv yourEnv
    workon yourEnv
    pip install pip-tools
    cd requirements
    pip-sync common.txt dev.txt

    invoke runserver


## authentication token

Get token:

    curl --data "username=anUsername&password=aPassword" -i -X POST http://127.0.0.1/api-token-auth/

    {token' : '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' }


add token to next  request:

    Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

    curl -i -H "Authorization:token 747b645c91dd181ab21baf496238bdf7ad629cd0" -X
    GET http://127.0.0.1/users/
