# Instructions to pull Server container
# RabbitMQ Server for pulling Raspberry pi Bluetooth data from RabbitMQ queue 'bt_wardrive' at http://129.114.111.193:15672

# run these commands to start pulling data from RabbitMQ queue
service rabbitmq-server start
service mysql start
python3 /bluetooth_wardrive/ServerSetup/RabbitServer/RabbitMQ_receive.py

# modify RabbitMQ_receive.py with new sql_user: 'jaycryderman' and sql_password:  'mysql'
