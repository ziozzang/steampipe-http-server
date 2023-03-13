#!/bin/sh
steampipe service start &
# wait for steampipe to start
while ! steampipe service status | grep -q "Connection"; do sleep 1; done
# get the password
#steampipe service status --show-password | grep Connection | awk '{print $3}' | xargs -I {} echo "export STEAMPIPE_DB_PASSWORD={}" >> ~/.xonshrc
# Run Server
python3 /opt/server.py
