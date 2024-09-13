# Use the official Grafana image from Docker Hub
FROM grafana/grafana:latest

# Copy custom Grafana configuration
COPY grafana.ini /etc/grafana/grafana.ini

# Copy pre-configured dashboards
COPY dashboards/ /var/lib/grafana/dashboards/

# Expose Grafana port
EXPOSE 3000
