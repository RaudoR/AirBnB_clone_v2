#!/usr/bin/python3
# '''script deply static'''

from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['34.74.25.201', '54.173.62.214']


def do_pack():
    '''Fabric script to compress files in web_static'''

    local("mkdir -p versions")
    ver = ti("%Y%m%d%H%M%S")
    arc = local("tar -cvzf versions/web_static_{}.tgz web_static".format(ver))

    if arc is None:
        return None
    else:
        return ("versions/web_static_{}".format(ver))


def do_deploy(archive_path):
    '''deploy static to servers'''
    if (os.path.isfile(archive_path) is False):
        return False
    path = archive_path.split('/')[1]
    target = "/data/web_static/releases/" + path
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(target))
        run("sudo tar -xzf /tmp/{} -C {}/".format(path, target))
        run("sudo rm /tmp/{}".format(path))
        run("sudo mv {}/web_static/* {}/".format(target, target))
        run("sudo rm -rf {}/web_static".format(target))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(target))
        print("New version deployed")
        return True
    except Exception:
        return False
