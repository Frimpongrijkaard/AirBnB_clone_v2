#!/usr/bin/python3
"""A fabric script that generate .tgz archive from the content web static"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """this function generate .tgz from the content of the web static"""
    date = datetime.now()
    archive = "web_static_{}{}{}{}{}{}.tgz".format(date.year,date.month,date.day,date.hour,date.minute,date.second)
    local("mkdir -p versions")
    result = local("tar -czvf versions/{} web_static/".format(archive))
    if result.failed:
        return None
    return "versions/{}".format(archive)
