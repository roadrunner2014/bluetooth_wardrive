import time

import pika


class RabbitConsumer:
    def __init__(self, rabbit_server_addr, rabbit_server_port):
        # Establish incoming connection
        credentials = pika.PlainCredentials('orange', 'test5243')
        connection_params = pika.ConnectionParameters(host=rabbit_server_addr, port=rabbit_server_port,
                                                      virtual_host='/', credentials=credentials)
        connection = pika.BlockingConnection(connection_params)
        self.channel_in = connection.channel()
        self.channel_in.queue_declare(queue='bt_wardrive', durable=True)
        self.channel_in.exchange_declare(exchange='bt_wardrive', exchange_type='direct')

    # Document received message and publish to outgoing exchange
    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    server_addr = "129.114.111.193"
    port = 5672
    consumer = RabbitConsumer(rabbit_server_addr=server_addr, rabbit_server_port=port)
    try:
        print(' [*] Waiting for messages. To exit, press CTRL+C')
        consumer.channel_in.basic_consume(consumer.callback, queue='bt_wardrive')
        consumer.channel_in.start_consuming()
    except KeyboardInterrupt:
        print("\nExiting consumer script...")
        exit()
