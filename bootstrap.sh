#!/bin/bash
apt update
apt install python-pip -y

pip install docker-compose

curl -fsSL https://get.docker.com/ | sh
service docker start || systemctl start docker

mkdir -p /var/log/webhook

git clone https://github.com/scalr-tutorials/scalr-remote-var-webhook.git /opt/variable-webhook
