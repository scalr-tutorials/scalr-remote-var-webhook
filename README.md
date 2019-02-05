# Global Variables demo webhook

This webhook is used to give an exmpamle of how to use the a remote source for GV in Scalr.


# Instance setup.
Execute "bootstrap.sh" on the target install

This will install docker and pull down the variable-webhook repo.

# Variables File
This will by default read the example.json file to provide information to the GV.  You can change this file in the uwsgi.ini file as shown below.

# Update the uwsgi.ini file with your settings

```ini
[uwsgi]
chdir = /opt/variable-webhook
http-socket = 0.0.0.0:5018
wsgi-file = webhook.py
callable = app
workers = 1
master = true
plugin = python
env = SCALR_SIGNING_KEY=scalr_signing_key
env = SCALR_WEBHOOK=variable  # name of the webhook endpiont ex) "variable2" so your full endpiont in scalr would be "http:/xxx:5018/variable2"
env = SCALR_JSONFILE=example.json
# used if you want to use a mysql DB connection
env = SCALR_MYSQL_SERVER=mysql
env = SCALR_MYSQL_USER=root
env = SCALR_MYSQL_PASS=password
env = SCALR_MYSQL_DB=test
env = SCALR_TTL=10
env = SCALR_QUERY=SELECT * FROM variables
```

# Base installation
curl -L https://raw.githubusercontent.com/scalr-tutorials/scalr-remote-var-webhook/master/bootstrap.sh | bash

# Launch
execute 'relaunch.sh'
