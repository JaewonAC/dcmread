import requests
import os

UPLOAD_SINGLE_FILE = False
UPLOAD_MULTIPLE_FILE = True

url = 'http://jac-dt:4000/uploader'

if UPLOAD_SINGLE_FILE:
    file = open('E:/IMGDATA/20100910S0000007616/I0001597712.dcm', 'rb')
    files = {'file': file}

if UPLOAD_MULTIPLE_FILE:
    path = 'E:/IMGDATA/20100910S0000007616'
    files = []
    for f in os.listdir(path):
        with open(path + '/' + f, 'rb') as data:
            files.append(('files[]', (f, data.read())))

print(requests.post(url, files=files))

