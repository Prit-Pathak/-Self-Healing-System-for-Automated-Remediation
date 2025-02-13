# Set up a Kafka topic to receive alerts from Prometheus/Nagios.

# Create Kafka topic
kafka-topics.sh --create --topic system_alerts --bootstrap-server localhost:9092