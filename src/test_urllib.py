import urllib.request
import urllib

# notice, that urllib is modified in Python 3, the urlopen is removed to sub-mobule request, also you need import this
# module

f = urllib.request.urlopen('http://www.baidu.com')

d = f.read ()


print (d)