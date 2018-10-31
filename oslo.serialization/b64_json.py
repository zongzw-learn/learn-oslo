from oslo_serialization import base64
from oslo_serialization import jsonutils

data = 'hello OSLO'

print(base64.encode_as_bytes(data))
print(base64.encode_as_text(data))

data = {
    'data': {
        'name': 'zong', 
        'fullname': 'andrew zong', 
        'score': 0, 
        'password': {
            'weak': '123456', 
            'strong': '******', 
            'passlen': [1, 2, 3, 4, 5]
        }
    }
}

with open("app.txt", 'w') as fw:
    jsonutils.dump(data, fw)

print(jsonutils.dumps(data))
print(jsonutils.dump_as_bytes(data))
print(jsonutils.to_primitive(data, convert_instances=True, max_depth=1, level=0))
