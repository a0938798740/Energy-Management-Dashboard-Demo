# Configuration settings for the Flask Application

# Database Connection String
# Format: mysql+pymysql://user:password@host/dbname
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/energy_db'

# RabbitMQ Connection String
# Format: amqp://user:password@host:port/vhost
CLOUDAMQP_URL = 'amqp://guest:guest@localhost:5672/%2f'

# Application Secret Key (for session security)
SECRET_KEY = 'YOUR_SECRET_KEY_HERE'
