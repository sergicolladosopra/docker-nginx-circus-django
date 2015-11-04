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
