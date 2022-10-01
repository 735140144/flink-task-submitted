"""
@function:
@parameter:
@attention:
"""
# 该kafka包为kafka-python 可以执行命令 pip install kafka-python
from kafka import KafkaConsumer


def kafkaConf():
    topic = "sub_user_2022"
    # 重新拿数据需要更改group_id的值
    group_id = "user_2022"
    bootstrap_servers = ['172.16.0.101:9092', '172.16.0.102:9092', '172.16.0.103:9092']
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, group_id=group_id,
                             auto_offset_reset='earliest', api_version=(2, 2, 1), enable_auto_commit=True,
                             auto_commit_interval_ms=1000)
    return consumer

def run():
    conf = kafkaConf()
    for msg in conf:
        print(msg.value.decode("utf-8"))


if __name__ == "__main__":
    run()
