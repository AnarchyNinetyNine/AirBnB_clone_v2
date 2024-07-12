#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Update package list and install Nginx if it is not already installed
apt update
apt install -y nginx

# Create necessary directories if they do not exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file to test the Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link, force delete if it already exists
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
	alias /data/web_static/current;
	index index.html index.htm;
    }

    location /redirect_me {
	return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# Restart Nginx to apply the new configuration
service nginx restart

