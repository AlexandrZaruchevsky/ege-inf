from ipaddress import ip_network
c=0
net = ip_network('95.112.224.0/255.255.255.128')
for ip in net:
  ip_b = bin(int(ip))[-8:]
  if ip_b == ip_b[::-1]:
    c += 1
print(c)

# ip_bin_f = lambda ip : ' '.join([bin(int(i))[2:].zfill(8) for i in ip.split('.')])
# print(ip_bin_f('151.172.115.121'))
# print(ip_bin_f('151.172.115.156'))