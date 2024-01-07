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
    i = 0

    while i < len(lines):
        if lines[i].strip().isdigit():
            timecode = lines[i + 1].strip().replace(',', '.')
            start_time, end_time = map(lambda x: datetime.strptime(x, '%H:%M:%S.%f'), timecode.split(' --> '))
            start_time_seconds = start_time.hour * 3600 + start_time.minute * 60 + start_time.second + start_time.microsecond / 1e6
            end_time_seconds = end_time.hour * 3600 + end_time.minute * 60 + end_time.second + end_time.microsecond / 1e6

            text = ''
            j = i + 2
            while j < len(lines) and lines[j].strip() != '':
                text += lines[j].strip() + ' '
                j += 1

            lyrics.append({"time": start_time_seconds, "text": text.strip()})

            i = j
        else:
            i += 1

    return lyrics


# Example usage:

def lrc_to_lyrics(lrc_file):
    lyrics = []
    try:
        with open(lrc_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith('[') and ']' in line:
                time_text = line.strip().split(']')
                for t in time_text:
                    if t.startswith('['):
                        time_str = t[1:]
                        try:
                            min, sec = map(float, time_str.split(':'))
                            time_seconds = min * 60 + sec
                        except ValueError:
                            continue
                    else:
                        text = t.strip()
                        if text:
                            lyrics.append({"time": time_seconds, "text": text})

    except FileNotFoundError:
        print(f"Error: File {lrc_file} not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

    return lyrics

print(srt_to_lyrics('/workspaces/monify-music-app/static/lyrics/Memories.srt'))
# print(lrc_to_lyrics('/Users/gokulakrishnan/Desktop/extra study/Zoom-Clone-With-WebRTC/music_App/static/srt/Sugar - Maroon .lrc'))


@app.route('/')
def index():
    music_files = [file for file in os.listdir(app.config['UPLOAD_FOLDER']) if file.endswith('.mp3')]
    file_name=music_files[0].strip('.mp3')
    srt_file_path='./static/lyrics/'+file_name+'.srt'
    lrc_file_path='./static/lyrics/'+file_name+'.lrc'
    if os.path.exists(srt_file_path):
        lyrics=srt_to_lyrics(srt_file_path)
    elif os.path.exists(lrc_file_path):
        lyrics=lrc_to_lyrics(lrc_file_path)
    else:
        lyrics=[]
    return render_template('index.html', music_files=music_files,lyrics=lyrics)


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
