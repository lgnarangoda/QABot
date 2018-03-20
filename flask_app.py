import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, json
from flask_cors import CORS

file_name = ''
app = Flask(__name__)
CORS(app, resources=r'/*')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'docx'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        global file_name
        file_name = file.filename;
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            import DocumentProcess.pdfreader as pdfreader
            pdfreader.convertMultiple(file)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # import Controller.MainController as MainController
            # answer = MainController.set_filename_and_question(filename)
            #

            return "success save file"


@app.route('/question', methods=['POST'])
def ask_question():
    global file_name
    content = request.get_json(silent=True)
    import Controller.MainController as MainController
    answer = MainController.set_filename_and_question(file_name, content['question'])

    return json.dumps({'answer': answer})


if __name__ == '__main__':
     app.debug = True
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)
