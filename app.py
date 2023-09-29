from flask import Flask, render_template , redirect , url_for , request
import os
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './static/music'

@app.route('/')
def index():
    music_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', music_files=music_files)


@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        music_file = request.files['music']
        if music_file and music_file.filename.endswith('.mp3'):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], music_file.filename)
            music_file.save(filename)
            return redirect(url_for('index'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)

