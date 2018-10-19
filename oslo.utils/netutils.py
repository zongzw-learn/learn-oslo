from oslo_utils import netutils

print(netutils.escape_ipv6('fe80::f493:20ff:fe5b:6cf'))

print(netutils.get_ipv6_addr_by_EUI64('fe80::d480:b0ff:fe33:1543/64', 'f2:2c:d8:c3:73:fb'))

print(netutils.get_my_ipv4())

print(netutils.is_ipv6_enabled())

print(netutils.is_valid_cidr('10.10.10.10/24'))

code_list = []
for n in range(-5, 5):
    code_list.append(netutils.is_valid_icmp_code(n))
print(code_list)

print(netutils.urlsplit('https://foxfox.mybluemix.net.com:8443/index.html?auto=off'))
# SplitResult(scheme='https', netloc='foxfox.mybluemix.net.com:8443', path='/index.html', query='auto=off', fragment='')