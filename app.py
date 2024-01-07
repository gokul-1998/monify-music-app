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

from datetime import datetime

def srt_to_lyrics(srt_file):
    with open(srt_file, 'r') as file:
        lines = file.readlines()

    lyrics = []

    for i in range(0, len(lines), 4):
        timecode = lines[i + 1].strip().replace(',', '.')
        start_time, end_time = map(lambda x: datetime.strptime(x, '%H:%M:%S.%f'), timecode.split(' --> '))
        start_time_seconds = start_time.hour * 3600 + start_time.minute * 60 + start_time.second + start_time.microsecond / 1e6
        end_time_seconds = end_time.hour * 3600 + end_time.minute * 60 + end_time.second + end_time.microsecond / 1e6
        text = lines[i + 2].strip()

        lyrics.append({"time": start_time_seconds, "text": text})

    return lyrics

# Example usage:
srt_file_path = 'lyrics.srt'
lyrics_data = srt_to_lyrics(srt_file_path)

@app.route('/')
def index():
    music_files = [file for file in os.listdir(app.config['UPLOAD_FOLDER']) if file.endswith('.mp3')]
    
    return render_template('index1.html', music_files=music_files,lyrics=lyrics_data)


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
