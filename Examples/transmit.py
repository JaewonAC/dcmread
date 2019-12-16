import requests
import os

UPLOAD_SINGLE_FILE = True
UPLOAD_MULTIPLE_FILE = False

url = 'http://jac-dt:4000/uploader'
path = 'E:/IMGDATA/20100910S0000007616'

if UPLOAD_SINGLE_FILE:
    files = []
    f = 'I0001597712.dcm'
    with open(path + '/' + f, 'rb') as data:
        files.append(('files[]', (f, data.read())))

if UPLOAD_MULTIPLE_FILE:
    files = []
    for f in os.listdir(path):
        with open(path + '/' + f, 'rb') as data:
            files.append(('files[]', (f, data.read())))

print(requests.post(url, files=files))

