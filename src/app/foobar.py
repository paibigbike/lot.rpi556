# Copyright (C) 2022 Chatpon

"""



"""

__author__ = "Chatpon Chaimongkol"

# standard Libraries
from datetime import datetime
import json


print(datetime.now().strftime('%Y-%m-%d %H %M %S'))

data = {'datetime': '2023-02-08 10:50:18',
        'device': 'device 2',
        'temperature': 30}
# {} - curly brackets [] - square brackets

print(data)
print(type(data))
print(data.keys())
for key in data.keys():
    print(f"key: {key}, value: {data[key]} ")

mqtt_data = json.dump(data)
print(f"mqtt_data: {mqtt_data}")
print(type(mqtt_data))