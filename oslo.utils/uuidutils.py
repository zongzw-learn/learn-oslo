from oslo_utils import uuidutils

uuid1 = uuidutils.generate_uuid()
uuid2 = uuidutils.generate_uuid(dashed=False)

print(uuid1, uuid2)

print(uuidutils.is_uuid_like(uuid1), uuidutils.is_uuid_like(uuid2))
