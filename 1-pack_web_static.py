#!/usr/bin/python3

""" A module that generates a .tgz archive """


from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""

    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    # Create the .tgz archive
    result = local("tar -czvf {} web_static".format(archive_name))

    # Check if the archive was created successfully
    if result.failed:
        return None

    return archive_name
