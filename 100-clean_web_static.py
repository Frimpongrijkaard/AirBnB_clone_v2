#!/usr/bin/python3
from fabric.api import env, run, local, lcd
from datetime import datetime
from os.path import exists


env.hosts = ['52.91.144.93', '54.236.41.73']
def do_clean(number=0):
    """Delete out-of-date archives."""
    number = int(number)
    if number < 1:
        number = 1

    try:
        with lcd("versions"):
            archives = local("ls -1t", capture=True).split("\n")
            if len(archives) <= number:
                return
            remove_count = len(archives) - number
            for i in range(remove_count):
                local("rm {}".format(archives[i]))
        releases = run("ls -1t /data/web_static/releases").split("\n")
        if len(releases) <= number:
            return
        for i in range(remove_count):
            release_path = "/data/web_static/releases/{}".format(releases[i])
            run("rm -rf {}".format(release_path))
    except Exception as e:
        return False
