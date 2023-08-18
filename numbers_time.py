from kafka import KafkaProducer 
import random
import json
import time

topic='PythonKafkaProducer'
producer = KafkaProducer(bootstrap_servers='kafka:9092')

def randomWithAnomaly(anomaly_prob, anomaly_factor):
    if random.random() < anomaly_prob:
        anomaly_value = random.random() * anomaly_factor
        return anomaly_value
    else:
        return random.random()
    
while True:
    value = randomWithAnomaly(0.02,3)
    data = {"fields": {
        "value": value
    },
    "name": "epic1",
    "tags": {
        "host": "Jaime"
    },
    "timestamp": time.time()
}
    
    js = json.dumps(data).encode('utf-8')
    producer.send(topic, js)
    producer.flush()
    time.sleep(1)
