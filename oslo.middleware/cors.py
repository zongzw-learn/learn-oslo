
'''
OpenStack supports Cross-Origin Resource Sharing (CORS), 
a W3C specification defining a contract by which 
the single-origin policy of a user agent (usually a browser) 
may be relaxed. 
It permits the javascript engine to access an API that 
does not reside on the same domain, protocol, or port.
'''


'''
Manually construct a CORS request
curl -I -X OPTIONS https://api.example.com/api -H "Origin: https://ui.example.com"

'''
