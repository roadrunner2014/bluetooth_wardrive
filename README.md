# Dependencies for the bluetooth python library
sudo apt upgrade
sudo apt install python-pip python-dev ipython
sudo apt install bluetooth libbluetooth-dev

# To install Docker
sudo apt install docker

# To start the Rabbit image from scratch (RabbitMQ documentation)
docker run -d --hostname rabbit-server --name rabbit-image rabbitmq

# To attach to the docker instance
sudo docker exec -i -t <instance_name> /bin/bash

## MELVIN's Notes
IP ADDR (OpenStackOCI) 10.3.101.1 -- Will have a guide at a later time
Username: THarper
Password: abc123 

# Openstack notes:
* Will need to do an ssh-keygen and upload to the open stack to authenticate.
IPADDR (GitLab) 10.3.101.60
