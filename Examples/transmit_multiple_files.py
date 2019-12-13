'''
reference
https://stackabuse.com/the-python-requests-module/
'''

import requests
import os

url = 'http://jac-dt:4000/muploader'
path = 'E:/IMGDATA/20100910S0000007616'
files = []
for f in os.listdir(path):
    with open(path + '/' + f, 'rb') as data:
        files.append(('files[]',(f, data.read())))

print(len(files))

print(requests.post(url, files=files))

