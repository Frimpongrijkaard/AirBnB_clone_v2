#!/usr/bin/env bash
# This file set-up my web servers for my deployment of web static

if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get install nginx 
fi
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo touch /data/web_static/releases/test/index.html
echo "<html>
<head>
<title>test page</title>
</head>
<body>
Holberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu: ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
