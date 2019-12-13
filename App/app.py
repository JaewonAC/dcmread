from flask import Flask, request, redirect, render_template
from redis import Redis, RedisError
import os
import socket
import pydicom


# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__, template_folder='')


@app.route('/')
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)


@app.route('/test')
def test():
    s = 'test'
    print(s)
    return(s)


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    print('uploader')
    if request.method == 'POST':
        f = request.files['file']
        print(f)
        dcm = pydicom.dcmread(f)
        print(dcm)
        s = '<p>' + dcm.__str__().replace('\n', '</p><p>') + '</p>'
        return(s)

    return 'please POST file.'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    # app.run(host='0.0.0.0', port=80, debug=True)
