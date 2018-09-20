import ast
import bluetooth
from bs4 import BeautifulSoup
from datetime import datetime
import pika
from time import sleep
import urllib3


class BluetoothScanner:
    def __init__(self):

        print("Initializing bluetooth monitor client...")

        self.ip_addr = None
        self.location = None
        self.capture = None
        self.get_relative_location()

        print("Initial IP Address: {}".format(self.ip_addr))
        print("Initial Location: {}".format(self.location))

    class MonitorCapture:
        """Inner class used to store the capture data as an object"""

        def __init__(self, timestamp, structure, ip_addr, location):
            self.timestamp = timestamp
            self.mac_pairs = dict()
            self.ip_addr = ip_addr
            self.location = location
            # Given a tuple, create a dictionary of the bluetooth devices.
            for entry in structure:
                if isinstance(entry, tuple):
                    self.mac_pairs[entry[0]] = entry[1]

    def get_relative_location(self):
        """Using an ISP locator, get the location closest to the the client"""
        http = urllib3.PoolManager()
        url = 'http://ipinfo.io/json'
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data, features="html5lib")
        soup = str(soup).split("body")[1][1:-2]
        try:
            soup = ast.literal_eval(soup)
            self.ip_addr = soup['ip']
            self.location = soup['loc']
        except Exception as e:
            print("Approximate address can not be determined...")
            self.ip_addr = None
            self.location = None

    def scan_bluetooth(self):
        """Scan nearby bluetooth networks"""
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print("Found {} devices at {}".format(len(nearby_devices), datetime.now()))
        self.capture = self.MonitorCapture(timestamp=datetime.now(), structure=nearby_devices, ip_addr=self.ip_addr,
                                           location=self.location)
        for name, addr in nearby_devices:
            print(" %s - %s" % (addr, name))

    def transmit_to_server(self, server_addr, server_port):
        """Send the capture object to the RabbitMQ broker"""
        # If a server argument was not given then exit the program
        if not server_addr:
            exit()

        # Credentials: <Team Color> -- Test5423
        credentials = pika.PlainCredentials('orange', 'cloud5243')
        connection = pika.BlockingConnection(pika.ConnectionParameters(server_addr, server_port, '/', credentials))
        channel = connection.channel()
        channel.exchange_declare(exchange='exchange_pi_to_mq', exchange_type='direct')
        channel.queue_delare('bt_wardrive')
        # TODO: Serialize the capture into JSON format
        channel.basic_publish(exchange='exchange_pi_to_mq', routing_key='bt_wardrive', body=self.capture)


if __name__ == '__main__':
    btscanner = BluetoothScanner()
    try:
        while True:
            btscanner.scan_bluetooth()
            btscanner.transmit_to_server("172.16.9.106", "15672")
            sleep(60)
    except KeyboardInterrupt:
        print("\nExiting client script...")
        exit()
