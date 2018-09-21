# Setting up the Bluetooth Scanner Client
## Dependencies
```bash
sudo apt upgrade
sudo apt install python3-pip python3-dev ipython
sudo apt install bluetooth libbluetooth-dev
pip3 install pybluez pika
```

## Running the client
```bash
python3 ./ClientSetup/bluetooth_monitor.py

```

# Consumer Setup
```bash
sudo apt-get install python3-dev libmysqlclient-dev mysql-server
sudo pip3 install pymysql sqlalchemy
mysql_secure_installation

# Check that the service is running
systemctl status mysql.service

```

# Misc Notes (Not project specific)
## To install Docker
```bash
sudo apt install docker
```

## To start the Rabbit image from scratch (RabbitMQ documentation)
```bash
docker run -d --hostname rabbit-server --name rabbit-image rabbitmq
```

## To attach to the docker instance
```bash
sudo docker exec -i -t <instance_name> /bin/bash
```

*Openstack notes: Will need to do an ssh-keygen and upload to the open stack to authenticate.*