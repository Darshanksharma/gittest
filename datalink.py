import dns.resolver
import dns.reversename
x = True
y = False
f= open("ip.txt","r").rstrip("\n\r"
for ip in f:

    try:
        qname = dns.reversename.from_address(ip)  # www.google.com for me
        answer = dns.resolver.query(qname,'PTR')
        print(answer)
        w = x
        print(x)
    except:
        w = y
        print(y)