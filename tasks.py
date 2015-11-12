from invoke import task, run


@task
def runserver(image="djangorest"):
    env = '-e DJANGO_SETTINGS_MODULE="app.settings.dev"'
    command = "docker run -ti -v $PWD/app:/opt/app {env} --net=host {image}".format(image=image, env=env)
    print('exe: ',command)
    run(command)

@task
def runbash(image="djangorest"):
    env = '-e DJANGO_SETTINGS_MODULE="app.settings.dev"'
    command = "docker run -ti -v $PWD/app:/opt/app {env} --net=host {image} /bin/bash".format(image=image, env=env)
    print('exe: ',command)
    run(command)

@task
def runtests(image="djangorest"):
    command = "docker run -ti -v $PWD/app:/opt/app --net=host {image} /code/docker/run_tests.sh ".format(image=image)
    print('exe: ',command)
    run(command)


