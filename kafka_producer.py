import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps

producer = KafkaProducer(
    bootstrap_servers=['54.89.24.2:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

df = pd.read_csv("data/indexProcessed.csv")
while True:
    record = df.sample(1).to_dict(orient="records")[0]
    producer.send('portfolioproject', value=record)
    sleep(1)
