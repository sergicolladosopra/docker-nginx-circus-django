from invoke import task, run


@task
def runserver(image="djangorest"):
    env = '-e DJANGO_SETTINGS_MODULE=app.settings.dev'
    command = "docker run -ti -v $PWD/app:/opt/app {env} --net=host {image}".format(image=image, env=env)
    print('exe: ',command)
    run(command)
