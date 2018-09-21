import time
import pika
import pymysql


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

    # Document received message
    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # TODO: Rewrite this section using SQLAlchemy
    def create_database(self, sqlhost, sqluser, sqlpasswd): # passwd: mysql
        conn = pymysql.connect(host=sqlhost, user=sqluser, password=sqlpasswd)
        cursor = conn.cursor()

        # If the database already is on the system, delete it
        if cursor.execute('SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA where SCHEMA_NAME = "wardrive"'):
            cursor.close()
            self.deconstruct_database(sqlhost=sqlhost, sqluser=sqluser, sqlpasswd=sqlpasswd)
            # Restore the cursor
            conn = pymysql.connect(host=sqlhost, user=sqluser, password=sqlpasswd)
            cursor = conn.cursor()

        # Create a fresh database
        cursor.execute('CREATE DATABASE wardrive')

        # Create the table
        conn.cursor().execute('USE wardrive')
        conn.cursor().execute('CREATE TABLE bluetooth(capture_time varchar(32), location varchar(32),'
                              ' ip_addr varchar(32), mac_addr varchar(32), ssid varchar(64))')

    @staticmethod
    def deconstruct_database(sqlhost, sqluser, sqlpasswd):
        # TODO: Refactor this to be more class-oriented
        print('Removing database...')
        conn = pymysql.connect(host=sqlhost, user=sqluser, password=sqlpasswd)
        cursor = conn.cursor()
        cursor.execute('DROP DATABASE wardrive')
        cursor.close()


if __name__ == '__main__':
    server_addr = "129.114.111.193"
    port = 5672
    sql_host = '127.0.0.1'
    sql_user = 'root'
    sql_password = 'mysql'
    consumer = RabbitConsumer(rabbit_server_addr=server_addr, rabbit_server_port=port)
    consumer.create_database(sqlhost=sql_host, sqluser=sql_user, sqlpasswd=sql_password)
    try:
        print(' [*] Waiting for messages. To exit, press CTRL+C')
        consumer.channel_in.basic_consume(consumer.callback, queue='bt_wardrive')
        consumer.channel_in.start_consuming()
    except KeyboardInterrupt:
        print("\nCleaning consumer script...")
        consumer.deconstruct_database(sqlhost=sql_host, sqluser=sql_user, sqlpasswd=sql_password)
        print("\nExiting consumer script...")
        exit()
