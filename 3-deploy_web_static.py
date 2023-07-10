#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['52.91.144.93', '54.236.41.73']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'

def do_pack():
    """this function generate .tgz from the content of the web static"""
    date = datetime.now()
    archive = "web_static_{}{}{}{}{}{}.tgz".format(date.year,date.month,date.day,date.hour,date.minute,date.second)
    local("mkdir -p versions")
    result = local("tar -czvf versions/{} web_static/".format(archive))
    if result.failed:
        return None
    return "versions/{}".format(archive)

def do_deploy(archive_path):
    """ this function distribute acrhive to your web server"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        arch_file = archive_path.aplit("/")[-1]
        folder = arch_file.split(".")[0]
        release_path = "/data/web_static/releases/{}".format(folder)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(arch_file, release_path))
        run("rm -rf /tmp/{}".format(arch_file))
        run("mv {}/web_static/* {}/".format(release_path, release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        return True

    except Exception as e:
        return False

def deploy():
    """distributes an archive to your web servers, using the function deploy"""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
