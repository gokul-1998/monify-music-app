"""from flask import Flask, render_template, redirect, url_for, request
from pysrt import open as open_srt
import os
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './static/music'

@app.route('/')
def index():
    music_files = [file for file in os.listdir(app.config['UPLOAD_FOLDER']) if file.endswith('.mp3')]
    return render_template('index.html', music_files=music_files, lyrics=lyrics)

@app.route('/upload', methods=['GET', 'POST'])
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
"""

from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './static/music'

# Define the lyrics data directly in the code
lyrics_data = [
    { 'time': 7.02, 'text': 'Wise men say' },
    { 'time': 13.92, 'text': 'Only fools rush in' },
    { 'time': 21.17, 'text': "But I can't help falling in love with you" },
    { 'time': 35.92, 'text': 'Shall I stay?' },
    { 'time': 42.07, 'text': 'Would it be a sin' },
    { 'time': 49.82, 'text': "If I can't help falling in love with you?" },
    { 'time': 64.57, 'text': 'Like a river flows' },
    { 'time': 68.36, 'text': 'Surely to the sea' },
    { 'time': 71.76, 'text': 'Darling, so it goes' },
    { 'time': 75.25, 'text': 'Some things are meant to be' },
    { 'time': 82.51, 'text': 'Take my hand' },
    { 'time': 88.75, 'text': 'Take my whole life too' },
    { 'time': 104.57, 'text': "For I can't help falling in love with you" },
    { 'time': 111.76, 'text': 'Like a river flows' },
    { 'time': 115.25, 'text': 'Darling, so it goes' },
    { 'time': 118.75, 'text': 'Some things are meant to be' },
    { 'time': 128.64, 'text': 'Take my hand' },
    { 'time': 134.89, 'text': 'Take my whole life too' },
    { 'time': 142.04, 'text': "For I can't help falling in love with you" },
    { 'time': 156.94, 'text': "For I can't help falling in love with you" }
]

@app.route('/')
def index():
    music_files = [file for file in os.listdir(app.config['UPLOAD_FOLDER']) if file.endswith('.mp3')]
    
    return render_template('index.html', music_files=music_files, lyrics_data=lyrics_data)

@app.route('/upload', methods=['GET', 'POST'])
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
