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
https://kubernetes.io/docs/tasks/tools/install-kubectl/
```bash
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
Install VirtualBox:
```bash
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian `lsb_release -cs` contrib"
sudo apt update
sudo apt-get install virtualbox-5.2
```
Start the cluster:
```bash
minikube start
```
Configure the Minikube
```bash
kubectl config use-context minikube
eval $(minikube docker-env)
```
Build the Image
```bash
docker build -t bt-webserver:v1 .
```
Start the Deployment (Note the --image-pull-policy=Never flag makes kube look for local Images
```bash
kubectl run bt-webserver --image=bt-webserver:v1 --port=8080 --image-pull-policy=Never
```