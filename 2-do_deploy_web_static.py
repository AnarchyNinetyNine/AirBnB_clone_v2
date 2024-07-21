#!/usr/bin/python3

""" Module for Deploying Archive """

from fabric.api import env, put, run, sudo
import os

# Define the IPs of the web servers
env.hosts = ['web-01.bloodlink.tech', 'web-02.bloodlink.tech']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): The path to the archive to distribute.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract archive filename and name without extension
        archive_filename = os.path.basename(archive_path)
        archive_name = archive_filename.split('.')[0]

        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Create the target directory on the web server using sudo
        sudo("mkdir -p /data/web_static/releases/{}/".format(archive_name))

        # Uncompress the archive to the target directory
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_filename, archive_name))

        # Delete the archive from the web server
        sudo("rm /tmp/{}".format(archive_filename))

        # Move the contents to the proper directory
        sudo(f"rm -rf /data/web_static/releases/{archive_name}/web_static")

        # Delete the existing symbolic link
        sudo("rm -rf /data/web_static/current")

        # Create a new symbolic link to the new version
        path = "/data/web_static/releases/"
        sudo(f"ln -s {path}{archive_name}/ /data/web_static/current")

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
