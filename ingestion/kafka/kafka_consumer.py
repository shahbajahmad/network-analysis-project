from kafka import KafkaConsumer
import json
import yaml

def load_config(file_path):
    """
    Load the Kafka configuration from a YAML file.

    Args:
        file_path (str): The path to the YAML configuration file.

    Returns:
        dict: The loaded configuration as a dictionary.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def process_message(message):
    """
    Process the consumed message from Kafka.

    Args:
        message (dict): The message data consumed from Kafka.

    """
    # Here you can add the logic to process the message
    # For demonstration, we will just print the message
    print(f"Processing message: {message}")

def main():
    # Load Kafka configuration
    config = load_config('../config/kafka_config.yaml')

    # Set up the Kafka consumer
    consumer = KafkaConsumer(
        config['topic'],
        bootstrap_servers=config['bootstrap_servers'],
        auto_offset_reset='earliest',  # Start reading from the earliest available message
        enable_auto_commit=True,
        group_id='network-analysis-group',  # Consumer group id
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON messages
    )

    print("Kafka Consumer has started...")

    # Consume messages from the Kafka topic
    for message in consumer:
        print(f"Received message: {message.value}")
        process_message(message.value)

if __name__ == "__main__":
    main()
