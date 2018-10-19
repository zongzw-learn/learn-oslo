from oslo_utils import dictutils

d = {'name': "Andrew Zong", 'age': 50, 'company': 'f5networks', 'family': {'wife': 'annie', 'kids': ['sally']}}
generator = dictutils.flatten_dict_to_keypairs(d, '.')

print(list(generator))
'''
[('age', 50), ('company', 'f5networks'), ('family.kids', ['sally']), ('family.wife', 'annie'), ('name', 'Andrew Zong')]
'''