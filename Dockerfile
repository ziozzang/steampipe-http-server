FROM turbot/steampipe

RUN steampipe plugin install net theapsgroup/vsphere kubernetes prometheus jira theapsgroup/gitlab docker ellisvalentiner/confluence csv config theapsgroup/vault ldap theapsgroup/keycloak trivy jira grafana

#EXPOSE 9194
#EXPOSE 5000
user 0
COPY bootstrap.sh /
RUN apt update -y && \
    apt install -y python3-postgresql python3-psycopg2 python3-flask-restful python3-requests python3-bs4 \
        vim xonsh curl && \
    rm -rf /var/lib/apt/lists/* && \
	chmod 755 /bootstrap.sh

COPY server.py /opt/
user 9193
ENTRYPOINT ["/bin/sh", "/bootstrap.sh"]
