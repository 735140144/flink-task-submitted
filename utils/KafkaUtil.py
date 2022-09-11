"""
@function:
@parameter:
@attention:
"""
import json

from kafka import KafkaProducer


def kafkaConf():
    bootstrap_servers = ['172.16.0.101:9092', '172.16.0.102:9092', '172.16.0.103:9092']
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                             value_serializer=lambda m: json.dumps(m).encode("utf-8"))
    return producer


def sendKafka(topic, value):
    kafkaConf().send(topic, value)
    return