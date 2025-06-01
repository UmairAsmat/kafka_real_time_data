# Stock Market Data Engineering Project with Kafka and AWS

A real-time stock market data engineering project that demonstrates the implementation of a complete data pipeline using Apache Kafka and various AWS services. The project simulates real-time stock data streaming and implements a scalable data lake architecture.

## 🏗️ Architecture

![Architecture](https://raw.githubusercontent.com/username/stock-market-kafka-data-engineering/main/architecture.png)

The project utilizes the following technologies:
- Apache Kafka (Producer/Consumer) on EC2
- Amazon S3 (Data Lake Storage)
- AWS Glue (Metadata & ETL)
- AWS Athena (SQL-based Serverless Querying)

## 🚀 Project Components

### 1. Kafka Setup on EC2

#### Prerequisites
- Java 8
- Apache Kafka 3.7.0
- Amazon EC2 instance (Amazon Linux 2)

#### Installation Steps
```bash
# Install Java
java -version
sudo yum install java-1.8.0-openjdk
java -version

# Download and Setup Kafka
wget https://archive.apache.org/dist/kafka/3.7.0/kafka_2.13-3.7.0.tgz
tar -xvf kafka_2.13-3.7.0.tgz
cd kafka_2.13-3.7.0
```

#### Configuration
1. Update `server.properties`:
```properties
listeners=PLAINTEXT://0.0.0.0:9092
advertised.listeners=PLAINTEXT://<YOUR-EC2-PUBLIC-IP>:9092
```

2. Configure EC2 Security Group:
- SSH (TCP/22)
- Kafka (TCP/9092)
- Zookeeper (TCP/2181)

#### Start Services
```bash
# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka (in a new terminal)
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
bin/kafka-server-start.sh config/server.properties

# Create Kafka Topic
bin/kafka-topics.sh --create --topic portfolioproject --bootstrap-server <YOUR-EC2-PUBLIC-IP>:9092 --replication-factor 1 --partitions 1
```

### 2. Python Implementation

#### Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

#### Files Structure
- `kafka_producer.py`: Streams stock data to Kafka topic
- `kafka_consumer.py`: Consumes data and writes to S3
- `data_uploader.py`: Direct CSV upload to S3

### 3. AWS Configuration

#### S3 Setup
- Create bucket: `portfolio-project-data`
- Configure appropriate IAM roles and policies

#### AWS Glue
1. Create Crawler:
   - Name: `portfolio-index-crawler`
   - Database: `portfolio_project_db`
   - Target path: `s3://portfolio-project-data/raw/index/`

2. Run crawler to create table schema

#### Athena Queries
```sql
SELECT * FROM portfolio_project_db.indexprocessed_csv LIMIT 10;
```

## 📦 Requirements

```
kafka-python==2.2.10
boto3==1.38.27
pandas
python-dateutil
```

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/username/stock-market-kafka-data-engineering.git
cd stock-market-kafka-data-engineering
```

2. Set up virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure AWS credentials:
```bash
aws configure
```

4. Update configuration files with your AWS and Kafka settings

5. Run the pipeline:
```bash
# Start producer
python kafka_producer.py

# In another terminal, start consumer
python kafka_consumer.py
```

## 🔑 Environment Variables

Create a `.env` file with:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region
KAFKA_BOOTSTRAP_SERVERS=your_ec2_public_ip:9092
```

## 🏆 Skills Demonstrated

- Cloud DevOps & Automation
- Data Engineering
- AWS Data Lake Architecture
- Serverless ETL
- Big Data Analytics
- IAM & Security Best Practices

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](issues).

## 👨‍💻 Author

Your Name
- LinkedIn: [Your LinkedIn]()
- Portfolio: [Your Portfolio]()

## 🙏 Acknowledgments

- EduQual Level 6 Diploma in AIOps
- AWS Documentation
- Apache Kafka Documentation 