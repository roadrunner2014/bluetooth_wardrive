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
```

*Alternatively, you can use:*
```sudo easy_install sqlalchemy```

# Check that the service is running
systemctl status mysql.service

```

# Misc Notes (Not project specific)
## To install Docker & Docker Compose
```bash
sudo apt install docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## To start the Rabbit image from scratch (RabbitMQ documentation)
```bash
docker run -d --hostname rabbit-server --name rabbit-image rabbitmq
```

## To attach to the docker instance
```bash
sudo docker exec -i -t <instance_name> /bin/bash
```

## Docker-Compose
```bash
cd ./ServerSetup/DjangoServer/
docker-compose build
# Initial container start
docker-compose up -d
# Stopping a container
docker-compose stop
# Restarting a container
docker-compose start
```

*Openstack notes: Will need to do an ssh-keygen and upload to the open stack to authenticate.*

# Setting up Kubernetes on Minikube

Install kubectl:
```bash
https://kubernetes.io/docs/tasks/tools/install-kubectl/
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo touch /etc/apt/sources.list.d/kubernetes.list
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl
```
Install minikube:
```bash
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.8.0/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```
Start the cluster:
```bash
minikube start
```

Link to run a django kube --> https://medium.com/google-cloud/deploying-django-postgres-redis-containers-to-kubernetes-9ee28e7a146

Install docker-machine:
```bash
base=https://github.com/docker/machine/releases/download/v0.14.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
  sudo install /tmp/docker-machine /usr/local/bin/docker-machine
```

Initialize the docker-machine (Note: This may not be necessary for Linux)
```bash
docker-machine create --driver virtualbox default
```

Confirm that docker-machine is working correctly
```bash
docker-machine start dev
eval $(docker-machine env dev)
```