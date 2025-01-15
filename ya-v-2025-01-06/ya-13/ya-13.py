from ipaddress import *

net = ip_network('212.192.32.96/255.255.255.224')
c=0
for ip in net:
  ip2:str=bin(int(ip))[-8:]
  ip2.count('111')
  if ip2.find('111') < 0 and ip2.find('000') < 0:
    print(ip2, '----', ip2[-4:])
    c +=1
print(c)