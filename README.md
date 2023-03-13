# Steampipe with RESTful API

* why and what is this?
  * steampipe has no RestAPI support.
  * I need make some multi tenant environments.
  * and I need to test some... :)

# How to use
* mount /home/steampipe with configurations.

```
curl -X POST -L \
  localhost:5000/query \
  -d "q=select * from net_dns_record where domain = 'steampipe.io' and dns_server = '1.1.1.1:53';"

```

# Disclaimer
* use at your own risk

