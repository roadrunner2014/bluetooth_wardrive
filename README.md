# Dependencies for the bluetooth python library
sudo apt upgrade
sudo apt install python3-pip python3-dev ipython
sudo apt install bluetooth libbluetooth-dev
pip3 install pybluez pika

# To install Docker
sudo apt install docker

# To start the Rabbit image from scratch (RabbitMQ documentation)
docker run -d --hostname rabbit-server --name rabbit-image rabbitmq

# To attach to the docker instance
sudo docker exec -i -t <instance_name> /bin/bash

# Openstack notes:
* Will need to do an ssh-keygen and upload to the open stack to authenticate.