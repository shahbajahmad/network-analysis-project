from kafka import KafkaProducer
import json
import yaml

# Load Kafka configuration
with open('../config/kafka_config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

producer = KafkaProducer(bootstrap_servers=config['bootstrap_servers'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def produce_data():
    data = {"name": "Cisco ISR 4431", "type": "Router", "cost": 2500}
    producer.send(config['topic'], value=data)
    print(f"Sent: {data}")

if __name__ == "__main__":
    produce_data()
