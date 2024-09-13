# Use the official Apache Airflow Docker image
FROM apache/airflow:2.4.3  # Specify the Airflow version

USER root

# Install additional packages if needed (e.g., MySQL or Postgres client)
RUN apt-get update && apt-get install -y \
    libmysqlclient-dev \
    && apt-get clean

USER airflow

# Copy DAGs into the container
COPY dags/ /opt/airflow/dags/

# Copy configuration files (if needed)
COPY config/airflow_config.yaml /opt/airflow/config/

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow

# Expose web server port
EXPOSE 8080

# Start the Airflow web server by default
ENTRYPOINT ["airflow", "webserver"]
