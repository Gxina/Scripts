#----------------------------------------------------
#					Script par : Rose
#					Le : 20/05/2019
#----------------------------------------------------

#!/usr/bin/python3

import sys
import docker
client = docker.from_env()
def run():
    client.containers.run(image="dns", name="dns")
    client.containers.run(image="apache", name="apache2")
    client.conatiners.run(image="ftp", name="ftp")
    client.containers.run(image="httpd", name="httpd")
    client.containers.run(image="mysql:5.6.40", name="mysql")



def get(name):

    client.containers.get(image="dns", name='dns')
    client.containers.get(image="apache", name='apache2')
    client.containers.get(image="ftp", name='ftp')
    client.containers.get(image="httpd", name='httpd')
    client.containers.get(image="mysql:5.6.40", name='mysql')

run()

if len(sys.argv) == 2 :

    if sys.argv[1] == "start" :
        var = get(mysql)
        var.start()
        print("Start success")

    if sys.argv[1] == "stop" :
        var = get()
        var.stop()
        print("Stop success")

    if sys.argv[1] == "restart" :
        var = get()
        var.restart()
        print("Restart success")

    if sys.argv[1] == "rm" :
        var = get()
        var.remove()
        print("rm success")

    if sys.argv[1] == "run" :
        var = get()
        var.run()
        print("run de l'image")
else:

    print("Veillez entrer au moins 1 argument:'run'; 'start';'stop';'restart';'rm'")
