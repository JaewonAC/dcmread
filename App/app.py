from flask import Flask, flash, request, redirect, render_template
from redis import Redis, RedisError
from werkzeug.utils import secure_filename

import os
import socket
import pydicom

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__, template_folder='')
app.secret_key = '"super secret key'


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


@app.route('/mupload')
def uploads():
    return render_template('mupload.html')


'''
reference
https://www.tutorialspoint.com/flask/flask_file_uploading.htm
'''
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


'''
reference
https://www.roytuts.com/python-flask-multiple-files-upload-example/
secret key - https://stackoverflow.com/questions/26080872/secret-key-not-set-in-flask-session-using-the-flask-session-extension
'''
@app.route('/muploader', methods=['GET', 'POST'])
def muploader():
    print('uploader')
    if request.method == 'POST':
        # check if the post request has the files part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')

        s = ''
        for file in files:
            filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            s += '<p>' + filename + '</p>'
            print(filename)

        flash('File(s) successfully uploaded')
        return s


if __name__ == "__main__":
    app.debut = True
    app.run(host='0.0.0.0', port=80)
