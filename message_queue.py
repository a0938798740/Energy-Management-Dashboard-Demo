import pika
import os

class MessageQueue:
    """
    Wrapper for RabbitMQ interactions using Pika.
    Handles connection setup and message publishing.
    """
    
    def __init__(self, url):
        self.url = url
        self.params = pika.URLParameters(url)

    def get_connection(self):
        return pika.BlockingConnection(self.params)

    def publish_task(self, queue_name, message):
        """
        Publishes a message to the specified queue.
        """
        connection = None
        try:
            connection = self.get_connection()
            channel = connection.channel()
            channel.queue_declare(queue=queue_name, durable=True)
            
            channel.basic_publish(
                exchange='',
                routing_key=queue_name,
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # Make message persistent
                )
            )
            print(f" [x] Sent '{message}' to {queue_name}")
            return True
            
        except Exception as e:
            print(f"MQ Error: {e}")
            return False
            
        finally:
            if connection:
                connection.close()
