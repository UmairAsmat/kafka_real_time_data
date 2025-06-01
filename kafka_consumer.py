from kafka import KafkaConsumer
from json import loads
import json
import boto3
from datetime import datetime

consumer = KafkaConsumer(
    'portfolioproject',
    bootstrap_servers=['54.89.24.2:9092'],
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

s3 = boto3.client('s3')
bucket_name = 'portfolio-project-data'

for count, message in enumerate(consumer):
    data = message.value
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S')
    key = f'stock_market/record_{timestamp}_{count}.json'
    s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data))
