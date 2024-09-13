# Use the official Prometheus image from Docker Hub
FROM prom/prometheus:latest

# Copy the Prometheus configuration file into the container
COPY prometheus.yml /etc/prometheus/prometheus.yml

# Expose Prometheus port
EXPOSE 9090

# Start Prometheus
CMD ["--config.file=/etc/prometheus/prometheus.yml"]
