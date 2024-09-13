# Network Analysis Project

## Overview

The **Network Analysis Project** is a scalable, maintainable, and efficient data processing pipeline built to analyze network devices and generate comprehensive reports. It leverages modern data engineering technologies like Apache Kafka, Hadoop, Apache Spark, Flask, Apache Airflow, Prometheus, and Grafana to provide a robust architecture for data ingestion, storage, processing, delivery, orchestration, and monitoring.

The project is designed to simulate network performance, evaluate security, and generate network architecture proposals based on various network devices' data. This pipeline can be extended to accommodate more complex data workflows and integrations.

## Key Features

- **Data Ingestion**: Real-time data ingestion using Apache Kafka.
- **Data Storage**: Distributed storage of data using Hadoop HDFS.
- **Data Processing**: Batch processing of large datasets using Apache Spark.
- **Data Delivery**: RESTful API built with Flask to serve processed data.
- **Orchestration**: Workflow orchestration using Apache Airflow for scheduled and dependent tasks.
- **Monitoring**: Real-time monitoring and visualization using Prometheus and Grafana.
- **Security Evaluation**: Dynamic security scoring and report generation for network devices.

## Architecture

The architecture of this project is composed of several microservices and components that work together to achieve the project's goals:

1. **Ingestion Layer**: Apache Kafka to ingest data streams.
2. **Storage Layer**: Hadoop HDFS for scalable and reliable data storage.
3. **Processing Layer**: Apache Spark for data transformation and aggregation.
4. **Delivery Layer**: Flask API for data delivery to consumers.
5. **Orchestration Layer**: Apache Airflow for scheduling and managing workflows.
6. **Monitoring Layer**: Prometheus for metrics collection and Grafana for visualization.

## Prerequisites

- Docker and Docker Compose installed on your system.
- Python 3.8+ installed.
- Basic understanding of Docker, data engineering, and Python programming.

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/network-analysis-project.git
cd network-analysis-project

This command will build all Docker images and start the containers for Kafka, Hadoop, Spark, Flask, Airflow, Prometheus, and Grafana.

3. Access the Services
Once all services are up and running, you can access them through the following URLs:

Kafka (for ingestion): localhost:9092
Hadoop Namenode (for storage management): http://localhost:50070
Spark Master (for job monitoring): http://localhost:8080
Flask API (for data delivery): http://localhost:5000
Airflow UI (for workflow management): http://localhost:8081
Prometheus (for monitoring metrics): http://localhost:9090
Grafana (for visualizations): http://localhost:3000
4. Working with the Services

Data Ingestion: Data can be ingested into Kafka topics using the Kafka producer provided in ingestion/kafka/kafka_producer.py. Modify the script or use the Kafka command-line tools to push data.

Data Storage: Hadoop HDFS will store ingested data. Use the upload_to_hdfs.py script located in storage/scripts to upload data to HDFS.

Data Processing: The Spark job defined in processing/spark/spark_job.py will process data from HDFS. It can be executed as part of the Airflow DAG or independently.

Data Delivery: The Flask API (app.py in delivery/api) exposes endpoints to deliver processed data. You can interact with the API using curl or any HTTP client.

Orchestration: Apache Airflow orchestrates the entire pipeline. The DAG file located at orchestration/airflow/dags/data_pipeline_dag.py defines the workflow. Use the Airflow UI to trigger or schedule jobs.

Monitoring and Visualization: Prometheus collects metrics, and Grafana provides a dashboard to visualize these metrics. Default dashboards are included in monitoring/grafana/dashboards.

5. Generate Reports
The analysis folder contains scripts for generating various reports:

Network Analysis: Run network_analysis.py to simulate network performance and generate a performance report.
Security Evaluation: Use security_evaluation.py to evaluate network devices' security and generate a security report.
Proposal Generation: proposal_generator.py generates a comprehensive network architecture proposal based on device data, performance, and security evaluation.
6. Configurations
Each service has its own configuration file located in the respective config directories:

Kafka: ingestion/config/kafka_config.yaml
Spark: processing/config/spark_config.yaml
Airflow: orchestration/config/airflow_config.yaml
Flask API: delivery/config/api_config.yaml
Prometheus: monitoring/prometheus/prometheus.yml
Grafana: monitoring/grafana/grafana.ini
Modify these configuration files as needed to adjust service parameters.
