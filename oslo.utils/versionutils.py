from oslo_utils import versionutils

print(versionutils.convert_version_to_int('9.6.6'))
print(versionutils.convert_version_to_str(9007000)) # every 3 bits is a number.
print(versionutils.convert_version_to_str(90070000))
print(versionutils.convert_version_to_tuple('9.7.0'))

print(versionutils.is_compatible('9.6.6', '9.7.0', same_major=True))