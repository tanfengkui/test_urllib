import urllib.request
import urllib

# notice 1 :urllib is move to sub-module request
# notice 2:the url to retrive data is changed, the noaa web site is rebuild.

#response  = urllib.request.urlopen('http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt')
response  = urllib.request.urlopen('http://www.bsb.com.cn/')

print('http header:\n',response .info())
print('http statues:',response .getcode())
print('url:',response .geturl())


for line in response.readlines():
    print(bytes.decode(line,"UTF-8"))

response.close()