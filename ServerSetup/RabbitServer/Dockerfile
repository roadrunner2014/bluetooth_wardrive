# Get the latest rabbitMQ image
FROM rabbitmq:latest

# Make the project directory and copy the python script into the directory
RUN mkdir /rabbit-server
COPY RabbitMQ_receive.py /rabbit-server

# Install python3 and the pika dependency
RUN apt update && apt install -y python3 python3-dev python3-pip
RUN pip3 install pika

# Start the python script as a background process
#RUN python3 /rabbit-server/RabbitMQ_receive.py