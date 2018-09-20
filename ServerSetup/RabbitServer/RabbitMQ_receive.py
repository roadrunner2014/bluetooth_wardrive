# Name: simple_receive_and_send.py
# Written by: Richard Azille
#
# This program serves as a consumer-producer script for 
# receiving messages and returning them to the original 
# source using multiple connections and direct exchanges.
# 
# NOTE: Execute on RabbitMQ server (before running 
# simple_send.py

import pika

# Establish incoming connection
connection_in = pika.BlockingConnection(pika.ConnectionParameters(host="172.16.9.106"))
channel_in = connection_in.channel()
channel_in.exchange_declare(exchange='exchange_pi_to_mq',
                            exchange_type='direct')
result_in = channel_in.queue_declare(exclusive=True)
queue_in_name = result_in.method.queue
channel_in.queue_bind(exchange='exchange_pi_to_mq',
                      queue=queue_in_name,
                      routing_key='key_pi_to_mq')

# Establish outgoing connection 
connection_out = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel_out = connection_out.channel()
channel_out.exchange_declare(exchange='exchange_mq_to_pi',
                             exchange_type='direct')

# Document received message and publish to outgoing exchange
def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        channel_out.basic_publish(exchange='exchange_mq_to_pi',
                                  routing_key='key_mq_to_pi',
                                  body=body)
        print(" [x] Sent     %r" % body)

# Indicate queue readiness
print(' [*] Waiting for messages. To exit, press CTRL+C')

# Consumption configuration
channel_in.basic_consume(callback,
                         queue=queue_in_name,
                         no_ack=True)

# Begin consuming
channel_in.start_consuming()