from flask import Flask, request, render_template
from collections import Counter
import re

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    text = file.read().decode('utf-8')
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)

    if word_counts:
        most_common_word, most_common_count = word_counts.most_common(1)[0]
        return f'Самое частое слово: "{most_common_word}" с частотой {most_common_count}'
    else:
        return "Файл не содержит слов."




if __name__ == '__main__':
    app.run(debug=True)
