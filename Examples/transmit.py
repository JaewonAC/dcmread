import requests

url = 'http://jac-dt:4000/uploader'
file = open('E:/IMGDATA/20100910S0000007616/I0001597712.dcm', 'rb')
files = {'file': file}

print(requests.post(url, files=files))

