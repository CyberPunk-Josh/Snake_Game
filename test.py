from ftplib import FTP
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import tempfile
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])

app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

FTP_HOST = 'ftp.acquatronix.com'
FTP_USER = 'LaundryWeb'
FTP_PASS = 'i$Rbe0n7#Zm'

ftp = FTP(FTP_HOST)

ftp.login(FTP_USER, FTP_PASS, '')


# ftp.cwd('LaundryWebFTP')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


'''@app.route('/')
def upload_form():
	return render_template('upload.html')'''

'''@app.route('/', methods=['POST'])'''


@app.route('/upload_image', methods=['PUT'])
def upload_file():
    if request.method == 'PUT':
        if 'image' not in request.files:
            # flash('No image part')
            # return redirect(request.url)
            return {'message': 'no image part'}, 404
        image = request.files['image']
        if image.filename == '':
            # flash('No image selected for uploading')
            # return redirect(request.url)
            return {'message': 'No image selected for uploading'}, 404
        if image and allowed_file(image.filename):
            url = 'https://www.acquatronix.com/LaundryWebFTP/'
            filename = secure_filename(image.filename)
            # open connection:

            with tempfile.TemporaryDirectory() as directory:
                image.save(os.path.join(directory, filename))
                urlRela = os.path.join(directory, filename)
                ftp.storbinary("STOR " + os.path.basename(urlRela), open(urlRela, "rb"))
            # ftp.dir()
            # flash('File successfully uploaded')

        # return redirect('/')
        return {'image': url + filename}, 201
    else:
        # flash('Allowed image types are txt, pdf, png, jpg, jpeg, gif')
        # return redirect(request.url)
        return {'message': 'Allowed image types are pdf, png, jpg, jpeg'}, 404


'''@app.errorhandler(413)
def error413(e):
	flash("error: the image exceeds the maximum allowed capacity")
	return redirect('/')'''

if __name__ == "__main__":
    app.run()